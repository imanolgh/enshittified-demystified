# The private equity firm test and asset managers

Type: grilling
Status: open
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

