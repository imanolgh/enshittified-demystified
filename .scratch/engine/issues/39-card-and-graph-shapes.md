# Brand card, receipt and edge shapes

Type: grilling
Status: resolved
Blocked by: 26, 27, 68  (Edge lifecycle: ending, retraction and staleness; Category precedence and public companies; Category storage and recompute)
Map: [engine](../map.md)
Formerly "Claim card and graph output shapes"; the graph endpoint and non-brand shapes moved to [Graph endpoint and non-brand output shapes](69-graph-endpoint-and-non-brand-shapes.md) on 2026-11-07.

## Question

What do the public output models contain — the business card, the per-claim receipt, edges, and the graph response — and what may be shown from stored documents?

## Context

- **"Claim card" means two things**: step1 guide@HEAD:92 (one claim + quote + provenance) vs evidence_layer_plan.md:203 (business-level card: category, separation degree, sponsor, date, N sources) vs decisions.md:58 (verdict, ownership type…). Name both.
- EdgeOut lost `ownership_type` (ADR 0001); nothing replaces it (category, separation degree, last confirmed, end date?).
- Card contents needed: chains, formerly-PE history, last-confirmed, owner-type-not-confirmed, sources-disagree links, checked date, coverage state, PC jargon hooks; card shapes for rollups, funds, BDCs, retirement plans.
- **Graph endpoint** (build_roadmap.md:121; evidence_layer_plan.md:204): depth cap value; both directions (clinic→DSO→PE firm←lends_to←BDC); relation filters; ended/history edges; node cap for hubs with thousands of locations.
- **Document receipts**: re-serve archived copies (copyright risk for news) or only URL + quote + retrieved_at + sha? pre-launch-seeding.md:119 requires cards to resolve to stored documents.
- `ConfigDict(from_attributes=True)` for ORM-built outputs.
- **Chains and brands** (added 2026-11-04, ADR 0004): output shapes for a brand, a chain, a category page and the public deal feed. Their wording is in chains-and-brands "Card wording and the how-this-works page", the pages in "Website pages and shareable cards".
- **From "Predicate semantics"** (2026-11-05; role table in evidence_layer_plan.md §4 `claims`): the graph has two hop kinds (`owned_by`, `operated_by`) plus non-hop money edges; a store shows both the brand verdict and the store verdict, and code can say whether the store is company-run or franchised (glossary "Operator").
- **From chains-and-brands "Brand and chain model"** (2026-11-06): one verdict per card at launch, the brand's. The store map (follow-up) shows the brand's verdict on each pin, labeled as the brand's; a second, operator verdict waits for operators.
- **From "Entity lifecycle"** (2026-11-06; notes in evidence_layer_plan.md §4 `entities`): a merged entity's card and graph redirect to the survivor's; a `closed` entity (store-map follow-up) still shows its history.
- **From "Funds and their investment firm"** (2026-11-07; ADR 0001 amended; notes in evidence_layer_plan.md §4): the card names the firm that manages a PE fund through its `managed_by` edge without adding a hop, and one (brand, PE owner) row covers a fund and its firm (Jersey Mike's two Blackstone funds give one Blackstone row). Whether and how the card shows a firm's listed parent ("part of Blackstone Inc. (NYSE: BX)") is this ticket's.
- **From "Conflict, succession and co-investors"** (2026-11-07; ADR 0001 and ADR 0002 amended; notes in evidence_layer_plan.md §4 `claims` and `edges`): a card may list several co-owners (THL and Linden at Smile Doctors), an owner line marked sources disagree with each side's links (edge confidence `sources_disagree`) while the category stands, and pending deals (announced, not completed; ended by `terminated` or 18 months). The shapes for these are this ticket's.
- **From "Category precedence and public companies"** (2026-11-07; ADR 0001 amended): a card may show every co-owner with its own chain label, the ticker beside a PE-owned public company (Jersey Mike's, Chewy), PE holders of a public company with their stake ("3G Capital, a PE firm, holds 22% of voting power"), and an unconfirmed controlling owner beside a PE minority stake. The shapes are this ticket's.
- **From "What 'checked' means and coverage states"** (2026-11-07; ADR 0001 amended; tables `document_reads` and `source_runs` in evidence_layer_plan.md §4): a card can be in the state "not yet checked" (no completed check and no PE found), showing any owner found so far; every other non-PE result carries its checked date.
- **From "Document storage, fetch log and last-confirmed"** (2026-11-07; notes in evidence_layer_plan.md §4 `documents` and `fetches`): a claim's receipt links to its child document (a Schedule row, a locator record, a bulk row), which shows its parent filing or file.
- **From "Edge lifecycle: ending, retraction and staleness"** (2026-11-07; notes in evidence_layer_plan.md §4 `edges`): edges carry a phase: `pending` (with an expected closing range when the release gave one), `active`, `unconfirmed` ("last confirmed {date}", not counted) and `ended` (with `end_reason`, feeding "formerly PE-owned {years}"). The shapes are this ticket's.
- **From "Category storage and recompute"** (2026-11-07; tables `entity_categories` and `entity_pe_owner_periods` in evidence_layer_plan.md §4): a card reads the brand's `entity_categories` row (category, confidence, `checked_on`, deciding owner) and its `entity_pe_owner_periods` rows (`active` for current PE owners with separation degree and stake role, `unconfirmed` for "last confirmed", `ended` for "formerly PE-owned {years}"); the chains themselves are walked from the edges on read. This ticket is now takeable.

## Comments

### Round 1 (2026-11-07)

- **Split** (Q0): the graph endpoint (depth caps, directions, relation filters, history edges, node caps), the category page, the public deal feed and company, fund and BDC shapes moved to new ticket "Graph endpoint and non-brand output shapes", which waits on this one; chains "Website pages and shareable cards" now also waits on it. This ticket keeps the brand card, the receipt, the edge and what may be shown from stored documents.
- **Names** (Q1): **brand card** (everything a brand page shows about who owns the brand) and **receipt** (one fact's quote with its source and dates); "claim card" retired; both terms go in the glossary.
- **Brand card sections** (Q2), each shown only when it has something: (1) verdict: category, confidence label, checked date or "not yet checked", a ticker when a public company is in the deciding chain ("PE-owned · NYSE: JMKE"); (2) PE owners: one line per active PE owner period (firm name, funds behind it, separation degree, control or minority, confidence; a listed parent as a label, "part of Blackstone Inc. (NYSE: BX)"); (3) other owners: controlling co-owners and minority holders, each with its chain label; (4) PE holders of a public company ("3G Capital, a PE firm, holds 22% of voting power"); (5) disputes, each side with receipts; (6) pending deals (buyer, announcement date, expected closing range); (7) last confirmed: unconfirmed owners with their date; (8) history: "formerly PE-owned {years}"; (9) the franchise note. BDC lenders join in the first follow-up. Field-level models are Claude's to draft in the spec.
- **Chains** (Q3, refined after the developer asked whether several PE owners at several degrees would all show): the walk branches at every owner and each path stops at its first PE owner, so every PE owner on a separate path gets its own line, chain and degree (brand Z: 60% Company A → Fund X at degree 2, and Fund Y directly at degree 1; Smile Doctors: THL and Linden at degree 1). A PE owner can only sit above another on the same path through a stake in a firm itself (a listed parent, or a GP-stakes holder such as Blue Owl's funds, from memory); those appear as labels on the firm, never as hops or owners of the brand. Every active chain shows hop by hop (phase, confidence, stake, start date, receipts); unconfirmed and ended chains show only in sections 7 and 8, collapsed to owner and dates. Example: Dunkin' → Inspire Brands → Roark Capital.
- **Receipts and stored documents** (Q4): a receipt shows the verbatim quote, the source's name and domain, the source type, a link to the live URL, `published_on`, the first fetch date and the last date the page still showed the same text. The archived copy is never served publicly (it stays internal, as the record in a dispute), except that a child document from an official filing or bulk file (a Schedule row, a Form ADV row, an IRS row) shows its full row text. A dead link gets "This page has changed or is gone; the quote was checked against our copy fetched {date}." The wire-terms question from "Research: Press-release and news feed sources" stays an open legal call for the developer.
- **Edge shape** (Q5): from, to, relation, phase, confidence, `started_on`/`ended_on` with precision, `end_reason`, `last_confirmed_on`, the current value from `value_claim_id`, the expected closing range on a pending edge, the number of independent sources, and the receipts; output models read from database rows (Pydantic `from_attributes`).

### Round 2 (2026-11-07)

- **Passive holdings on a public company's card** (Q6): 13G holdings filed under Rule 13d-1(b) (BlackRock, Vanguard, T. Rowe Price) don't show on the card at all; the how-this-works page explains that index and mutual fund holdings are ordinary passive investments. PE holders and any controlling owner still show (Wendy's shows Trian, not BlackRock or Vanguard).
- **How a fact was read** (Q7, option a): receipts show no reader; the how-this-works page explains that an AI model or a parser reads documents and that every quote is matched word for word against the stored copy. Turned down: a per-receipt "read by AI" label, which puts the method where the source should be.

## Answer

Resolved 2026-11-07 in a grilling session (two rounds, recorded under Comments). Split before round 1: the graph endpoint, category page, deal feed and company, fund and BDC shapes went to "Graph endpoint and non-brand output shapes"; this ticket was renamed from "Claim card and graph output shapes".

- **Names:** **brand card** (everything a brand page shows about who owns the brand) and **receipt** (one fact's quote with its source and dates); "claim card" retired.
- **Brand card sections**, each shown only when non-empty: verdict (category, confidence, checked date or "not yet checked", ticker when a public company is in the deciding chain); PE owners (firm, funds, degree, control or minority, confidence; listed parent as a label); other owners; PE holders of a public company; disputes; pending deals (with expected closing); last confirmed; history ("formerly PE-owned {years}"); the franchise note. BDC lenders join in the first follow-up. Passive 13d-1(b) holdings never show.
- **Chains:** the walk branches at every owner and each path stops at its first PE owner, so every PE owner on a separate path has its own line, chain and degree; a PE firm's own owners (a listed parent, a GP-stakes holder) are labels on the firm. Active chains show hop by hop with receipts; unconfirmed and ended chains are collapsed into their sections.
- **Receipts:** verbatim quote, source name and domain, source type, live link, `published_on`, first fetch date and last date the same text was seen. Archived copies are never served publicly, except the full row text of an official filing's or bulk file's child document; a dead link gets a fixed note. Receipts show no reader (LLM or parser); the how-this-works page explains the method.
- **Edge shape:** from, to, relation, phase, confidence, start and end dates with precision, `end_reason`, `last_confirmed_on`, current value, expected closing range, number of independent sources, receipts; models read from database rows.
- Docs: glossary "Brand card" and "Receipt"; evidence_layer_plan.md card endpoint note; decisions.md §4 note. No ADR.

Handed on:
- "Graph endpoint and non-brand output shapes": the moved shapes.
- "Mechanical docs sweep": the remaining "claim card" mentions.
- chains "Card wording and the how-this-works page": section wording, labels, the dead-link note, how-this-works explanations, private-credit term help.
- chains "Website pages and shareable cards": the brand page is the brand card.
- "Source independence and syndication": the independent-sources count.
- "Press and EDGAR full-text connectors": no re-served wire copies; the wire-terms legal call.
- "API conventions, internal auth and operator surface": output models and the receipt response.
