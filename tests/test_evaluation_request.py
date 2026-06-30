from src.models.evaluation_request import EvaluationRequest


def test_evaluation_request():
    request = EvaluationRequest(
        prompt="What is AI?",
        response_a="Artificial intelligence is a field of computer science.",
        response_b="AI refers to machines performing intelligent tasks."
    )

    assert request.prompt == "What is AI?"
    assert request.response_a.startswith("Artificial")
    assert request.response_b.startswith("AI")