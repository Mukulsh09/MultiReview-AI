import json
import time
import os
from abc import ABC, abstractmethod
from models import AgentResult, Issue


class BaseAgent(ABC):
    def __init__(self, name: str, model: str, provider: str):
        self.name = name
        self.model = model
        self.provider = provider

        # Load prompt template
        prompt_path = os.path.join(
            os.path.dirname(__file__), "..", "prompts", f"{name}.txt"
        )
        with open(prompt_path, "r") as f:
            self.prompt_template = f.read()

    def _build_prompt(self, code: str) -> str:
        """Insert the user's code into the prompt template."""
        return self.prompt_template.replace("{code}", code)

    @abstractmethod
    async def _call_llm(self, prompt: str) -> str:
        """
        Send the prompt to the LLM and return the raw text response.
        Each subclass implements this for its specific LLM provider.
        """
        pass

    def _parse_response(self, raw: str) -> list[Issue]:
        """Parse the LLM's raw text into a list of Issue objects."""
        # Clean up common LLM quirks
        cleaned = raw.strip()

        # Remove markdown code fences if the LLM wraps its response
        if cleaned.startswith("```json"):
            cleaned = cleaned[7:]
        if cleaned.startswith("```"):
            cleaned = cleaned[3:]
        if cleaned.endswith("```"):
            cleaned = cleaned[:-3]
        cleaned = cleaned.strip()

        # Handle empty response
        if not cleaned or cleaned == "[]":
            return []

        try:
            data = json.loads(cleaned)
        except json.JSONDecodeError:
            # If LLM returned malformed JSON, return a single info issue
            return [
                Issue(
                    severity="info",
                    line=0,
                    message=f"Agent '{self.name}' returned unparseable response",
                    suggestion="Review manually or re-run",
                )
            ]

        issues = []
        for item in data:
            try:
                issue = Issue(
                    severity=item.get("severity", "info"),
                    line=item.get("line", 0),
                    message=item.get("message", "No description"),
                    suggestion=item.get("suggestion", "No suggestion"),
                )
                issues.append(issue)
            except Exception:
                continue  # Skip malformed individual issues

        return issues

    async def review(self, code: str) -> AgentResult:
        """
        Main method: build prompt, call LLM, parse response, return result.
        This is what the aggregator calls.
        """
        prompt = self._build_prompt(code)

        start = time.time()
        try:
            raw_response = await self._call_llm(prompt)
            issues = self._parse_response(raw_response)
        except Exception as e:
            # If anything goes wrong, return a graceful error
            issues = [
                Issue(
                    severity="info",
                    line=0,
                    message=f"Agent '{self.name}' encountered an error: {str(e)}",
                    suggestion="Try again or check API key configuration",
                )
            ]
        elapsed_ms = int((time.time() - start) * 1000)

        return AgentResult(
            name=self.name,
            model=self.model,
            response_time_ms=elapsed_ms,
            issues=issues,
        )