# Ownership category is computed by code from owner kind and the ownership chain

Status: accepted (2026-10-26). Supersedes the LLM `ownership_type` classification in `evidence_layer_plan.md` §4–§5 and `build_roadmap.md` Steps 7 and 27b.

A business's category (PE-owned, family-owned, No PE evidence found, etc.) is never chosen by the LLM. Each owner entity carries an **owner kind** (`pe_firm, other_investment_fund, conglomerate, family, employee_owned, trust, public_company, nonprofit, government`), and code computes each business's **category** by walking its ownership chains. We chose this because a category is a judgment no verbatim quote can prove, a per-link label stores the same owner fact many times so the copies can disagree, and reclassifying one owner must update every business beneath it automatically.

## Rules

- **Owner kind sources, ranked** *(amended 2026-10-26)*: (1) official filings (Form ADV, SEC filings/ticker, Form 5500 ESOP, IRS exempt-organization / Form 990) > (2) the firm's own words, quoted from its `company_site` or its own `press_release` > (3) third-party `news`, quoted. Ranks 2–3 are read by the LLM from a verbatim quote checked by `verify_citations` and publish as `reported`. A higher rank wins outright; a contradiction within the same rank gives "owner type not confirmed". The registry is a crawl list, never evidence, so it has no rank.
- **PE firm vs other funds:** `pe_firm` = a Form ADV adviser with at least one fund of type "private equity fund". An adviser whose funds are only venture capital, hedge, or real estate is `other_investment_fund`, and a business it owns is `investment_fund_owned` — "PE-owned" never stretches to mean any investor.
- **Chain walk:** walk up from the business until the first entity whose owner kind is `pe_firm` (fund or firm), or the top. Unclassified intermediate owners do not block. PE anywhere in a chain beats the top owner's kind (a Blackstone fund under Blackstone Inc. is still PE). An unclassified top with no PE → "owner type not confirmed".
- **Control vs minority:** a hop is control unless a quoted document states a stake under 50% or calls it a minority investment. Any minority hop makes that chain minority. A control chain to PE → `pe_owned`; only minority PE chains → `pe_minority_stake`, which still outranks every non-PE category (the card shows the controlling non-PE owner beside it).
- **Separation degree:** one stored row per (business, PE firm), counting hops to the first PE entity (direct ownership = 1); the card also names the firm without adding a hop. Ownership hops only (`acquired_by, owned_by, operates_location_of`), never `lends_to`. Recomputed whenever a hop or an owner kind is published, ended, or retracted.
- **Confidence:** a category is `verified` only if every hop and the deciding owner kind are verified; otherwise `reported`.
- **Time:** a new controlling-owner claim ends the previous owner's hop (end date = new claim's date, with an `events` row). A hop with no source confirming it for 18 months shows "last confirmed {date}" and stops counting as current. Ended PE ownership appears on the card as "formerly PE-owned {years}" history, not as a category.
- **Never "independent":** a business with no PE chain is `no_pe_evidence_found` (checked {date}). The only future route to the word is the Certified Independent badge (automated checks against official records) — **not in the MVP** (2026-10-26).

## Categories (`BusinessCategory`)

`pe_owned, pe_minority_stake, investment_fund_owned, conglomerate_owned, family_owned, employee_owned, trust_owned, public_company_owned, nonprofit_owned, government_owned, owner_type_not_confirmed, no_pe_evidence_found, sources_disagree`

## Considered options

- **LLM classifies per document** (the original plan): best coverage, but unprovable, inconsistent across documents, and not repeatable.
- **Official sources only:** most defensible, but family/trust/conglomerate owners have no official marker, so most would be "not confirmed".
- **Label on each link:** already in the schema and one query to read, but duplicates the owner fact and cannot express "PE three hops up".
