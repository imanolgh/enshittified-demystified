---
name: conformance-tests
description: Write and maintain the project's test suites — golden-fixture conformance tests for connectors, unit tests for core pipeline functions, regression tests. Use whenever tests are needed, a fixture must be added or updated, or a source changed shape in production.
---

# Test Suites & Golden Fixtures

Tests are your territory end to end. The developer runs them (after every change of theirs) but does not write them. Tests exist for regression protection and to verify your own scaffolding — they are not a substitute for the developer's manual verification pass.

## Golden-fixture conformance tests (every connector)
- Fixtures: 2–3 REAL captured responses/pages/files per connector in `tests/fixtures/<connector>/`, named descriptively (`nppes_org_hit.json`, `nppes_no_results.json`, `sponsor_roster_static.html`). Sanitize secrets, keep structure authentic — never hand-invent a fixture.
- The test: run the connector's parse path over each fixture → assert output validates as the contract types (`RawDocument`, enrichment structs, or claims), assert key extracted values match expected constants written into the test, assert graceful behavior on the "empty/miss" fixture.
- **When a source changes shape in production: update the fixture to the new reality FIRST (capture a fresh real sample), watch the test fail, then fix. Fixtures track truth; commits show fixture-then-fix order.**

## Core pipeline tests (highest value in the repo)
- `verify_citations`: quote present; quote absent (auto-reject); whitespace/smart-quote normalization; quote spanning a line break; quote appearing twice (first offset wins); quote in tables text. Include the developer's own edge-case list — ask for it if you don't have it.
- `score_and_publish`: two independent sources → verified; same press release syndicated on two domains → counts once; single source → reported + review_item; conflict → review only; official-filing source self-verifies; `events` row per publication; retraction end-dates without deleting claims.
- Idempotency: re-run the same extraction/filing twice → zero duplicate claims (DB unique index holds).
- Entity resolution: exact hit, fuzzy hit above threshold, ambiguous → review, miss → create.

## Conventions
- pytest; httpx `TestClient` for API tests; a Postgres test database via the compose stack (no SQLite substitution — CTEs and JSONB must match production).
- Factories/helpers in `tests/factories.py`; keep tests readable as documentation of intended behavior.
- Fast suite runnable in one command (`uv run pytest`); mark slow/live-network tests so the default run stays offline against fixtures.
- Never weaken an assertion to make a test pass; if behavior legitimately changed, say so and update expected values with a comment noting why.
