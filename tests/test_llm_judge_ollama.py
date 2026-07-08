from src.judges.llm_judge import LLMJudge
from src.models.evaluation_request import EvaluationRequest
from src.services.ollama_client import OllamaClient


def test_llm_judge_with_ollama():
    request = EvaluationRequest(
        prompt="What is the capital of France?",
        response_a="The capital of France is Paris.",
        response_b="The capital of France is London.",
    )

    judge = LLMJudge(
        client=OllamaClient(model="qwen3:32b")
    )

    result = judge.evaluate(request)

    print(result)

    assert result.winner.value == "response_a"