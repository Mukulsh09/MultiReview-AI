import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
HF_API_TOKEN = os.getenv("HF_API_TOKEN")

AGENT_CONFIG = {
    "correctness": {
        "provider": "google",
        "model": "gemini-2.0-flash",
    },
    "security": {
        "provider": "google",
        "model": "gemini-2.0-flash",
    },
    "readability": {
        "provider": "google",
        "model": "gemini-2.0-flash-lite",
    },
    "performance": {
        "provider": "huggingface",
        "model": "mistralai/Mistral-7B-Instruct-v0.3",
    },
    "style": {
        "provider": "huggingface",
        "model": "codellama/CodeLlama-34b-Instruct-hf",
    },
}