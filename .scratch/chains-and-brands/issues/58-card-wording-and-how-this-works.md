# Card wording

Type: prototype
Status: resolved
Blocked by: engine/39, 53  (Claim card and graph output shapes; Brand and chain model)
Map: [chains-and-brands](../map.md)

## Question

What does a brand card say, section by section, for each outcome?

(Renamed from "Card wording and the how-this-works page" and narrowed 2026-11-18, round 1 Q0: the generated "what would change this" text moved to "What would change this"; the page moved to "The how-this-works page". Continues as a prototype after round 1: draft cards for real cases, reacted to by the developer.)

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
- **From engine "Edge lifecycle: ending, retraction and staleness"** (2026-11-07): wording is needed for a pending deal with an expected closing ("expected to close by mid-2027"), for an unconfirmed hop ("last confirmed {date}", no longer counted) as opposed to an ended one ("formerly PE-owned {years}"), and for a loan that ended because the lender's next filing no longer lists it.
- **From engine "Brand card, receipt and edge shapes"** (2026-11-07; formerly "Claim card and graph output shapes"): the brand card has nine sections (verdict; PE owners; other owners; PE holders of a public company; disputes; pending deals; last confirmed; history; franchise note), and each needs wording, as do the ticker beside the verdict, the listed-parent label ("part of Blackstone Inc. (NYSE: BX)"), a GP-stakes label on a firm, and the dead-link note ("This page has changed or is gone; the quote was checked against our copy fetched {date}"). The how-this-works page must explain why fund managers' passive holdings never show, and that an AI model or a parser reads documents while every quote is matched word for word; plain-language help for private-credit terms is needed when lenders join. This ticket is now takeable.
- **From engine "Source independence and syndication"** (2026-11-08; ADR 0002 amended): the how-this-works page should explain what two independent sources means: different organizations that don't control each other (a buyer and its seller, a firm and a news outlet); a release copied onto many sites is one source; a company and its owners speak with one voice.
- **From "Product categories: vocabulary and assignment"** (2026-11-16): a brand page names every industry it belongs to; the site states that it covers brands' US businesses; the word "category" never appears on the site (industries, industry pages).
- **From "Alternatives and affiliate links"** (2026-11-17): wording needed for the alternatives block's quality line (chosen by ownership alone, "That isn't a quality rating"), the label next to every affiliate link ("We earn a commission if you buy through this link"), Amazon's required line ("As an Amazon Associate I earn from qualifying purchases") on pages with Amazon links, and a how-this-works section on which programs are used and that commission never sets the order.
- **From "Licensed names in v1"** (2026-11-18): when the USPTO guard applies (a listing-only PE chain, and a USPTO registered owner that is a different, unlinked company), the verdict reads "owner type not confirmed" and the card shows the USPTO owner as an owner line with its receipt; it needs a one-line reason, something like "The name is registered to {company}, which no source links to {company}". Set-aside listing claims and licensees don't show in v1.

## Comments

### Round 1 (2026-11-18)

- **Split** (Q0): this ticket keeps the card wording and continues as a prototype (a page of 8 to 10 drafted cards for real cases: Dunkin', Jersey Mike's, Wendy's, Nature's Bounty, KitchenAid, a no-PE-evidence brand, a formerly-PE brand, a sources-disagree case, a USPTO-guard case). New tickets: "What would change this" (rules for the generated text) and "The how-this-works page".
- **Voice** (Q1): no written prose from an AI model on a card, only computed labels, names, dates and quotes copied word for word; plain words, sentence case, no adjectives; never "independent", "not PE-owned" or "PE-backed"; a card says who owns the brand and since when, never that it got worse; every owner fact links to its receipt.
- **Labels explain themselves** (Q2, revised after the developer asked for no labels a reader must remember, proposing a legend or longer labels; Claude recommended self-explaining labels, since shared cards and screenshots lose a page legend): each verdict keeps its short label with a fixed one-line explanation under it:
  - PE-owned: "A private equity firm owns this brand, directly or through other companies."
  - PE minority stake: "A private equity firm owns part of this brand, less than half."
  - Owned by an investment fund: "A fund that isn't private equity, such as a hedge or credit fund, controls this brand."
  - Owned by a venture capital fund: "A venture capital fund controls this brand." ("VC-backed" turned down: the glossary avoids "-backed".)
  - Owned by a real estate fund: "A real estate fund controls this brand."
  - Owned by a conglomerate: "A company that owns businesses in many unrelated industries controls this brand."
  - Family-owned: "A person or family owns this brand in their own name."
  - Employee-owned: "The company's employees own it, usually through an ESOP."
  - Owned by a trust: "A trust controls this brand."
  - Public company · {ticker}: "A company whose shares trade on a stock exchange controls this brand. No private equity found in its ownership."
  - Nonprofit-owned, Government-owned, Cooperative-owned: "A nonprofit / a government body / its members as a cooperative owns this brand."
  - Owner type not confirmed: "We found who owns it, but no source says what kind of owner it is." (The USPTO guard adds its own reason line naming both companies.)
  - No PE evidence found · checked {date}: "On {date} we finished checking every source on our list and found no private equity in its ownership."
  - Sources disagree: "Our sources say different things about who controls this brand. Each one is shown below."
  - Not yet checked: "We haven't finished checking this brand. Owners found so far are shown below."
  - A ticker shows beside any verdict whose deciding chain runs through a public company ("PE-owned · NYSE: JMKE").
- **Confidence and time, written out** (Q3, revised): every fact reads "Verified by {n} independent sources", "Verified by an official filing ({type})" or "Reported by 1 source"; owners show "since Mar 2017"; history reads "Formerly PE-owned: {firm}, 2010–2021"; an unconfirmed hop reads "No source has shown this since Jun 2025, so we no longer count it"; a pending deal reads "Pending deal: {buyer} agreed to buy this brand on {date}, expected to close by {range}. It doesn't change the verdict until it closes"; checks read "checked Nov 17, 2026". The how-this-works page also gets a "what our labels mean" section, but no card depends on it.

### Prototype (2026-11-18)

- Ten cases (Dunkin', Jersey Mike's, Wendy's, Nature's Bounty, KitchenAid, Casper, Pioneer Woman, and invented Brightway Fitness, Copperline Cookware and Fable Pet Co.) with every section filled in under the round 1 rules; real brands use the audits' quotes, dates are placeholders. File: `.scratch/chains-and-brands/prototypes/card-wording-prototype.html` (kept on main as the primary source). Private link for review: https://claude.ai/artifact/Gqhsabk2oDKkKhfk4Wtasu. Each case lists its open wording questions.

### Round 2, from the prototype (2026-11-18)

- **Chain line** (Q1): keeps the count: "Dunkin' → Inspire Brands → Roark Capital (2 companies up)".
- **Verdict names the owner** (Q2): the verdict names the deciding owner for every category that has one: "PE-owned · Roark Capital", "PE-owned · Blackstone · NYSE: JMKE", "Public company · Whirlpool (NYSE: WHR)", "Family-owned · the Cathy family" (a family only as sources name it); with several PE owners, two names then "+1 more".
- **PE shareholders of a public company** (Q3): section title "Private equity shareholders", with the line "Private equity firms that own part of {company}'s shares, each less than half."
- **Pending deal** (Q4): directly under the verdict: "Pending deal: Yellow Wood Partners agreed to buy this brand on Sep 1, 2026, expected to close by the first half of 2027. It doesn't change the verdict until it closes."
- **Licensees shown** (Q5, revised after the developer asked whether licensees were meant to show; they weren't, per "Licensed names in v1" round 2 Q4, which this amends): when licensing evidence exists, a section "Products under this name" under the owners lists "Licensed to {company}" where the company itself says it holds a license (Lifetime Brands, from its 10-K), "Also listed among {company}'s brands" for a set-aside listing, without calling it a licensee (Meyer), and the line "This page reports who owns the name." The licensee's own ownership isn't shown; its name links to its page if it is in the data.
- **History** (Q6): firm, years, and how it ended when a source says so, with its receipt: "Formerly PE-owned: Durational Capital Management, 2022–2024. Sold to Carpenter Co. in 2024."
- **What we checked** (Q7, revised after the developer asked to name the sources even when no PE evidence is found): every checked card shows each required source with the date it last finished and how many documents it read for the brand ("SEC full-text search · Nov 12, 2026 · 3 documents"); documents that named an owner link from their facts, the rest are listed under each source and can be expanded. When no source named an owner at all, the verdict adds "No source we checked named an owner."
- **Disputes** (Q8): each reading shows its result, computed by code: "If this is right: PE-owned"; "If this is right: Family-owned".

## Answer

Resolved 2026-11-18 in two rounds: principles (round 1), then reactions to a ten-case prototype (round 2). Split before round 1: "What would change this" and "The how-this-works page" became their own tickets.

- **Voice:** computed labels, names, dates and verbatim quotes only; plain words, sentence case; never "independent", "not PE-owned" or "PE-backed"; who owns it and since when, never that it got worse; a receipt on every fact.
- **Verdict:** short label plus the deciding owner (and ticker where a public company is in the deciding chain), with a fixed one-line explanation under it (the round 1 table); confidence written out ("Verified by {n} independent sources", "Verified by an official filing ({type})", "Reported by 1 source"); "No source we checked named an owner" when none did; the USPTO guard's reason line where it applies.
- **Order of sections:** verdict; pending deal; private equity owners (firm, owner kind with the Form ADV reason, role and stake, "since {Mon YYYY}", the chain with its count of companies up, the funds); private equity shareholders of a public company; other owners or other companies in the chain; products under this name (licensees and set-aside listings); where sources disagree (each reading with "If this is right: {category}"); "No source has shown this since {Mon YYYY}, so we no longer count it" lines; history ("Formerly PE-owned: {firm}, {years}. {How it ended}."); the franchise note; alternatives (from "Alternatives and affiliate links"); what we checked; the receipts note with the dead-link line.
- **Fixed lines:** franchise note "This page reports who owns the brand. A store can be run by a different company, such as a franchisee."; "This page covers the brand's US business."; dead link "This page has changed or is gone; the quote was checked against our copy fetched {date}."; alternatives "No private equity found in these brands' ownership. That isn't a quality rating."; affiliate "We earn a commission if you buy through this link." plus Amazon's line where it applies.
- **Prototype:** `.scratch/chains-and-brands/prototypes/card-wording-prototype.html` (round 1 rules; round 2 decisions not folded in), private link https://claude.ai/artifact/Gqhsabk2oDKkKhfk4Wtasu; kept on main as the primary source (developer, 2026-11-18: prototypes may live on main).
- Docs: no glossary or ADR change; "Licensed names in v1" amended (licensees now show).

Handed on:
- "Website pages and shareable cards": the section order and every fixed line above; layout, type and styling are its own (the prototype's look isn't a decision).
- "What would change this": the voice rules and the confidence wording it must use.
- "The how-this-works page": the "what our labels mean" backup section, and every topic already listed there.
- "Brand-level checked: required sources and freshness": the "What we checked" section lists each required source with its last finished date and document count.
- engine "Brand card, receipt and edge shapes" (amended): the card shape gains the deciding owner on the verdict, a products-under-this-name section, a what-we-checked section (from `source_runs` and `document_reads`) and each dispute reading's category.
- non-PE owners "Brand licensors and licensees on the brand page": showing licensees moved into v1 in this limited form.
