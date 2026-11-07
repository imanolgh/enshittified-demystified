# Entity lifecycle: status, merges and renames

Type: grilling
Status: resolved
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

## Comments

### Round 1 (2026-11-06)

Boundaries: the type a newly seen name gets and hash stability are "Claim identity"; other merge rules are "Entity resolution algorithm"; edge retraction is "Edge lifecycle"; the events row is "Events and the public changelog"; the registry `kind` vocabulary is "Rosters, portfolio pages and the registry". ADR 0002 rules out hand edits of individual facts; fixes are code changes plus a re-run.

- **Status** (Q1): `active | merged | closed`, set only by code. `closed` = the thing stopped existing (a location that moved leaves a closed one, ADR 0005). Nothing sets it at launch; the store-map follow-up sets it when a store drops out of its locator (diff owned by "Rosters…" and "Edge lifecycle"). A discontinued brand leaves the launch lists ("Category brand lists and brand-level checked").
- **Merge by pointer** (Q2): the duplicate gets `status = merged` and `merged_into_id`; its claims and identity rows keep their entity id; reads follow the pointer to the end of the line and both entities' names count toward the canonical name. The duplicate's edges are retracted and the survivor's recomputed from both entities' claims, with an events row. The older entity (lower id) survives. The duplicate's `public_id` redirects (301) to the survivor, never reused, never a 404. A wrong merge is undone by clearing the pointer.
- **Only code merges** (Q3, option a): same strong identifier on two entities of the same type merges them; same identifier, different types → no merge, an alert. Other rules (name plus address) are "Entity resolution algorithm", with a dedup pass re-running them after a rules change. A merge is undone when the identifier row that triggered it is retracted. No hand merge or split; an uncaught duplicate stays until a source supplies a shared identifier.
- **`renamed_from`** (Q4, option a): kept, with no object. Subject = the entity under its current name; `value.former_name` = the old name, which must appear in the quote. An accepted claim makes code write a `former_name` alias citing the document. If the old name matches another same-type entity, they merge only once the rename is verified. Never a hop. `claims.object_entity_id` becomes nullable for `renamed_from` only.
- **Identity history and retraction** (Q5): alias, identifier, address, industry and `location_brands` rows are never deleted. A newer document's different value doesn't remove the old row; the current value is the newest document's, and old values stay as history (their weight in matching is "Entity resolution algorithm"'s). The tables gain `retracted_at`, set by code only when a whole `producer` + `producer_version` is withdrawn by one operator command after a code fix, followed by a re-run. No single-row retraction. Each retraction writes an events row; a retracted identifier undoes a merge it triggered. Claims and edges of that version: "Edge lifecycle".
- **Type changes** (Q6): code may change `company` to `investment_firm` or `fund` when a Form ADV identity record matches, with an events row. Brands and locations never change type and nothing becomes one. The type a claim-created entity starts with is "Claim identity"'s.

### Round 2 (2026-11-06)

- **Merge trigger, made precise** (Q7): strong identifiers have one holder (unique index), so the collision appears at resolution. An identity record whose strong identifiers already belong to two different same-type entities merges them. An identifier on one entity plus a name match on another is a name rule ("Entity resolution algorithm"). A merge is also undone when the verified `renamed_from` that triggered it is retracted. The unique index ignores retracted rows.

## Answer

Resolved 2026-11-06 in a grilling session (two rounds, recorded under Comments).

- **Status:** `active | merged | closed`, set only by code. Nothing sets `closed` at launch; the store-map follow-up sets it when a store drops out of its locator.
- **Merges add a pointer, never rewrite rows.** The duplicate gets `status = merged` and `merged_into_id`; its claims and identity rows keep their entity id; reads follow the pointer to the end. The duplicate's edges are retracted and the survivor's recomputed from both entities' claims, with an events row. The older entity survives; the duplicate's `public_id` redirects (301). Undo = clear the pointer.
- **Only code merges** (ADR 0002 amended): an identity record whose strong identifiers belong to two same-type entities merges them; different types → no merge, an alert. Other rules and a dedup pass are "Entity resolution algorithm"'s. A merge is undone when the identifier row or the verified `renamed_from` that triggered it is retracted. No hand merge or split.
- **`renamed_from`** stays, with no object: subject = the entity under its current name, `value.former_name` = the old name (in the quote). An accepted claim makes code write a `former_name` alias; a match to another same-type entity merges only once the rename is verified. Never a hop.
- **Identity rows** keep their history (the newest document's value is current) and gain `retracted_at`, set only when one operator command withdraws a whole `producer` + `producer_version` after a code fix, followed by a re-run. Each retraction writes an events row. The strong-identifier unique index ignores retracted rows.
- **Type changes:** only `company` → `investment_firm` or `fund`, by code, when a Form ADV identity record matches, with an events row. Brands and locations never change type.
- No new ADR, no glossary change.

Handed on:
- "Claim identity": the type of a claim-created entity, the hash across pointer merges, the nullable object.
- "Entity resolution algorithm": name-based merge rules, the dedup pass, the weight of old values.
- "Edge lifecycle": edges on merge, withdrawing a version's claims, `closed` from locator diffs.
- "Events and the public changelog": the event kinds.
- "API conventions and operator surface": the 301 redirect, the withdraw-version command.
- "Operational identity and guardrails": the different-type alert.
- Also "Owner kind", "Form ADV and IRS exempt-org ingestion", "Claim value schemas", "Citation verification rules", "Card and graph shapes", "Rosters, portfolio pages and the registry", and chains "Category brand lists and brand-level checked".
