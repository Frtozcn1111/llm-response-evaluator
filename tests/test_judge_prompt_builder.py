from src.judges.judge_prompt_builder import JudgePromptBuilder
from src.models.evaluation_request import EvaluationRequest


def test_build_prompt():
    request = EvaluationRequest(
        prompt="What is AI?",
        response_a="Artificial intelligence is a field of computer science.",
        response_b="AI refers to machines performing intelligent tasks.",
    )

    builder = JudgePromptBuilder()

    prompt = builder.build(request)

    assert "What is AI?" in prompt
    assert "Artificial intelligence is a field of computer science." in prompt
    assert "AI refers to machines performing intelligent tasks." in prompt