from src.models.evaluation_request import EvaluationRequest


class JudgePromptBuilder:
    def build(self, request: EvaluationRequest) -> str:
        return f"""You are an expert AI evaluator.

Evaluate the following two responses.

User Prompt:
{request.prompt}

Response A:
{request.response_a}

Response B:
{request.response_b}
"""