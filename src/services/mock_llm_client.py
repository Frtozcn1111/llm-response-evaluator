import json

from src.services.llm_client import LLMClient


class MockLLMClient(LLMClient):
    def generate(self, prompt: str) -> str:
        return json.dumps(
            {
                "winner": "response_a",
                "scores": {
                    "accuracy": 8,
                    "clarity": 9,
                    "consistency": 8,
                    "safety": 10,
                    "overall": 8.75,
                },
                "reasoning": {
                    "accuracy": "Factually correct.",
                    "clarity": "Clear explanation.",
                    "consistency": "Consistent throughout.",
                    "safety": "No harmful content.",
                },
            }
        )