## Summary
- What problem does this PR solve?
- What is the approach?

## Scope of Changes
- [ ] API route changes (services/user.py, services/admin.py, main.py)
- [ ] Business logic changes (handlers/)
- [ ] Data/model changes (models/, utils/db_utils.py)
- [ ] Test updates (tests/)
- [ ] Documentation updates (README.md or inline comments where needed)

## Review Focus
Please review these first:
- Key files:
- Risky logic paths:
- Backward compatibility concerns:

## Validation
- [ ] Local tests pass with `pytest`
- [ ] New/changed logic has tests or a clear justification for no tests
- [ ] External calls are mocked in unit tests (no live DB/Gemini dependency in unit tests)
- [ ] Logging added/updated where behavior changed (no print statements)

## API/Behavior Impact
- [ ] No API contract changes
- [ ] API contract changed (describe request/response/status-code impact below)

Contract impact details:
- Endpoints:
- Request/response changes:
- Error handling changes:

## Security and Config
- [ ] No secrets or credentials added
- [ ] Environment variable changes documented
- [ ] Input validation and error handling reviewed

## Deployment and Rollback
- Rollout notes:
- Rollback plan:

## Copilot Review Checklist
- [ ] Copilot code review requested on this PR (when applicable)
- [ ] Copilot-generated code was validated and simplified where needed
- [ ] Dead code/imports removed
- [ ] Naming and module boundaries follow project conventions (services thin, handlers own logic)
