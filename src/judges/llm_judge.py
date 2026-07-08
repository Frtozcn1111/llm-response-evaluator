import json

from src.judges.judge_prompt_builder import JudgePromptBuilder
from src.models.evaluation_request import EvaluationRequest
from src.models.evaluation_result import (
    EvaluationResult,
    Reasoning,
    Scores,
    Winner,
)
from src.services.llm_client import LLMClient


class LLMJudge:
    def __init__(self, client: LLMClient):
        self.client = client
        self.prompt_builder = JudgePromptBuilder()

    def evaluate(self, request: EvaluationRequest) -> EvaluationResult:
        prompt = self.prompt_builder.build(request)

        response = self.client.generate(prompt)

        data = json.loads(response)

        return EvaluationResult(
            winner=Winner(data["winner"]),
            scores=Scores(**data["scores"]),
            reasoning=Reasoning(**data["reasoning"]),
        )