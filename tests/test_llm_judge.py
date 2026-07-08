from src.judges.llm_judge import LLMJudge
from src.models.evaluation_request import EvaluationRequest
from src.models.evaluation_result import Winner
from src.services.mock_llm_client import MockLLMClient


def test_llm_judge():
    request = EvaluationRequest(
        prompt="What is AI?",
        response_a="Artificial intelligence is a field of computer science.",
        response_b="AI refers to machines performing intelligent tasks.",
    )

    judge = LLMJudge(client=MockLLMClient())

    result = judge.evaluate(request)

    assert result.winner == Winner.RESPONSE_A
    assert result.scores.accuracy == 8
    assert result.scores.clarity == 9
    assert result.scores.overall == 8.75
    assert result.reasoning.safety == "No harmful content."