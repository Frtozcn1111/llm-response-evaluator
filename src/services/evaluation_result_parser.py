import json

from src.models.evaluation_result import EvaluationResult
from src.services.response_cleaner import ResponseCleaner


class EvaluationResultParser:
    def parse(self, response: str) -> EvaluationResult:
        response = ResponseCleaner.clean(response)

        start = response.find("{")
        end = response.rfind("}")

        if start == -1 or end == -1:
            raise ValueError("No JSON object found in LLM response.")

        json_text = response[start:end + 1]

        data = json.loads(json_text)

        return EvaluationResult.model_validate(data)