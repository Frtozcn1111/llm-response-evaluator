from pydantic import BaseModel


class EvaluationRequest(BaseModel):
    pass
from pydantic import BaseModel


class EvaluationRequest(BaseModel):
    prompt: str
    response_a: str
    response_b: str