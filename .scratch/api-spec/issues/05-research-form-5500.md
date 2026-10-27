# Research: Form 5500 bulk data contents

Type: research
Status: resolved
Map: [api-spec](../map.md)

## Question

What does the DOL/EFAST Form 5500 bulk data actually contain, and can a plan's fund-by-fund lineup be built from it?

## Why it matters

Scenario B1a (research_flows.md:123–126; evidence_layer_plan.md:219) assumes the bulk CSVs list each 401(k) plan's fund lineup, producing `allocates_to` claims and the free headline exposure number (pre-launch-seeding.md:71). The gap analysis flagged this as **high risk**: structured data may carry only Schedule H aggregate line items and Schedule D names of collective trusts/pooled accounts, while the fund-by-fund schedule of assets is a PDF attachment.

## Find out

- Datasets published (Form 5500, 5500-SF, Schedules H, I, D, C, R…), download URLs, formats, years available, update cadence, file sizes.
- Exactly which fields could identify funds/investments held; whether the schedule of assets held (line 4i) is structured or attachment-only.
- 5500-SF small-plan filers (no Schedule H); DC-plan filter codes (plan type/feature codes); amendments; the EIN+PN plan key; employer (sponsor) identification fields.
- Anything resembling a "sponsor index" for employer → plan lookup (research_flows.md:146).


## How to resolve

AFK. A subagent invokes the `research` skill and writes findings, every claim cited to its primary source, to `.scratch/api-spec/research/form-5500.md`. No branches, commits or pushes (map scope ruling 2026-10-26). Then append `## Answer` here: a short summary + link to the findings file.

## Answer

- **No fund-by-fund lineup in the structured data.** The Schedule H line 4i "Schedule of Assets (Held At End of Year)" is a filer-prepared attachment (PDF or TXT). The CSVs carry only the Yes/No flag `AST_HELD_INVST_IND`.
- Large plans: Schedule H gives **aggregate dollar totals by asset class**. Mutual funds are one line, `INT_REG_INVST_CO_*`. Schedule D Part I **names each CCT/PSA/MTIA/103-12 IE** the plan invested in, with the vehicle's EIN/PN and the plan's year-end dollar value. Mutual funds are never on Schedule D.
- Small plans (5500-SF; Schedule I): totals only, no asset-class detail and no Schedule D.
- Datasets: zipped CSVs per form year, 1999–2025, at `askebsa.dol.gov/FOIA Files/{YEAR}/{Latest|All}/`, refreshed about monthly. "Latest" = the newest `FILING_RECEIVED` filing per plan. Join on `ACK_ID` (one submission). 2024 sizes: F_5500 28.6 MB, 5500-SF 136 MB, Sch H 15 MB zipped.
- Plan key = sponsor EIN + 3-digit PN (permanent, never reused). DC filter = plan-characteristic codes in `TYPE_PENSION_BNFT_CODE` (2J = 401(k), etc.) plus `SF_401K_PLAN_IND`. Amendments fully replace the earlier filing.
- No DOL "sponsor index" file. It can be built from F_5500/F_5500_SF sponsor name/DBA/EIN/address/`BUSINESS_CODE` → EIN+PN. The only route to line-4i attachments is EFAST2 Filing Search, one filing at a time. No bulk download or API for attachments was found, and attachments post up to 21 days after the structured data.
- Open: EFAST2 attachment fetch mechanics (search guide returned 403), attachment PDF quality, and the exact format of the plan-code field.

[findings](../research/form-5500.md)
