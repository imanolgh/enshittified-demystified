# Entity lifecycle: status, merges and renames

Type: grilling
Status: open
Blocked by: 12  (What a business entity is)
Map: [engine](../map.md)

## Question

How do entities change over time: what status values exist, how are duplicates merged (or wrongly merged entities split), can an entity's type change, and what does `renamed_from` do?

## Context

- `entities.status` exists with no vocabulary (evidence_layer_plan.md:89); deactivated NPIs, closed businesses and merged duplicates all need one.
- No `merged_into` mechanism. Append-only claims, edges, aliases and shared public card URLs all need a rule for following a merge.
- **`renamed_from` vs `former_name` alias** (CLAUDE.md:30; evidence_layer_plan.md:92): two mechanisms for one fact. Edge, alias, merge trigger? Does the chain walk cross it?
- **Type changes**: when does a business become a `rollup` (GLOSSARY.md:61)? Entity type of entities created from SoI borrowers or new portfolio names.
- Registry vocabulary (`pe_sponsor | dso_mso | consolidator_brand | platform_co`, registry-research SKILL:14) maps to neither entity_type nor owner kind and uses GLOSSARY-avoided terms.
- **From "What a business entity is"** (2026-11-05, [ADR 0005](../../../docs/adr/0005-brands-companies-locations-separate.md)): `rollup` is no longer an entity type (a rollup is a company), so the rollup part of "Type changes" is settled; SoI borrowers and new portfolio names still need a type rule. New items: a location that moves to a new address is a new location, and the old one needs a closed status; whether old values of a changed identifier (a ticker, a domain) are kept; a strong identifier found on a second entity is a merge signal.
- **From "Schema conventions"** (2026-11-05; conventions in evidence_layer_plan.md §4; no on-demand research per decisions.md §15): `entities.public_id` (12 random Crockford base32 characters, never reused) is what card URLs carry; where a merged entity's public id leads is this ticket's.
- **From "Claim producers and the claims door"** (2026-11-05; summary in evidence_layer_plan.md "Producers and the door"): alias, identifier, address and industry rows now carry `producer` and `producer_version`. When a producer version turns out to be buggy, how its identity rows are withdrawn (no deletes, and these tables have no status) is this ticket's.
- **From "Predicate semantics"** (2026-11-05; role table in evidence_layer_plan.md §4 `claims`): `renamed_from` is still this ticket's: its roles, and whether it stays a predicate or a rename is just a `former_name` alias. New identity table `location_brands` (location → brand, sourced, code producers only); when a store changes brand, how the old row stops counting is this ticket's.
