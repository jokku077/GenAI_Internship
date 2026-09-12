# Copilot Instructions for GenAI_fastapi

## Project Intent
This repository is a FastAPI backend for Q&A retrieval using MongoDB, Gemini embeddings, and cosine similarity. Keep route handlers thin and place core logic in handlers.

## Architecture Conventions
- Prefer this flow: API route -> handler/service logic -> db utility access.
- Keep FastAPI route modules in `services/` focused on request validation, orchestration, and HTTP response behavior.
- Put business logic in `handlers/`.
- Keep models in `models/` as clear Pydantic schemas.
- Avoid cross-layer shortcuts (for example, heavy DB logic directly in routes).

## Code Style and Safety
- Use Python logging, not print.
- Add try/except where failures are expected and return consistent HTTP errors.
- Do not introduce secrets, keys, or connection strings in source code.
- Keep changes small and local; avoid unrelated refactors in feature PRs.

## Testing Expectations
- For behavior changes in `handlers/`, `services/`, `models/`, or scoring logic, update/add tests in `tests/`.
- Unit tests must mock external systems (MongoDB, Gemini/embedding calls).
- Keep tests descriptive and scenario-based (`test_<unit>_<scenario>` style).

## PR and Review Expectations
When generating PR-ready changes:
- Summarize behavioral impact and touched modules.
- Include test updates with logic changes.
- Flag any API contract changes explicitly (request/response/status codes).
- Add migration notes for data-shape changes if relevant.

## Review Priorities
Reviewers should prioritize:
1. Correctness of scoring/retrieval logic changes.
2. API contract stability.
3. Test coverage for changed logic paths.
4. Security/config correctness (env vars, no secret leakage).

## Non-Goals
- Do not generate broad rewrites or move large folder structures unless explicitly requested.
- Do not add new dependencies unless justified and documented.
