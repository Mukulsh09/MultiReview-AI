import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HF_API_TOKEN = os.getenv("HF_API_TOKEN")

AGENT_CONFIG = {
    "correctness": {
        "provider": "openai",
        "model": "gpt-4o-mini",
    },
    "security": {
        "provider": "openai",
        "model": "gpt-4o-mini",
    },
    "readability": {
        "provider": "openai",
        "model": "gpt-4o-mini",
    },
    "performance": {
        "provider": "huggingface",
        "model": "Qwen/Qwen2.5-Coder-32B-Instruct",
    },
    "style": {
        "provider": "huggingface",
        "model": "meta-llama/Llama-3.1-8B-Instruct",
    },
}