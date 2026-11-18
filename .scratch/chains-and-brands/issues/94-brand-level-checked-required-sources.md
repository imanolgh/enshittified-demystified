# Brand-level checked: required sources and freshness

Type: grilling
Status: open
Blocked by: engine/37  (Retrieval fan-out, tracked entities and refresh cadence)
Map: [chains-and-brands](../map.md)

## Question

Which sources are on a chains-and-brands brand's required list, so that it counts as checked once all of them have finished a run, and how long does a check stay fresh before it must run again?

## Context

- Split off "Category brand lists and checked" on 2026-11-17 (round 1 Q0), because the required list can't settle until engine "Retrieval fan-out, tracked entities and refresh cadence" decides which connectors run for a brand, including the historical press route (after "Research: Web search APIs for finding a brand's past coverage" and "Task: Test search API coverage of older deals").
- Engine side, settled in "What 'checked' means and coverage states" (2026-11-07; ADR 0001 amended): each product names a required source list per entity type; a brand is checked when every required source has finished a run (finding nothing counts); a failed or robots-blocked source leaves it unchecked and on the operator report; the checked date is the oldest required run's; shared sources (sponsor portfolio pages, press feeds, Form ADV, BDC Schedules) count through their latest complete pass after the brand was added; a check is judged against the list in force when it ran. Every launch brand must be checked.
- Candidates: SEC filings and EDGAR full-text search per brand (engine "EDGAR full-text search and ownership filings"), press (wire feeds going forward plus the historical route; engine "Press and EDGAR full-text connectors"), the registry's sponsor portfolio pages, newsrooms and about pages (engine "Rosters, portfolio pages and the registry"), Form ADV (engine "Form ADV and IRS exempt-org ingestion"), BDC Schedules (engine "BDC discovery and Schedule of Investments parsing"; whether a brand counts as checked only after their latest complete pass is open in the map's fog). USPTO is not a v1 source ("USPTO trademark data: adopt as a source?").
- From the 2026-11-16 and 2026-11-17 research: sites that block the bot leave required sources unfinished (every Nestlé Purina site; New Balance; Mary Kay; WinCo's robots.txt disallows ClaudeBot), so this ticket also needs what a brand shows when a required source can never finish.
- 37 launch industries, about 1,100 brands at 30 per list ("Launch industries", amended).
