# Card wording and the how-this-works page

Type: grilling
Status: open
Blocked by: engine/39, 53  (Claim card and graph output shapes; Brand and chain model)
Map: [chains-and-brands](../map.md)

## Question

What does a brand card say for each outcome (PE-owned, formerly PE, public company, other owner, no evidence, sources disagree), what "what would change this" text does code generate, and what does the public how-this-works page cover?

## Context

- Pivot proposal, **not decided**: positioning "See what private equity owns, since when, and the proof"; show the owner type on every result so a "no" is still useful; "Public company (NYSE: CMG)" or "No PE evidence found (checked {date})". "Not PE-owned" is banned (GLOSSARY).
- From the Worse on Purpose review (handoff §5), proposals: code generates "what would change this" on every card; no AI-written prose on cards, only quotes and computed labels; show acquisition dates; a how-this-works page at launch covering AI, funding and affiliate links.
- Evidence caution: publish who owns it and when, never that it got worse (the "Barbarians at the Store?" paper found PE-backed consumer brands grew sales 50% against matched firms and raised existing prices about 1%).
- Ownership categories are computed by code (ADR 0001); labels come from GLOSSARY.
- **From "Brand and chain model"** (2026-11-06): every brand page carries the same franchise note (draft: "This page reports who owns the brand. A store can be run by a different company, such as a franchisee."); its final text is this ticket's. For the store-map follow-up, a pin shows the brand's verdict labeled as the brand's plus a line saying the store's operator isn't checked; a Dunkin' pin never reads "PE-owned". There is no "parent company" term; how a card labels each owner (including a fund or firm named directly as a brand's owner) is this ticket's.
- **From engine "Claim value schemas"** (2026-11-06; schemas in evidence_layer_plan.md §4 `claims`): an announced deal (`acquired_by` with `deal_status = announced`) is a pending deal, never an ownership hop; how a card or the deal feed shows it is this ticket's.
- **From engine "Owner kind: storage, evidence and the PE-firm test"** (2026-11-07; ADR 0001 amended): a firm that reports private equity funds on Form ADV reads `pe_firm` even if it calls itself something else (Trian, 3G, BDT, JAB), so a card needs wording such as "reports private equity funds on its SEC Form ADV". A self-described PE firm without that filing reads as reported. New category `cooperative_owned`. "Owner type not confirmed" covers owners whose descriptions matched no term.
- **From engine "Funds and their investment firm"** (2026-11-07; ADR 0001 amended): the owner kind `pe_firm` above is renamed `private_equity`; new kinds `real_estate` and `venture_capital` and categories `real_estate_fund_owned` and `venture_capital_owned` need display wording (for example "VC-backed"). A card may name a fund, its managing firm, and the firm's listed parent ("part of Blackstone Inc. (NYSE: BX)", per engine "Claim card and graph output shapes").
- **From engine "Conflict, succession and co-investors"** (2026-11-07; ADR 0001 and ADR 0002 amended): wording is needed for co-owners (an owner who joins doesn't replace the others), an owner line where sources disagree while the category stands, pending deals (Nestlé's agreed sale of Nature's Bounty to Yellow Wood Partners) and deals called off, and how the how-this-works page explains when a past owner stops being shown.
- **From engine "Category precedence and public companies"** (2026-11-07; ADR 0001 amended): wording is needed for a public company that reads PE minority stake (Wendy's: Trian; Restaurant Brands: 3G), for a PE-owned public company with its ticker, for PE holders listed on a public company's card, and for "owner type not confirmed" when a controlling owner's kind is unknown beside a known family owner. The how-this-works page should explain why a fund manager's passive holding never counts.
- **From engine "What 'checked' means and coverage states"** (2026-11-07; ADR 0001 amended): wording is needed for "not yet checked" (owners found so far still shown) and for "checked {date}", whose date is the oldest of the required source runs; the how-this-works page should list the required sources.
