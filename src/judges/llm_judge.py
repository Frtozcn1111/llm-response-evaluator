from src.judges.judge_prompt_builder import JudgePromptBuilder
from src.models.evaluation_request import EvaluationRequest
from src.models.evaluation_result import EvaluationResult
from src.services.evaluation_result_parser import EvaluationResultParser
from src.services.llm_client import LLMClient


class LLMJudge:
    def __init__(self, client: LLMClient):
        self.client = client
        self.prompt_builder = JudgePromptBuilder()
        self.parser = EvaluationResultParser()

    def evaluate(self, request: EvaluationRequest) -> EvaluationResult:
        prompt = self.prompt_builder.build(request)

        response = self.client.generate(prompt)

        print("\n===== RAW LLM RESPONSE =====\n")
        print(response)
        print("\n============================\n")

        return self.parser.parse(response)