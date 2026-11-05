# Map: Retirement (parked)

Label: wayfinder:map · Tracker: local markdown (`docs/agents/issue-tracker.md`) · Split from the API spec map 2026-11-04

**Deferred by ADR 0004 (2026-11-04).** The employer → plan lookup and the Form 5500 exposure number are not in the first product. Unparking it is a developer decision. Don't work this map's frontier until then.

## Destination

`.scratch/retirement/spec.md`: a build spec for the employer → plan lookup with the free headline exposure number, on top of the [engine](../engine/map.md) spec. It must be complete enough that Claude can build it without asking a design question.

## Notes

- The [engine map](../engine/map.md) Notes apply here too.
- What stays in the engine (ADR 0004): BDC loan data ("BDC discovery and Schedule of Investments parsing") is the first follow-up after the chains-and-brands launch, and Form ADV ingestion stays because it identifies PE firms. The Form 5500 research ticket stays in engine, because engine "Claim value schemas and values over time" depends on it.
- The regulatory line in decisions.md §5 still holds: informational only, never recommend actions.
- **Research tickets**: findings go to `.scratch/retirement/research/<slug>.md`.

## Decisions so far

None yet. Relevant engine research: [Research: Form 5500 bulk data contents](../engine/issues/05-research-form-5500.md) (no per-plan fund lineups in bulk data).

## Not yet specified

- How a user without a Form 5500 plan is routed, now that CAFR pensions are out of scope.
- **BDC fund health** (total PIK %, non-accrual %): facts about a fund, not relations, moved here from the engine on 2026-11-05 (engine "Predicate semantics"). How they are stored and shown is open.

## Out of scope

- **CAFR ingestion**, N-PORT look-through and the paid 401(k)/pension analysis (decisions.md §5, build_roadmap.md §8).
- Everything the [engine map](../engine/map.md) rules out of scope.
