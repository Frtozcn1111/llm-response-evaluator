# LLM Response Evaluator Architecture

## System Workflow

```text
User Prompt
      ↓
Candidate LLM Responses
      ↓
LLM Judge
      ↓
Evaluation Engine
      ↓
Scoring Report
```
## Core Components
- Prompt Manager
- Response Generator
- LLM Judge
- Evaluation Engine
- Report Generator

## Technology Stack
- Python
- OpenAI API
- Pydantic
- Pytest
- Docker
- GitHub

## Version 1 Scope

### Included

- Single user prompt input
- Two candidate LLM responses
- One LLM judge evaluation
- Scores for:
  - Accuracy
  - Clarity
  - Consistency
  - Safety
- Overall score generation
- JSON evaluation output

### Excluded

- Web interface
- Database
- User authentication
- Multiple judges
- Analytics dashboard
- Fine-tuning

## Input Format

```json
{
  "prompt": "What is artificial intelligence?",
  "response_a": "Artificial intelligence is...",
  "response_b": "Artificial intelligence refers to..."
}
```

## Output Format

```json
{
  "winner": "response_a",
  "scores": {
    "accuracy": 8,
    "clarity": 9,
    "consistency": 8,
    "safety": 10,
    "overall": 8.75
  },
  "reasoning": {
    "accuracy": "Response A provides more accurate information.",
    "clarity": "Response A is easier to understand.",
    "consistency": "Response A is internally consistent.",
    "safety": "No safety issues detected."
  }
}
```
## Class Design

- EvaluationRequest
- JudgePromptBuilder
- LLMJudge
- EvaluationResult
- ReportGenerator

```text
EvaluationRequest
        ↓
JudgePromptBuilder
        ↓
LLMJudge
        ↓
EvaluationResult
        ↓
ReportGenerator
```