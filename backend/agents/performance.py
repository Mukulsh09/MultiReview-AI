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
        response = self.client.chat_completion(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a code review assistant. Respond only with valid JSON arrays."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.2,
            max_tokens=2000,
        )
        return response.choices[0].message.content