# Map: Local businesses (parked)

Label: wayfinder:map · Tracker: local markdown (`docs/agents/issue-tracker.md`) · Split from the API spec map 2026-11-04

**Parked by ADR 0004 (2026-11-04).** Its tickets and launch plan stay on file and are not rewritten for chains. Unparking it is a developer decision. Don't work this map's frontier until then.

## Destination

`.scratch/local-businesses/spec.md`: a build spec for the local-businesses product on top of the [engine](../engine/map.md) spec: the NPPES census and census match, launch-state deep research (New York, plus at most one more state), SoS and vet license board connectors, and the local seeding runbook. It must be complete enough that Claude can build it without asking a design question.

## Notes

- The [engine map](../engine/map.md) Notes apply here too: authorship, skills, how to resolve, no application code.
- Shared questions live in engine tickets; a blocker there is written `engine/NN`. Bullets split out of engine tickets on 2026-11-04 are marked with where they came from.
- The parked launch plan is `docs/pre-launch-seeding.md`, with decisions.md §4 and §11.
- **Research tickets**: findings go to `.scratch/local-businesses/research/<slug>.md`.

## Decisions so far

- [Research: NPPES bulk file and API](issues/06-research-nppes.md): monthly ~1.1 GB zip (10.8 GB CSV, 330 cols, V2 only) + weekly incrementals + XLSX deactivations; DBAs only in `othername_pfile`, extra sites only in `pl_pfile`; solo practices may exist only as Type 1 sole proprietors; ~half of dental orgs use individual-section taxonomy codes (org-code filter misses most); API capped at 1,200 results/query and throttled — bulk must use the file; CMS download page was down 2026-10-26; NUCC taxonomy descriptions need a commercial license; authorized-official clusters hint at DSO footprints.
- [Launch states and metros](issues/03-launch-states-and-metros.md): New York is launch state 1. Deep research covers whole launch states, not metros ("showcase metro" dropped), with a per-batch spend cap. An optional second state from FL/CO/TX/AZ only if its SoS data and vet list are cheap. NY vets fall back to a FOIL request, and are roster-only until it arrives. GLOSSARY gains Coverage state and Launch state. The NYC area runs first (added 2026-10-31).
- [Research: SoS and vet license boards in the launch states](issues/11-research-sos-vet-boards.md): Free registry bulk data or API: NY (data.ny.gov; LLCs have no officers), FL (SFTP files, but the site terms say "non-commercial", a conflict) and CO (Public Domain; no officers). TX and AZ are paid or search-only. Vet census: FL licenses vet premises and publishes a free weekly CSV (~2.5k establishments with addresses). AZ licenses premises, but whether a list exists is unconfirmed (site 403). NY and CO license only individuals. Texas facility registration starts in 2027. NY vet list: NYSED "bulk verification files" form (unconfirmed) or FOIL (5/20 business days, cost-only). Dental density evidence is thin.

## Not yet specified

- **Seeding runbooks** — the code entrypoints (CLI) and order for registry → NPPES → roster crawl → census match → vet boards → launch-state batches, and the re-extraction backfill; specifiable once the connector tickets close.

## Out of scope

- Everything the [engine map](../engine/map.md) rules out of scope.
- **Retirement lookup**: in the [retirement map](../retirement/map.md).
