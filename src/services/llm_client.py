from abc import ABC, abstractmethod


class LLMClient(ABC):
    @abstractmethod
    def generate(self, prompt: str) -> str:
        """
        Send a prompt to an LLM and return the raw text response.
        """
        pass