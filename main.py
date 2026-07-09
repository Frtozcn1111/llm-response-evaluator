from src.judges.llm_judge import LLMJudge
from src.models.evaluation_request import EvaluationRequest
from src.services.ollama_client import OllamaClient


def main():
    request = EvaluationRequest(
        prompt="What is the capital of France?",
        response_a="The capital of France is Paris.",
        response_b="The capital of France is London.",
    )

    judge = LLMJudge(
        client=OllamaClient(model="qwen3:32b")
    )

    result = judge.evaluate(request)

    print("=" * 50)
    print("LLM Response Evaluator Demo")
    print("=" * 50)

    print(f"\nWinner: {result.winner.value}")

    print("\nScores")
    print("-" * 30)
    print(f"Accuracy:     {result.scores.accuracy}")
    print(f"Clarity:      {result.scores.clarity}")
    print(f"Consistency:  {result.scores.consistency}")
    print(f"Safety:       {result.scores.safety}")
    print(f"Overall:      {result.scores.overall}")

    print("\nReasoning")
    print("-" * 30)
    print(f"Accuracy:\n{result.reasoning.accuracy}\n")
    print(f"Clarity:\n{result.reasoning.clarity}\n")
    print(f"Consistency:\n{result.reasoning.consistency}\n")
    print(f"Safety:\n{result.reasoning.safety}")


if __name__ == "__main__":
    main()