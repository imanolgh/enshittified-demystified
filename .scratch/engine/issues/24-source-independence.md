# Source independence and syndication

Type: grilling
Status: open
Map: [engine](../map.md)

## Question

What precisely makes two sources independent, and how is a syndicated or same-publisher copy detected so it counts once?

## Context

- Rule as written: "different source_type OR domain" (CLAUDE.md:26; ADR 0002:9; evidence_layer_plan.md:191; conformance-tests SKILL:17). As intended: a release syndicated to five sites counts once (GLOSSARY:91–93).
- The written rule counts one wire release on five domains as five sources, and a firm's own site + its own press release as independent — while ADR 0001:9 treats them as one "firm's own words" rank.
- ADR 0003:5,11 says source_type names *who published*, but company_site / press_release / news are genres, not publishers.
- Detection options: text similarity, shared-quote check, wire attribution, same issuer.
- python-types-primer.md:55,107 shows the rule as distinct source_type only (omits domain).
- **From "Claim identity"** (2026-11-06; notes in evidence_layer_plan.md §4 `claims`): claims from the same document share a hash when their names, predicate and quote match, so one document is one source; claims from different documents count separately, subject to this ticket's independence rule.
- **From "Document storage, fetch log and last-confirmed"** (2026-11-07; notes in evidence_layer_plan.md §4 `documents` and `fetches`): each document row carries `domain`, the registrable domain from the public suffix list, and the same text on two URLs is two rows (Warburg's El Car Wash release on PR Newswire and on elcarwash.com). Detecting that they are one source is this ticket's.
- **From "Brand card, receipt and edge shapes"** (2026-11-07; formerly "Claim card and graph output shapes"; glossary "Brand card" and "Receipt"): each edge on a card shows its number of independent sources, so the counting rule this ticket sets is visible to readers.
