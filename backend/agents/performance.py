from huggingface_hub import InferenceClient
from agents.base_agent import BaseAgent
from config import HF_API_TOKEN, AGENT_CONFIG


class PerformanceAgent(BaseAgent):
    def __init__(self):
        cfg = AGENT_CONFIG["performance"]
        super().__init__(
            name="performance",
            model=cfg["model"],
            provider=cfg["provider"],
        )
        self.client = InferenceClient(token=HF_API_TOKEN)

    async def _call_llm(self, prompt: str) -> str:
        response = self.client.text_generation(
            prompt,
            model=self.model,
            max_new_tokens=2000,
            temperature=0.2,
        )
        return response