from src.services.ollama_client import OllamaClient


def test_ollama_client():
    client = OllamaClient(model="qwen3:32b")

    response = client.generate("Reply with exactly one word: hello")

    assert isinstance(response, str)
    assert len(response) > 0