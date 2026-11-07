# Owner kind: storage, evidence and the PE-firm test

Type: grilling
Status: resolved
Blocked by: 07, 12  (Research: Form ADV and IRS exempt-org bulk data; What a business entity is)
Map: [engine](../map.md)

## Question

Where does an entity's owner kind live, how is it evidenced and ranked, who maps a quoted self-description onto the enum, what test makes an investment firm a PE firm, and what is a BDC's owner kind?

## Context

- ADR 0001:5,9,14 makes owner kind a sourced, ranked fact with a confidence (a category is verified only if the deciding owner kind is verified). The 7-predicate set (CLAUDE.md:30) can't express it; §4 has no column (evidence_layer_plan.md:88 is a comment only). Options: `entities.owner_kind` + an assertions table, or a new claim type (vocabulary decision).
- **Self-description → enum**: ADR 0001:9 / evidence_layer_plan.md:177 have the LLM extract the quote, but mapping "growth equity", "family office", "holding company" onto 9 kinds is classification. LLM emits enum + quote, or code applies a phrase table?
- **`pe_firm` definition vs ranks**: ADR 0001:10 defines it via Form ADV; ADR 0001:9 / evidence_layer_plan.md:177 let a rank-2/3 self-description set it.
- ADR 0003:13 says a source type joins only when a relationship takes evidence from it, yet `form_adv` and `irs_exempt_org` exist only for owner kind.
- **Field evidence** (added 2026-11-04): the category audit pilot found that `Any PE Funds` flags Trian, 3G, BDT and JAB as PE and misses L Catterton's main US adviser ([chains-and-brands/research/category-audit-pilot.md](../../chains-and-brands/research/category-audit-pilot.md) §5).
- Form ADV and IRS exempt-org are in scope (map ruling 2026-10-26); facts from "Research: Form ADV and IRS exempt-org bulk data".
- **From "What a business entity is"** (2026-11-05, [ADR 0005](../../../docs/adr/0005-brands-companies-locations-separate.md)): owners now include a `family` entity (one person or a family owning in their own name; owner kind `family`). Trusts, ESOP trusts, nonprofits and government bodies are `company` rows carrying owner kind `trust`, `employee_owned`, `nonprofit` or `government`.
- **From "Claim producers and the claims door"** (2026-11-05; summary in evidence_layer_plan.md "Producers and the door"): Form ADV is an `etl` producer that emits identity records for advisers (CRD, SEC number, legal name, office address). If owner-kind evidence such as `Any PE Funds` is its own output rather than a claim, it rides in the same door call; its shape and storage are this ticket's.
- **From "Entity lifecycle"** (2026-11-06; notes in evidence_layer_plan.md §4 `entities`): code may change an entity's type from `company` to `investment_firm` or `fund` when a Form ADV identity record matches it (events row). A firm first created from a news quote as a company becomes an investment firm that way.
- **From "Claim identity"** (2026-11-06; notes in evidence_layer_plan.md §4 `claims`): a claim-created owner is a `company`, or a `family` when the LLM marks the name as a person or family ("the Cathy family"). A firm not in Form ADV (a family office, a foreign firm) stays a `company`, so owner kind for it comes only from this ticket's other evidence.
- **From "ExtractedClaim and the extraction result envelope"** (2026-11-06): the LLM response is only `claims: list[ExtractedClaim]`. If this ticket makes quoted owner self-descriptions ("a private equity firm") an LLM output, the envelope gains a second list for them, shaped here.
- **From "Claim value schemas"** (2026-11-06; schemas in evidence_layer_plan.md §4 `claims`): a BDC is a `fund` entity (recognized by its `814-` file number); its owner kind (a public BDC with a ticker, an externally managed BDC whose adviser files Form ADV) is this ticket's.
- **Split 2026-11-06** (developer ruling, before round 1): the fund–firm link and where a PE chain ends moved to "Funds and their investment firm"; whether a public company a PE fund controls (Jersey Mike's) or with a PE-fund 5%+ holder reads PE-owned or PE minority stake moved to "Category precedence and storage".

## Comments

### Round 1 (2026-11-07)

Facts read: the audit's Form ADV check (every control owner in a PE-owned row has an adviser with `Any PE Funds = Y` except L Catterton, whose main US adviser CRD 157428 reports N while its Europe and Asia advisers report Y; Trian, 3G, BDT and a JAB manager report Y without calling themselves PE).

- **Storage** (Q1, option a): an `owner_kind_evidence` table (entity, kind, rank, document, quote, producer and version, status, `retracted_at`); rows enter through the door and their quotes pass `verify_citations`. Code computes each entity's owner kind (higher rank wins; a same-rank contradiction → "owner type not confirmed") and stores it on `entities.owner_kind`, recomputed when evidence changes.
- **Self-descriptions** (Q2, revised twice after the developer asked how terms get added and whether Jev could classify): the envelope gains `owner_descriptions` (owner's name as written, describing phrase as written, document label, quote). Every description is stored with a state: mapped, listed as unclear, or unknown; the phrase and quote never change, and the kind is code's current answer from a term table in code, recomputed when the table changes (an entity whose owner kind changes gets an events row). Matching: the table's terms inside the phrase, case-insensitive, longest term wins ("private equity-backed" is listed with no kind so it never reads as "private equity"); a negation or terms for two kinds give no evidence. New terms: the operator report lists unknown phrases by how many owners use them, with example quotes and a model-suggested kind (Claude, which the pipeline already calls; Jev only if adopted later) that never counts as evidence; the developer decides, Claude adds a general term (never a firm name) with a test, and stored descriptions are re-mapped with no new LLM calls. Jev as the mapper was turned down: a classifier can't be the source of a published fact (evidence_layer_plan.md), and Jev is out of scope for this map. Starting terms: Form ADV fund types, the glossary, the audit pilot's quotes, and a pre-launch pass over seeded owners' sites; a coverage bar goes to "Testing and acceptance".
- **PE-firm test** (Q3, option a): `Any PE Funds = Y` is rank-1 evidence for `pe_firm` (verified), Trian, 3G, BDT and JAB included (their own filing; card wording: "Card wording and the how-this-works page"). `N` is not evidence of anything (an affiliate may report the funds). A self-description mapping to `pe_firm` sets it as `reported` (L Catterton). ADR 0001's "PE firm vs other funds" rule amended.
- **Rank-1 sources** (Q4): `pe_firm` Form ADV `Y`; `public_company` a ticker from an SEC filing; `nonprofit` IRS EO BMF; `employee_owned` Form 5500 ESOP (parked); `family` needs none for a `family` entity; `other_investment_fund`, `conglomerate`, `trust`, `government` have none (self-description only). A public conglomerate reads `public_company` (ticker beats description).
- **BDC** (Q5): owner kind `other_investment_fund`, from its `814-` number (rank 1); its ticker doesn't count. The glossary's "other investment fund" widens to include credit funds. Whether a BDC can own: "BDC discovery and Schedule of Investments parsing".
- **Scope and time** (Q6): owner kind applies to companies, investment firms, funds, families and insurers, never brands or locations. Within one source, the newer document wins. ADR 0003's line about when a source type joins gains "or owner-kind evidence".

### Round 2 (2026-11-07)

- **Starting term table** (Q7): `pe_firm`: private equity firm/fund/investor/sponsor, buyout firm, growth equity firm/investor. `other_investment_fund`: venture capital firm/fund, hedge fund, activist investor, real estate investment firm, real estate fund, credit fund, private credit, direct lender, business development company. `public_company`: publicly traded, public company, listed on. `family`: family-owned, family owned, family business, family company. `employee_owned`: employee-owned, employee owned, ESOP. `nonprofit`: nonprofit, non-profit, not-for-profit. `conglomerate`: conglomerate. `trust`: family trust. `government`: government-owned, state-owned, sovereign wealth fund. Listed as unclear: private equity-backed, PE-backed, backed by, portfolio company, investment firm, investment company, asset manager, alternative asset manager, merchant bank, holding company, family office, privately held, private company, founder-led, independently owned, health system. Judgment calls: growth equity counts as PE (Form ADV files it so); "activist investor" is other investment fund (ADV `Y` still outranks it); "family office" stays unclear.
- **Gaps** (Q8, option a): `cooperative` owner kind and `cooperative_owned` category added (Ace Hardware, REI, Land O'Lakes, Ocean Spray), from self-descriptions ("cooperative", "co-op", "member-owned"); ADR 0001 amended, glossary updated. A pension fund maps to `other_investment_fund` (CDPQ co-owns New Look Vision Group), a sovereign wealth fund to `government`.
- **Rank 2** (Q9): a document on one of the owner's own `domain` identifiers, or a press release the owner issued (issuer: "Press and EDGAR full-text connectors"); everything else is rank 3 (Dunkin's site describing Roark is rank 3). Ranks 2 and 3 both publish as `reported`; the rank matters only when descriptions disagree.

## Answer

Resolved 2026-11-07 in a grilling session (two rounds, recorded under Comments). Split before round 1: the fund–firm link went to "Funds and their investment firm", and the public-company-with-PE-holder question to "Category precedence and storage".

- **Storage:** `owner_kind_evidence` rows (through the door, quotes verified); code computes `entities.owner_kind` and `owner_kind_confidence` (rank 1 verified, ranks 2–3 reported; a same-rank contradiction leaves "owner type not confirmed"). Only owners carry one.
- **PE-firm test** (ADR 0001 amended): Form ADV `Any PE Funds = Y` is rank 1 for `pe_firm` (Trian, 3G, BDT, JAB included); `N` is not evidence; a mapped self-description sets `pe_firm` as reported (L Catterton).
- **Self-descriptions:** the LLM returns `owner_descriptions` (name as written, phrase as written, label, quote); a term table in code maps phrases to kinds (terms inside the phrase, longest wins, negations and two-kind phrases give nothing). Every phrase is stored as mapped, unclear or unknown. Unknown phrases go to an operator report with a model-suggested kind that never counts; the developer decides and a general term is added with a test, then stored phrases are re-mapped with no new LLM calls.
- **Rank-1 sources:** Form ADV (`pe_firm`), a ticker from an SEC filing (`public_company`), the IRS exempt-org file (`nonprofit`), Form 5500 ESOP (parked); a `family` entity is family by definition. **Rank 2** = the owner's own domain or press release.
- **BDC** = `other_investment_fund` from its `814-` number; "other investment fund" now includes credit funds.
- **New kind:** `cooperative` (and `cooperative_owned`). Pension funds map to `other_investment_fund`, sovereign wealth funds to `government`.
- ADR 0003 amended ("or owner-kind evidence"); glossary "Owner kind" updated. No new ADR.

Handed on:
- "Funds and their investment firm": a fund's kind, and descriptions of funds.
- "Category precedence and storage": `cooperative_owned`, `owner_kind_confidence` in category confidence, PE holders in public companies.
- "Form ADV and IRS exempt-org ingestion": rank-1 rows.
- "Extraction execution": the prompt asks for owner descriptions.
- "Citation verification rules": description quotes.
- "Press and EDGAR full-text connectors": who issued a release.
- "BDC discovery…": 814- evidence rows.
- "API conventions and operator surface": the unknown-phrases report.
- "Testing and acceptance": the coverage bar.
- "Events and the public changelog": owner kind changed.
- chains "Card wording and the how-this-works page": ADV wording.
