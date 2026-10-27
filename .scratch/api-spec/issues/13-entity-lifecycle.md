# Entity lifecycle: status, merges and renames

Type: grilling
Status: open
Blocked by: 12  (What a business entity is)
Map: [api-spec](../map.md)

## Question

How do entities change over time: what status values exist, how are duplicates merged (or wrongly merged entities split), can an entity's type change, and what does `renamed_from` do?

## Context

- `entities.status` exists with no vocabulary (evidence_layer_plan.md:89); deactivated NPIs, closed businesses and merged duplicates all need one.
- No `merged_into` mechanism. Append-only claims, edges, aliases and shared public card URLs all need a rule for following a merge.
- **`renamed_from` vs `former_name` alias** (CLAUDE.md:30; evidence_layer_plan.md:92): two mechanisms for one fact. Edge, alias, merge trigger? Does the chain walk cross it?
- **Type changes**: when does a business become a `rollup` (GLOSSARY.md:61)? Entity type of entities created from SoI borrowers or new portfolio names.
- Registry vocabulary (`pe_sponsor | dso_mso | consolidator_brand | platform_co`, registry-research SKILL:14) maps to neither entity_type nor owner kind and uses GLOSSARY-avoided terms.
