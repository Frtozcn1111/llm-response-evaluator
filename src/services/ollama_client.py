import requests

from src.services.llm_client import LLMClient


class OllamaClient(LLMClient):
    def __init__(
        self,
        model: str = "qwen3:32b",
        host: str = "http://localhost:11434",
    ):
        self.model = model
        self.host = host

    def generate(self, prompt: str) -> str:
        response = requests.post(
            f"{self.host}/api/generate",
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False,
                "think": False,
            },
            timeout=300,
        )

        response.raise_for_status()

        return response.json()["response"]