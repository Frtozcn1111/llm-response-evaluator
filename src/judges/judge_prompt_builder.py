from pathlib import Path

from src.models.evaluation_request import EvaluationRequest


class JudgePromptBuilder:
    def __init__(self):
        prompt_path = (
            Path(__file__).parent.parent
            / "prompts"
            / "evaluation_prompt.txt"
        )

        self.template = prompt_path.read_text(encoding="utf-8")

    def build(self, request: EvaluationRequest) -> str:
        return self.template.format(
            prompt=request.prompt,
            response_a=request.response_a,
            response_b=request.response_b,
        )