# Research: Where PE owns consumer brands

Type: research
Status: claimed
Blocked by: none
Map: [chains-and-brands](../map.md)

## Question

Starting from what PE firms own rather than from a guessed list, which consumer-facing industries hold the most PE-owned brands, and which of them neither category audit nor the industry screen has measured?

## Context

- Added 2026-11-16 in "Product categories: vocabulary and assignment" (Q11). The developer asked how the screen's twelve industries were chosen; answer: Claude named them from general knowledge plus the developer's bowling example, so both candidate lists (the pivot proposal's thirteen and the screen's twelve) were guesses that were then measured. This ticket finds candidates bottom-up. The developer wants to run it right after "Product categories".
- Already measured: thirteen industries in [category-audit-pilot](../research/category-audit-pilot.md) and [category-audit-full](../research/category-audit-full.md), twelve in [industry-screen](../research/industry-screen.md).
- Estimated cost approved: roughly 1 to 2M tokens (not sized against real portfolios).

## Find out

1. **Portfolio pages:** the current portfolio pages of the PE firms with the most PE funds in the SEC's monthly Form ADV files, plus consumer-focused firms (Roark, Sycamore, L Catterton, TSG and similar), about 50 to 100 firms. Sort each consumer-facing portfolio company into an industry and count companies and brands per industry. Note rollups whose locations keep local names separately.
2. **BDC borrowers:** counts by the Industry Sector column of the latest SEC BDC data set (`soi.tsv`), as a cross-check of where PE-backed borrowers cluster.
3. **Screen anything new:** for each industry with several PE-owned consumer brands that isn't already measured, the top ~10 brands as in "Research: Industry screen".

## Rules

- Same rules as "Research: Industry screen": public primary sources only, trade press for rankings only, no PitchBook, Preqin, CB Insights or paywalled sources, competitor sites never sources, never fetch WhoIsMyDentist, Private Equity Vet or Reddit; robots.txt followed, SEC user agent `EvidenceEngine ownership-research bot (pe consumer scan)` with no email, at or under 2 per second; owner types are research notes, not engine classifications.
- Industry sorting here is a research note for a human decision, not the engine's industry assignment (which comes only from industry brand lists).
- Findings go to `.scratch/chains-and-brands/research/pe-consumer-scan.md`.

## Comments

### 2026-11-16 run

- **Firm selection.** Ranking advisers by PE fund count in the SEC's November 2026 adviser files (4,594 advisers report PE funds) is noisy at the top: SPV platforms (MicroAngel 833, EquityBee 581), fund-of-funds and secondaries managers (Hamilton Lane, StepStone, Adams Street, HarbourVest), wealth managers, venture and software firms, and infrastructure managers. Claude kept the buyout firms from that ranking and added consumer-focused firms and the firms the audits and the screen found owning consumer brands: 88 firms in four groups of 22.
- **Step 2 dropped.** In the August 2026 SEC BDC data set, the per-holding industry field (`Investment, Industry Sector [Extensible Enumeration]`) is filled on 4,483 of 143,266 holding rows (3%), and the Industry Sector Axis sits on subtotal rows, so a sector count of BDC borrowers isn't a useful cross-check without parsing the filings.
