---
name: registry-research
description: Research and propose entries for the sponsor/DSO/rollup registry (pre-launch workstream W1) — finding consolidators per business category and their roster/portfolio URLs. Use when asked to find rollups, DSOs, consolidators, platform companies, or sponsor portfolio pages for a category (dental, vet, funeral, car wash, HVAC, dermatology, ABA, etc.).
---

# Sponsor & Rollup Registry Research

Goal: the master registry of ~300–500 sponsor/DSO/consolidator domains that powers national top-down seeding (pre-launch-seeding.md W1, decisions.md §11). This is research assistance: you find and document candidates; the developer approves every entry before it enters the registry.

## Entry format (one per candidate)
```
name:            # legal/brand name
category:        # dental | veterinary | funeral | carwash | hvac | derm | aba | ...
kind:            # pe_sponsor | dso_mso | consolidator_brand | platform_co
domain:
roster_url:      # the locations/portfolio page to crawl
parent:          # known PE sponsor(s), with source URL
evidence_urls:   # 1–3 links establishing the PE connection (press release, portfolio page, filing)
js_required:     # true/false (check the roster page)
est_locations:   # rough count from the roster
notes:           # naming quirks, sub-brands, roster format oddities
confidence:      # documented | reported | inferred  — never present inferred as documented
```

## How to research a category
1. Start from the developer-provided seeds and the project corpus (docs/painpoints.md names several: Heartland-class DSOs, TeamHealth/Envision, NVA/VCA-class vet groups, TSG-backed groups, SCI-class funeral consolidators).
2. Expand via: PE sponsor portfolio pages (crawl the portfolio listings of known healthcare/services sponsors), trade-press "top DSOs / largest consolidators" lists, acquisition press releases, and the sub-brand pages of platform companies.
3. For each candidate, verify the PE connection with at least one primary-source URL. No PitchBook/Preqin — public sources only.
4. Flag ownership-type nuance: family-owned consolidators and public-company chains are NOT PE — record them with the correct `kind` anyway (the taxonomy matters; misattribution is the failure mode this project exists to fix).

## Rules
- Batch output as a reviewable table or YAML block; never write directly into the production registry.
- Distinguish confidence levels honestly; an "inferred" parent with no citation is a lead, not an entry.
- Track coverage against the targets in pre-launch-seeding.md §7 (dental ≥30, vet ≥15, etc.) and report the running count per category.
- When a category is exhausted, say so — padding the registry with weak entries degrades the census match.
