---
name: doc-digest
description: Research a third-party API, bulk file, or data source and produce an integration brief so the developer can write the connector without reading the raw docs. Use when asked to "digest", "research", or "read the docs for" NPPES, EDGAR, Form 5500/EFAST, Google Places, state SoS sites, license boards, CourtListener, sponsor sites, or any new source.
---

# Documentation Digest

Purpose: the developer integrates from your brief, never from the vendor's docs. The brief must be complete enough to write the connector in one sitting, and honest about what you couldn't verify.

## Output format (always this structure)

1. **Source overview** — what it is, what evidence it yields for this project, which pipeline stage it serves (map to evidence_layer_plan.md stages).
2. **Access** — base URL(s), auth (key? none?), cost per call if paid, rate limits (documented AND observed), bulk-file availability (URL, format, size, refresh cadence).
3. **Request reference** — every endpoint/parameter the connector will need, with types and quirks. For bulk files: every relevant column with meaning. Omit what the project won't use, but say what you omitted.
4. **Response reference** — schema of what comes back, field meanings, null/edge behaviors, pagination.
5. **Two real examples** — an actual request and its actual (redacted-if-needed) response, fetched live if possible. These become the seed of the fixture files.
6. **Gotchas** — encoding issues, name-matching quirks, downtime patterns, undocumented behavior found in community sources. Distinguish "documented" from "reported by users" from "I observed".
7. **Mapping suggestion** — how responses map onto `app/core/contracts.py` types (`RawDocument` fields, resolution enrichment, or claim inputs). Suggestion only — the developer decides.

## Rules
- Cite URLs for every factual claim about the source.
- If docs conflict with observed behavior, say so explicitly — observed wins, flagged.
- If a source has both an API and a bulk file (NPPES, Form ADV), cover BOTH and recommend which serves seeding vs. freshness (per decisions.md §11: bulk for seeding, API for freshness).
- Never write the connector itself. End the brief with "Ready for you to write `app/connectors/<name>.py` — want scaffolding?"
