# Task: Draft prompt p10 and run the approval check

Type: task
Status: open
Blocked by: none
Map: [engine](../map.md)

## Question

Does prompt p10, which adds licensing evidence to p9, pass the approval bars?

## Context

- Created 2026-11-18 from chains "Licensed names in v1" (Q6). p9 is the approved production prompt ("Task: Draft prompt p9 and run the approval check"; rules in "Extraction prompt rules").
- p10 adds: `licensed_to` (brand → company) for a licensee's statement that it makes or sells under the brand's name by license, including "used under license" on the licensee's own page; and `basis` on brand-subject owner claims: `listing` when the brand only appears on a brands or portfolio page, `license_grant` when the owner says it licenses the name out ("Predicate semantics", "Claim value schemas", amended 2026-11-18).
- Bars: the p9 bars from "Extraction prompt rules", plus targeted documents counted by script: Meyer's brands page (KitchenAid, Rachael Ray, Farberware as `listing`), Whirlpool's 10-K licensing sentence (`license_grant` for KitchenAid), Lifetime Brands' 10-K license sentence (`licensed_to` Farberware → Lifetime), a "used under license" page, and Dunkin's trademark footer (no basis).
- Claude drafts p10; the developer approves it (CLAUDE.md). Runs on DeepSeek's own API, off-peak, with costs logged.
- **From "Task: Estimate build, seeding and monthly running costs"** (2026-11-20): if p10 or any later version ships after the seeding pass, the whole corpus is re-read for another $850 to $7,700, so seeding after the prompt is final avoids paying twice.
- **From "Cost cuts before revenue"** (2026-11-21): seeding waits until p10 is approved, and later versions no longer re-read the corpus automatically ("Extraction execution" Q7, amended).
