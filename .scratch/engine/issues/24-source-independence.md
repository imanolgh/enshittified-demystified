# Source independence and syndication

Type: grilling
Status: resolved
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

## Comments

### Round 1 (2026-11-08)

- **Speakers** (Q1): two documents are independent when their speakers differ; a speaker is the organization whose words the document is. Replaces "different source type or domain" in CLAUDE.md, ADR 0002 and the glossary. Official filings still self-verify alone, so the rule matters for company sites, press releases and news.
- **Who the speaker is** (Q2): a company's own site → the entity holding that domain as an identifier (blackstone.com and bxpe.com are both Blackstone), else the domain; a press release → its issuer wherever the copy sits (Warburg's release on PR Newswire, Yahoo Finance or elcarwash.com is Warburg's; how the issuer is read: "Press and EDGAR full-text connectors"); a news article → the outlet's domain unless it copies; an adviser's page (Kirkland & Ellis on Dental365) → the adviser; an official filing → the filer.
- **Copies** (Q3, after the developer asked what fuzzy matching would involve and ruled it out): among the claims supporting one edge, two claims from different speakers with the same quote of at least 80 characters after normalization make the later document a copy with the earlier one's speaker; a wire tag in the text ("/PRNewswire/", "/GLOBE NEWSWIRE/", "(BUSINESS WIRE)") marks a release copy too. No fuzzy matching: two sources describing the same deal in similar words count as two (the developer's ruling). Turned down: overlapping-phrase similarity (a new library and tuning, still misses rewrites) and meaning similarity by embeddings (can't tell copying from independent reporting, and would put a model's judgment on confidence).
- **One voice per ownership group** (Q4): for a hop, documents from the owner, its controlling owners and the companies it controls (the owned brand included) count as one source (Dunkin's site and Inspire's site: one source, reported). The seller is a separate group (Wafra's and Warburg's releases: two sources for El Car Wash); advisers, outlets and regulators are separate (Kirkland's Dental365 page and The Jordan Company's portfolio page: two sources).

## Answer

Resolved 2026-11-08 in a grilling session (one round, recorded under Comments).

- **Rule** (ADR 0002 amended): an edge is verified by two sources from different speaker groups, or by one official filing. A speaker is the organization whose words a document is: a site's owner (by domain identifier, else the domain), a release's issuer wherever it is copied, a news outlet, an adviser, a filer.
- **One voice per ownership group:** for a hop, the owner, its controlling owners and the companies it controls (the owned brand included) count as one source; the seller, advisers, outlets and regulators are separate. Groups come from the control relationships current when the edge is scored.
- **Copies:** within one edge's claims, the same quote of at least 80 characters after normalization from two speakers makes the later document a copy of the earlier; a wire tag ("/PRNewswire/", "/GLOBE NEWSWIRE/", "(BUSINESS WIRE)") marks a release copy. No fuzzy matching (developer's ruling): similar wording from two speakers counts as two sources.
- **Storage:** `documents` gains `speaker_entity_id` (null means the domain is the speaker); an edge's independent-source count is its number of separate groups.
- Docs: ADR 0002 amended, ADR 0003 note, CLAUDE.md invariant, glossary "Independent sources", evidence_layer_plan.md §4, research_flows.md Step 6 example, conformance-tests skill. No new ADR.

Handed on:
- "Press and EDGAR full-text connectors": issuer and wire tags; speakers on press documents.
- "Rosters, portfolio pages and the registry": sponsor pages speak for the sponsor.
- "Entity resolution algorithm": domain identifiers decide whose site a page is.
- "Mechanical docs sweep": python-types-primer.md's old rule.
- chains "Card wording and the how-this-works page": explaining independence.
