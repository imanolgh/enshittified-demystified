# The private equity firm test and asset managers

Type: grilling
Status: resolved
Map: [engine](../map.md)

## Question

What rule decides that an investment firm is a private equity firm, so that asset managers that run a few private equity funds among many others (BlackRock, State Street, Fidelity, J.P. Morgan, T. Rowe Price) are not classed as private equity firms, while firms whose main business is private equity, including diversified ones (Blackstone, KKR, Apollo, Carlyle), still are?

## Context

- Opened 2026-11-20 at the developer's request (ticket 37 round 2, Q16), after the developer asked why BlackRock, State Street and Fidelity are classed as private equity firms when they aren't. This is v1 correctness work, not part of the parked [Asset Managers map](../../asset-managers/map.md).
- **The rule today** ("Owner kind", 2026-11-07; amended by "Funds and their investment firm"; evidence_layer_plan.md §4 `owner_kind_evidence`; ADR 0001 amended): Form ADV is rank-1 evidence for `private_equity`, from `Any PE Funds = Y` or the monthly counts by fund type, where "any PE fund → private_equity; all real estate or all VC → that kind; any other mix → other_investment_fund", and "Y on any of a firm's registrations counts". It was chosen to catch firms that run buyout funds without calling themselves private equity (Trian, 3G, BDT, JAB).
- **The misfire** (chains "Research: Full category audit", 2026-11-07; "Category precedence and storage" context): read literally, the rule also flags index and asset managers. BlackRock reports 125 PE funds, and J.P. Morgan, FMR, State Street and T. Rowe Price also report Y.
- **What was patched, and what wasn't.** "Category precedence and storage" (Q5) ruled that a 13G filed under Rule 13d-1(b) never counts toward PE minority stake. That stops the most common symptom, but the firms are still classed `private_equity`, so:
  - **Inherited kinds:** a fund with no type of its own takes its firm's kind ("Funds and their investment firm"; Form ADV connector: post-2024 IAPD funds "take the firm's kind"). Every BlackRock fund read from its IAPD PDF, credit, hedge and infrastructure funds included, is private equity by inheritance, and a brand controlled by one reads PE-owned.
  - **Other filings:** a 13D, or a 13G under (c) or (d), from one of these firms counts as PE minority stake.
  - **Labels:** wherever the product labels the owner, it says private equity firm.
- **Options raised in ticket 37** (no decision):
  - (a) fund-mix test from Form ADV counts already loaded (PE the largest group, or at least a set share, of the adviser's private funds), with the risk that diversified alternative managers fall below the line;
  - (b) main-business test (advisers whose main clients are mutual funds and ETFs are asset managers), if Form ADV data carries client types;
  - (c) a named list in code, which is a person deciding a classification and so needs ADR 0002 amended.
- **Starting facts:** a background check started 2026-11-20 gathers each firm's private funds by type and client types from the SEC's monthly Form ADV files, for 12 asset managers and 12 PE firms, and which simple lines separate them. Findings: [research/adv-fund-type-mix.md](../research/adv-fund-type-mix.md).
- **Related:** ticket 37 Q14 tracks a named operator list of asset managers (BlackRock, Vanguard, State Street) from launch. Tracking is not a classification, so that list decides nothing here. The chains card line for large shareholders ("Large shareholders of public owners on the card") waits on this ticket for how holders are labeled. Showing index managers apart from buyout firms beyond v1 is on the Asset Managers map.
- **On resolution, update:** ADR 0001 (the PE-firm test), evidence_layer_plan.md §4 `owner_kind_evidence` rank-1 rows, the glossary entries "Owner kind" and "Investment firm" if the vocabulary changes, and the Form ADV connector notes.
- **Starting facts, gathered 2026-11-20** ([research/adv-fund-type-mix.md](../research/adv-fund-type-mix.md); SEC November 2026 files `ia110226-registered.zip` and `ia11022026-exempt.zip`):
  - **The current rule** flags 10 of the 12 asset managers checked (all but Vanguard and Northern Trust) and all 12 PE firms.
  - **No fund-count line separates the two groups.** PE share of private funds: BlackRock 42.2% (294 of 697), Blackstone 39.1%, Apollo 30.0%, Bain Capital 26.3%, Ares 21.9%; KKR 79.7%; Leonard Green, Warburg Pincus and Roark 100%. Assets by fund type are in neither file.
  - **Investment-company share of regulatory AUM** (Item 5.D, registered file only) is the one measure where the ranges don't overlap. Asset managers run 20% to 97% (Vanguard 97.3%, State Street 96.3%, Fidelity 93.1%; J.P. Morgan AM 41.1%, Wellington 40.9%, Goldman Sachs AM 23.0%, Northern Trust 20.3%). PE firms run 0% to about 3% (KKR 0.5% to 3.2% depending on which registrations count; Apollo 2.3%).
  - **Caveats:** exempt reporting advisers file no Item 5 data, so a firm registered only as one can't be tested this way. RAUM is double-counted across affiliated registrations through subadvice. Affiliates with other names (HPS and GIP under BlackRock, Oaktree under Brookfield, 50 South under Northern Trust) were grouped from general knowledge, not from the file. Which Item 5.D lines count as investment companies (and whether BDCs do) should be checked against the form.
  - **Vanguard reports no private funds** in any of its 7 registrations, so the Form ADV load (advisers with private funds only) never creates it. Tracking it from the operator list (ticket 37 Q14) needs its entity created another way, by CRD from the list or from a 13G claim.

## Comments

**2026-11-20, before round 1:** testing a 10% registered-fund share line against the whole November file (not just the 24 sample firms) flipped 80 advisers that report PE funds, real PE firms among them: Partners Group (USA) 56.8%, Lexington 49.5%, Ardian 35.3%, Pomona 12.7%. They sell PE to retail investors through registered funds. By size, no PE firm passes about $18bn in registered funds (Apollo $17.8bn, Partners Group $16.5bn, Blackstone $16bn, Carlyle $11.6bn, KKR $6bn). Mid-size managers sit between (WCM $34bn, Barrow Hanley $21bn, GMO $19bn), and the big managers run hundreds of billions to trillions.

**Round 1 (developer: yes to all):**
- Q1: the test is size: $50bn in registered investment companies (Item 5.D(d), BDCs excluded) makes an asset manager. Turned down: $25bn (1.4 times headroom over Apollo), a 10% share line (misclasses Partners Group, Ardian, Lexington, Pomona), a named list (ADR 0002).
- Q2: new kind `asset_manager` and category `asset_manager_owned`, with the investment-fund kinds in precedence; glossary "Asset manager" added and the term taken off Investment firm's avoid list.
- Q3: summed over the firm's registrations (ADR 0001's grouping). Firms under their own names (Lexington, HPS, GIP) are tested alone.
- Q4: a fund's own evidence first; otherwise it inherits the firm's kind.
- Q5: the Form ADV load adds advisers at or above the line. Counted after the round: 105 registrations, 48 without private funds (Vanguard ×3, BlackRock Fund Advisors, Capital Research, Geode, Schwab, Mellon, Federated, MFS, insurers' fund advisers), not "a few dozen" as first estimated.

**Round 2 (developer: yes to all):**
- Q6: the size test is the kind's only source (rank 1) and overrides "any PE fund". Self-descriptions never set it; "asset manager" and "alternative asset manager" are unclear terms.
- Q7: a post-2024 Goldman (or J.P. Morgan) PE fund reads PE-owned once a release or page describes it as a private equity fund, else asset-manager-owned by inheritance.
- Q8: a buffer: an asset manager from $50bn, back below $40bn; operator alert when a firm classed private equity passes $25bn.
- Q9: the card label for `asset_manager_owned` goes to chains 121.

## Answer

Resolved 2026-11-20 in a grilling session (two rounds, above). Recorded in ADR 0001 (amended: kinds list, the PE-firm rule, precedence, categories), evidence_layer_plan.md (§4 `owner_kind_evidence`, the Form ADV connector's load, the card note on 13d-1(b) holders) and the glossary ("Asset manager", "Owner kind", "Investment firm").

- **Rule:** a firm with $50bn or more in registered investment companies (Form ADV Item 5.D(d)(3), summed over its registrations; BDCs excluded) is an **asset manager**, however many PE funds it reports. It stays one until those assets fall below $40bn. Every other firm keeps "any PE fund → private equity".
- **Why size:** fund-count shares overlap (BlackRock 42% PE, Blackstone 39%, Ares 22%). Registered-fund share catches PE firms with retail funds. Size leaves a wide gap: PE firms top out near $18bn, and the asset managers checked run $296bn and up.
- **Vocabulary:** owner kind `asset_manager`, category `asset_manager_owned`, placed after other investment funds in precedence. The size test, rank 1, is the kind's only source and overrides "any PE fund". "Asset manager" and "alternative asset manager" map to no kind.
- **Funds:** a fund's own evidence first; otherwise it inherits `asset_manager`. This can miss PE in an asset manager's own PE deals until something describes the fund, but it never wrongly claims PE.
- **Loading:** advisers at or above the line come into the Form ADV load (48 more in November 2026, Vanguard among them).
- **Unchanged:** a 13d-1(b) filing never counts; exempt reporting advisers never qualify.

Handed on:
- chains [121](../../chains-and-brands/issues/121-large-shareholders-of-public-owners-on-the-card.md): the card label and one-line explanation for `asset_manager_owned`, and how asset managers are named among large shareholders.
- "Operational identity, budgets and guardrail values": the $25bn alert, and the $50bn and $40bn lines as code values.
- "Events and the public changelog": owner-kind changes from this rule (the buffer keeps them rare).
- [Asset Managers map](../../asset-managers/map.md): the kind now exists in v1. Firm pages, 13F and N-PORT stay parked.

