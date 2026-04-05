from google import genai
from agents.base_agent import BaseAgent
from config import GOOGLE_API_KEY, AGENT_CONFIG


class ReadabilityAgent(BaseAgent):
    def __init__(self):
        cfg = AGENT_CONFIG["readability"]
        super().__init__(
            name="readability",
            model=cfg["model"],
            provider=cfg["provider"],
        )
        self.client = genai.Client(api_key=GOOGLE_API_KEY)

    async def _call_llm(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
            config=genai.types.GenerateContentConfig(
                temperature=0.2,
                max_output_tokens=2000,
            ),
        )
        return response.text