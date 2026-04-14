from openai import AsyncOpenAI
from agents.base_agent import BaseAgent
from config import OPENAI_API_KEY, AGENT_CONFIG


class ReadabilityAgent(BaseAgent):
    def __init__(self):
        cfg = AGENT_CONFIG["readability"]
        super().__init__(name="readability", model=cfg["model"], provider=cfg["provider"])
        self.client = AsyncOpenAI(api_key=OPENAI_API_KEY)

    async def _call_llm(self, prompt: str) -> str:
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a code review assistant. Respond only with valid JSON arrays."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.2,
            max_tokens=2000,
        )
        return response.choices[0].message.content