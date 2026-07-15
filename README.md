# LLM Response Evaluator

A lightweight framework that uses an LLM-as-a-judge to compare two candidate responses to the same prompt and score them against a structured rubric — accuracy, clarity, consistency, and safety — producing a JSON verdict with reasoning for each criterion.

This project started as a way to formalize how I already evaluate LLM outputs by hand: reading two answers to the same question, deciding which one is factually stronger, clearer, more internally consistent, and safer, and being able to explain *why*. The code externalizes that judgment process into a repeatable pipeline instead of a one-off gut call.

## Why this exists

Most "LLM eval" demos just ask a model "which is better?" and take the answer at face value. That's not useful when you actually care about *why* one response wins — for annotation, QA, or training-data curation work, the reasoning behind a score matters as much as the score itself. This project forces the judge model to:

- Score four criteria independently instead of one vague "overall" impression
- Justify each score in plain language
- Follow a strict priority order when picking a winner (accuracy > clarity > consistency > safety)
- Return a single, strictly-formatted JSON object — no prose, no markdown fences — so the output is machine-parseable

The rubric, the priority ordering, and the output schema are the actual design work here; the judge model is just the executor.

## How it works

```
User Prompt + Response A + Response B
              ↓
     JudgePromptBuilder   (fills a fixed rubric template)
              ↓
        LLM Judge         (Ollama / any LLMClient implementation)
              ↓
   Response Cleaner + Parser   (strips markdown fences, extracts JSON)
              ↓
       EvaluationResult   (Pydantic-validated, typed)
```

## Example

**Input**
```json
{
  "prompt": "Explain recursion to a 10-year-old in under 100 words.",
  "response_a": "Recursion is when something solves a problem by using a smaller version of itself...",
  "response_b": "Imagine you have a set of Russian nesting dolls..."
}
```

**Output**
```json
{
  "winner": "response_b",
  "scores": {
    "accuracy": 9.0,
    "clarity": 9.5,
    "consistency": 9.0,
    "safety": 10.0,
    "overall": 9.3
  },
  "reasoning": {
    "accuracy": "Both explanations are factually correct; response B's analogy maps more precisely to the base-case concept.",
    "clarity": "The nesting-doll metaphor is more concrete and age-appropriate than the mirror analogy.",
    "consistency": "No internal contradictions in either response.",
    "safety": "No safety concerns in either response."
  }
}
```

## Project structure

```
src/
├── models/       # Pydantic schemas: EvaluationRequest, EvaluationResult, Scores, Reasoning
├── judges/       # JudgePromptBuilder (rubric templating) + LLMJudge (orchestration)
├── services/     # LLMClient interface, OllamaClient, MockLLMClient, response parsing/cleaning
└── prompts/      # The rubric itself, as an editable text template
tests/            # Unit tests (mocked LLM) + integration tests (live Ollama)
```

The `LLMClient` abstract base class is the key seam: swap `OllamaClient` for any other backend (OpenAI, Anthropic, a local vLLM server) without touching the judging logic.

## Setup

```bash
pip install -r requirements.txt

# Requires a local Ollama instance for the live client:
# https://ollama.com
ollama pull qwen3:32b

python main.py
```

Unit tests run against a mocked LLM client and don't require Ollama:

```bash
pytest tests/test_evaluation_request.py tests/test_evaluation_result.py \
       tests/test_judge_prompt_builder.py tests/test_llm_judge.py
```

## Design decisions

- **Why four separate criteria instead of one score?** A single "quality" number hides *what* went wrong. Splitting accuracy/clarity/consistency/safety makes disagreements legible and lets a human auditor spot exactly where a response fails.
- **Why this priority order for picking a winner?** Accuracy first, because a clearer but wrong answer is worse than a correct but slightly awkward one. Safety is checked last only because both candidate responses are assumed to already pass a baseline safety bar in this v1 scope — it still gates the score, it just isn't the tiebreaker.
- **Why a Mock client for tests?** LLM judges are non-deterministic. Unit tests validate the *pipeline* (parsing, schema validation, prompt construction) against a fixed fake response, while a separate integration test validates the real model end-to-end.

## Current limitations (v1 scope)

- Single judge model only — no multi-judge consensus or inter-rater agreement scoring yet
- Two responses at a time — no N-way comparison
- No retry/fallback if the judge model returns malformed JSON
- No CLI or web interface — this is a library/demo, invoked from `main.py`

## Roadmap

- [ ] Add schema-validation retry with automatic re-prompting on parse failure
- [ ] Support N-way response comparison, not just A/B
- [ ] Add a second judge model for cross-verification (reduce single-model bias)
- [ ] Weighted, code-computed `overall` score instead of letting the judge model compute it

## Tech stack

## Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.14 |
| LLM | Ollama + Qwen3:32B |
| Validation | Pydantic v2 |
| Networking | Requests |
| Testing | Pytest |
| Version Control | Git, GitHub |
| IDE | Visual Studio Code |