# Testing and acceptance bars

Type: grilling
Status: open
Blocked by: 02  (Docs governance and definition of done)
Map: [api-spec](../map.md)

## Question

How is the build verified when no human hand-checks it: prompt golden tests, acceptance thresholds per component, and the launch gate?

## Context

- **Prompt golden-fixture tests** (CLAUDE.md:7): LLM output varies and costs money — offline replay of recorded responses + a frozen live eval set with precision/recall pass bars run on demand?
- **Acceptance bars**: Steps 18 and 27 measure outcome distributions without pass thresholds — quote-pass rate, resolution precision on a labeled set, BDC row accuracy. An agent can't judge "good enough" alone.
- **Launch gate** replacing W8 (pre-launch-seeding.md:94): share of `reported` and `sources_disagree` — no number.
- **Definition of done shape is settled** ("Docs governance and definition of done", CLAUDE.md working rules): fixtures + recorded live lookup + automatic BDC XBRL cross-check + developer commit. This ticket sets the numbers: what the live lookup must show to pass, the XBRL match threshold, fixture counts per source kind.
- Labeled resolution set: commit the "dozen tricky names" (build_roadmap.md:101) as a fixture.
- Harness defaults: Celery eager + one real-worker chord test; respx for httpx; local static server for Playwright; MinIO; bulk fixtures as real-row slices; property tests for chains/categories; per-test transaction rollback; Postgres test DB (no SQLite — conformance-tests SKILL).
