import json
import re

from src.models.evaluation_result import EvaluationResult


class EvaluationResultParser:
    def parse(self, response: str) -> EvaluationResult:
        response = response.strip()

        # Remove Markdown code fences if present
        response = re.sub(r"^```(?:json)?", "", response)
        response = re.sub(r"```$", "", response)
        response = response.strip()

        # Extract first JSON object if extra text exists
        start = response.find("{")
        end = response.rfind("}")

        if start == -1 or end == -1:
            raise ValueError("No JSON object found in LLM response.")

        json_text = response[start:end + 1]

        data = json.loads(json_text)

        return EvaluationResult.model_validate(data)