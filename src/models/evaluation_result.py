from enum import Enum

from pydantic import BaseModel


class Winner(str, Enum):
    RESPONSE_A = "response_a"
    RESPONSE_B = "response_b"
    TIE = "tie"


class Scores(BaseModel):
    accuracy: float
    clarity: float
    consistency: float
    safety: float
    overall: float

class Reasoning(BaseModel):
    accuracy: str
    clarity: str
    consistency: str
    safety: str

    
class EvaluationResult(BaseModel):
    winner: Winner
    scores: Scores
    reasoning: Reasoning