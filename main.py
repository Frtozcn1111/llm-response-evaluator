from src.judges.llm_judge import LLMJudge
from src.models.evaluation_request import EvaluationRequest
from src.services.ollama_client import OllamaClient


def main():
    request = EvaluationRequest(
        prompt="Explain recursion to a 10-year-old in under 100 words.",

        response_a=(
            "Recursion is when something solves a problem by using a smaller version of itself. "
            "Imagine two mirrors facing each other—they reflect the same image over and over. "
            "In programming, a recursive function calls itself until it reaches a stopping point "
            "called the base case. Without a base case, the function would continue forever."
        ),

        response_b=(
            "Imagine you have a set of Russian nesting dolls. "
            "You open the biggest doll and find a smaller one inside, then another, and another, "
            "until you reach the tiniest doll. "
            "Recursion works the same way: a problem is solved by breaking it into smaller versions "
            "of itself. When it reaches the smallest problem, it starts finishing each step one by one."
        ),
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