from src.models.evaluation_result import (
    EvaluationResult,
    Reasoning,
    Scores,
    Winner,
)


def test_evaluation_result():
    scores = Scores(
        accuracy=8,
        clarity=9,
        consistency=8,
        safety=10,
        overall=8.75,
    )

    reasoning = Reasoning(
        accuracy="Factually correct.",
        clarity="Clear explanation.",
        consistency="Internally consistent.",
        safety="No harmful content.",
    )

    result = EvaluationResult(
        winner=Winner.RESPONSE_A,
        scores=scores,
        reasoning=reasoning,
    )

    assert result.winner == Winner.RESPONSE_A
    assert result.scores.accuracy == 8
    assert result.scores.overall == 8.75
    assert result.reasoning.safety == "No harmful content."