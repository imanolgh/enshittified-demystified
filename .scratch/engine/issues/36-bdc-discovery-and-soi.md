# BDC discovery and Schedule of Investments parsing

Type: grilling
Status: resolved
Blocked by: 08, 16  (Research: EDGAR access, BDC identification and SoI formats; Claim value schemas and values over time)
Map: [engine](../map.md)

## Question

How is the BDC universe discovered, which filings are loaded, how are Schedules of Investments turned into `lends_to` claims, and who is the lender?

## Context

- Ruled 2026-10-26: the `bdc_soi` parser is the only source of SoI `lends_to` claims, no LLM fallback; failing rows rejected; above a per-filing failure-rate threshold the filing is withheld + operational alert (ADR 0002). Threshold and row tolerance unvalued.
- **Input format**: build_roadmap.md:11,117 ("PDF parser", "open each filing PDF") vs bdc-parser SKILL:11 ("PDF or filing HTML"); EDGAR filings are mostly HTML; inline XBRL may replace table parsing (bdc-parser SKILL:26) — from "Research: EDGAR access…".
- **Who lends to whom**: build_roadmap.md:119 and pre-launch-seeding.md:117 show "…sponsor ← lends_to ← BDC"; research_flows.md:134 and decisions.md:20 have the BDC lending to the portfolio company (the DSO). Lender entity = the BDC or its adviser?
- Several tranches per borrower: claim per row vs edge per borrower.
- Include non-traded/private BDCs? 10-Q handling, amendments; "in thousands" scaling inside the cross-check.
- **History at launch**: diffs need the prior quarter (research_flows.md:162) — latest filing only, or one prior too?
- Fund-level totals (PIK %, non-accrual %) need a non-relation fact form ("Predicate semantics").
- `parse_soi` (research_flows.md:131) vs `bdc_soi` naming.
- **From "Claim producers and the claims door"** (2026-11-05; summary in evidence_layer_plan.md "Producers and the door"): the BDC parser is the `parser` producer. A claim quotes the row's parsed-table text; if the parser reads DERA `soi.tsv`, each holding is a bulk row and quotes its whole data line. Per-record failures raise alerts; the per-filing withhold rule stays with this ticket and "Citation verification rules".
- **From "Predicate semantics"** (2026-11-05; role table in evidence_layer_plan.md §4 `claims`): equity rows in a Schedule (common units, warrants, preferred) emit `holds_position` (fund → company), never an ownership hop. Open here: whether a row in the Schedule's "control investments" section should also yield `owned_by`. Fund-level totals (PIK %, non-accrual %) are no longer emitted; they moved to the retirement map.
- **From "ExtractedClaim and the extraction result envelope"** (2026-11-06): an unparseable Schedule section or filing is a parse failure with an alert, never `no_evidence_found` (ADR 0002 and the bdc-parser skill corrected). A Schedule that parses cleanly with no row for a borrower counts as read: no lending evidence in that filing.
- **From "Claim value schemas"** (2026-11-06; schemas in evidence_layer_plan.md §4 `claims`): `lends_to` and `holds_position` value fields follow the SEC tags: `instrument`, `reference_rate`, `spread_pct`, `interest_rate_pct`, `pik_rate_pct`, `floor_pct`, `principal`, `cost`, `fair_value`, `currency`, `scale`, `non_accrual`, `maturity_date`, `affiliation` (from the Issuer Affiliation axis or the section heading). Mapping them from `soi.tsv`, XBRL and HTML tables is this ticket's. A BDC is a `fund` recognized by its `814-` file number.
- **From "Owner kind: storage, evidence and the PE-firm test"** (2026-11-07; ADR 0001 amended; table in evidence_layer_plan.md §4 `owner_kind_evidence`): each BDC gets a rank-1 `owner_kind_evidence` row for `other_investment_fund` from its `814-` number; its ticker doesn't make it `public_company`.
- **From "Funds and their investment firm"** (2026-11-07; ADR 0001 amended; notes in evidence_layer_plan.md §4): a BDC links to its adviser by `managed_by` (fund → investment_firm), from its 10-K ("externally managed by Ares Capital Management LLC"); which producer reads it is this ticket's. A BDC keeps `other_investment_fund` from its `814-` number even when its manager is a private equity firm (BCRED under Blackstone).
- **From "Document storage, fetch log and last-confirmed"** (2026-11-07; notes in evidence_layer_plan.md §4 `documents` and `fetches`): a 10-Q or 10-K is a parent document; each Schedule row the parser reads is a child document whose `raw_text` is the row's parsed-table text, with `parent_document_id`. A DERA data-set row is a child of the data-set file. Children inherit the parent's `published_on` (the filing date).
- **From "Edge lifecycle: ending, retraction and staleness"** (2026-11-07; notes in evidence_layer_plan.md §4 `edges`): a `lends_to` or `holds_position` edge ends (`absent_from_list`) when the fund's next Schedule parses cleanly and lacks the holding, as of that Schedule's period end, with that filing as `ended_by_document_id`; one miss is enough; an unparseable Schedule proves nothing. So the parser must report whether a Schedule parsed cleanly as a whole.
- **From "EDGAR full-text search and ownership filings"** (2026-11-08; section in evidence_layer_plan.md): full-text search leaves BDC filings out; BDC 10-Qs and 10-Ks stay with the BDC parser.

## Answer

Resolved 2026-11-16 in a grilling session (three rounds and a glossary question, recorded under Comments). Facts: [bdc-filing-facts](../research/bdc-filing-facts.md).

- **Lender and borrower:** the lender is the BDC, a `fund`; its adviser connects only through `managed_by`. The borrower is the company the row names, never the PE firm: brand → company ← lends_to ← BDC → managed_by → investment firm.
- **Universe:** every `814-` filer of 10-Ks or 10-Qs, listed, non-traded or private (about 187), found monthly from the SEC BDC data sets and BDC Report and confirmed in submissions JSON; an `etl` producer emits `fund` identity records (`cik`, `sec_file_number`) and rank-1 `other_investment_fund` evidence.
- **Filings:** every 10-K and 10-Q, amendments only with a tagged Schedule; every tagged Schedule since the BDC began tagging (about 2,400 filings); a daily submissions check finds new ones. Pre-tagging history and untagged EX-99 venture schedules go to the map's Not yet specified.
- **Parser** (`parser` producer, module `bdc_soi`): reads the filing's own Inline XBRL; one row per holding; values from the row's tags; each row a child document whose text is the visible row with blank name cells copied down; the hidden identifier is never quoted or used as a name. The SEC data set is not a source.
- **Claims:** `lends_to` for loans, `holds_position` for equity; a control-section equity row also gives `owned_by` (voting basis, no stake), which ends on a clean miss or `fund_closed` (ADR 0001 amended). Name as written: name cell minus footnote markers and tranche words; two suffixed names split into two claims; a trailing f/k/a gives `renamed_from`, and dba, aka or bare parentheses go to the new value field `other_name`, never an ownership claim.
- **Edges:** one `lends_to` and one `holds_position` edge per pair; new `edges.value_document_id` (the newest Schedule's filing) carries every tranche; new end reason `fund_closed` (N-54C or Form 15).
- **Joint ventures:** a venture schedule tagged inside the 10-Q is read with the venture as lender (a `fund` identity record), and the BDC's stake row gives `holds_position` (BDC → venture).
- **Adviser:** the LLM reads each 10-K's Item 1 Business section, once per 10-K; nothing else in BDC filings.
- **Outcomes per Schedule:** clean (claims publish, missing pairs end edges), partial (claims publish, nothing ends, alert), failed (nothing publishes, `unreadable`, alert); ADR 0002 amended.
- **Cross-check:** against the SEC's monthly BDC data set, in build tests and as a production alert that never changes claims; CLAUDE.md definition of done item 3 reworded.
- **Layouts:** generic rules plus per-filer overrides in code, each with a real fixture; no hand step in production.
- **Glossary:** new entries BDC and Schedule of Investments.
- **Docs changed:** evidence_layer_plan.md (§4 `claims` values, `edges`, §5 "BDC connector and Schedule parser", remnant notes), ADR 0001 and 0002, CLAUDE.md, GLOSSARY.md, build_roadmap Steps 20 to 22, research_flows B1b, pre-launch-seeding, the bdc-parser skill (rewritten XBRL-first).

Handed on:
- "Entity resolution": holding-company and acquisition-vehicle borrower names, `other_name`, venture names, spelling variants between BDCs.
- "Citation verification rules": quoting code-rendered row text; numbers checked against the tags.
- "Fan-out and refresh": daily submissions check, monthly universe job, monthly data-set comparison.
- "Celery topology": the SEC's 10 requests a second shared with full-text search and Form ADV; large parse tasks.
- "API conventions and operator surface": partial, failed and cross-check alerts.
- "Operational identity and guardrails": the failure-rate threshold value.
- "Testing and acceptance": BDC fixtures and the data-set match bar.
- "Graph endpoint and non-brand output shapes": BDC and venture pages.
- chains "BDC lenders on brand pages" (fog): `other_name` links, whether a brand's "checked" needs BDC Schedules.
- Corrections recorded here: "Conflict, succession and co-investors" ("each BDC holding is its own edge" means a pair); "Claim value schemas" (a BDC edge's value is all claims from the newest Schedule).

## Comments

### 2026-11-15/16 grilling session

Facts gathered for this session: [bdc-filing-facts](../research/bdc-filing-facts.md) (three parsed 10-Qs: Ares Capital, PennantPark Floating Rate, Blackstone Private Credit Fund; adviser sentences; data-set lag; sizes; joint-venture exhibits; consumer-brand borrowers in the SEC data set).

Kept whole, not split: the data source decides both discovery and the quote form, and the ticket comes to about 14 questions.

**Round 1** (all six accepted as recommended, Q4 as revised):

- Q1 Who lends to whom: the lender is the BDC itself, a `fund` entity; its adviser connects only through `managed_by`. The borrower is the company the row names, as written, never the PE firm. The "sponsor ← lends_to ← BDC" diagrams (build_roadmap Step 22, pre-launch-seeding) are wrong; the chain reads brand → company ← lends_to ← BDC → managed_by → investment firm.
- Q2 Universe: every entity with an `814-` file number that files a 10-K or 10-Q, listed, non-traded or private (about 187). A monthly job takes the union of the SEC BDC data-set CIKs and the yearly BDC Report and confirms each by an `814-` file number on a 10-K or 10-Q in its submissions JSON. Each BDC becomes a `fund` entity through identity records from an `etl` producer (`cik`, `sec_file_number`) plus its rank-1 `owner_kind_evidence` row for `other_investment_fund`.
- Q3 Filings: every 10-K and 10-Q; an amendment is parsed only when it carries a tagged Schedule, and then it is a later-filed document for the same period (wins a same-date tie). No N-2s or prospectuses.
- Q4 History (revised after the developer asked whether only records from 2022 on are tracked; answered: only for BDC loan data, ownership evidence keeps its own depth; a loan made before 2022 that still exists shows, often with the filer's printed acquisition date; a loan that started and ended before tagging never shows): load every tagged Schedule since each BDC began tagging (August 2022 to May 2023 by BDC; about 2,400 filings, 1 to 2 GB to download compressed, 24 to 31 GB uncompressed). Pre-tagging history goes to the map's Not yet specified, to revisit once BDC data is live.
- Q5 Tranches and edges: each row is its own claim; one `lends_to` edge per BDC and borrower pair and one `holds_position` edge per BDC and company pair; the edge's current value is every row from the newest Schedule naming the pair; the edge ends only when a clean Schedule has no row for the pair. Corrects "Conflict, succession and co-investors" ("each BDC holding is its own edge" means a pair) and "Claim value schemas" (for BDC edges the value is all claims from the newest Schedule).
- Q6 Control investments: each equity row under "Control investments" (over 25% of voting securities or control of management, 1940 Act) also gives an `owned_by` claim (company owned_by BDC) with `stake_basis: voting` and no `stake_pct`; it self-verifies (official filing) and ends when a clean Schedule no longer lists the control holding, a fourth way for a hop to end (ADR 0001 to amend). Affiliate and non-affiliate rows give `holds_position` only. Control status is not tagged per holding: the parser reads it from section headings or footnote markers, per filer.

**Round 2** (all four accepted as recommended, Q8 as revised):

- Q7 Row values and quotes: parse each filing's own tagged (Inline XBRL) document. One table row is one holding; values come from that row's tags with their scale; the name comes from the visible row. Each row becomes a child document whose text is the row's visible cells in order, with name and description cells copied down from the borrower's first row where the filer left them blank (Ares Capital style), rendered by code like store-locator records; the claim quotes that whole text; the parent keeps the original filing. The hidden identifier only groups a row's tags, never quoted or used as a name (it sometimes names another company). The SEC BDC data set (`soi.tsv`, 5 to 35 days late, shifting columns) is not a source.
- Q8 Joint ventures (revised after the developer asked whether skipping them misses connections; measured in the August 2026 data set: about 670 borrowers in three tagged venture schedules, about 97 of them in no BDC's own Schedule, e.g. American Greetings, CWGS Group; Claude corrected its "simpler parser" reason, since the parser must recognize venture rows either way): a venture schedule tagged inside the BDC's 10-Q is read with the venture as the lender. The venture becomes a `fund` entity through an identity record; its rows give `lends_to` (venture → borrower); the BDC's own stake row gives `holds_position` (BDC → venture). Untagged EX-99 venture schedules (five vehicles) are skipped and go to Not yet specified.
- Q9 Adviser: the LLM (approved prompt) reads each 10-K's Item 1 Business section, cut out by code as its own child document, once per 10-K (about 187 a year); internally managed BDCs give no claim; an adviser and sub-adviser of one firm resolve to one firm entity; a third-party sub-adviser shows `sources_disagree` under the one-manager rule. The LLM reads nothing else in BDC filings. Whether p9 catches defined-terms wording (PennantPark) is checked in the build.
- Q10 New filings and closed BDCs: a daily check of each BDC's submissions JSON (about 187 requests); a new 10-K, 10-Q or amendment with a tagged Schedule is fetched and parsed the same day ("Fan-out and refresh" schedules it). An N-54C or Form 15 ends all the BDC's open `lends_to`, `holds_position` and control `owned_by` edges as of its last Schedule's period end, with new end reason `fund_closed`.

**Round 3** (all six accepted as recommended; name counts measured on the August 2026 SEC data set, counting each tranche's name string):

- Q11 Name as written: the name cell after the copy-down, with footnote markers ("(13)", "(4)(10)") and appended tranche words ("- Funded Revolver") removed; spelling, punctuation and entity suffixes kept. Two names joined by "and" or "&", each ending in an entity suffix, give one claim per company with the same quote (about 490 strings); "Wash & Wax Systems, LLC" stays whole.
- Q12 Parentheses: a parenthesis at the end of the name cell comes off the name (one inside a name, "Activate Holdings (US) Corp.", stays). f/k/a or fka (about 600 strings) gives a `renamed_from` claim with `former_name`. dba, aka and bare parentheses (about 2,300 dba strings; aka runs both ways) give no claim; their text as written ("dba Dental365") goes into a new optional value field `other_name` on `lends_to` and `holds_position`. Not an ownership claim, because a franchisee also writes "dba <brand>" and a licensee never owns the brand. How `other_name` links a loan to a brand page goes to the chains map's "BDC lenders on brand pages" fog.
- Q13 Layouts: generic rules first (blank name copies down; trailing "(n)" is a footnote; a heading or footnote matching a fixed phrase list sets affiliation); per-filer overrides in code only where those fail, each with a real fixture from that filer added first. A BDC the rules can't read gets a partial or failed parse and an alert; Claude adds the override as an ordinary code change for the developer to commit. No hand step in production.
- Q14 Outcomes per Schedule (the BDC's own and each venture's): clean (no failed rows, fair values add up to the tagged total within the filer's rounding): claims publish and missing pairs end their edges; partial (failed rows at or below the threshold, or totals off): claims publish, no edge ends from it, alert; failed (above the threshold): nothing publishes, the read is `unreadable`, alert. A row fails when its shown numbers differ from its tags after scaling, it has no name after the copy-down, or the door rejects its claim. Threshold value: "Operational identity and guardrails".
- Q15 Cross-check: the SEC's monthly BDC data set is the independent copy. Build tests match each fixture filing's holdings to the data set's rows (count, fair value per holding, by identifier; bar in "Testing and acceptance"); in production each monthly file is compared with that month's parsed filings and any difference raises an alert, never changing or withholding claims.
- Q16 Edge value: new nullable `edges.value_document_id`, set for `lends_to` and `holds_position` edges to the newest Schedule's filing; `value_claim_id` stays null on them; the card reads that filing's claims for the pair. Ownership edges keep `value_claim_id`.

**Round 4** (accepted): Q17 glossary entries BDC and Schedule of Investments added; the developer confirmed the summary of derived details (producers, row keys, scale mapping, venture names), doc changes and hand-offs.
