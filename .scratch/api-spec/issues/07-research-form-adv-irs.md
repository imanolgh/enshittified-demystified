# Research: Form ADV and IRS exempt-org bulk data

Type: research
Status: resolved
Map: [api-spec](../map.md)

## Question

What do the SEC Form ADV bulk data and the IRS exempt-organization bulk data contain, and can they establish owner kinds at rank 1 (ADR 0001)?

## Find out

- Form ADV: bulk download (IAPD / SEC FOIA data), formats, cadence; Schedule D Section 7.B.(1) private fund reporting — the field giving fund type ("private equity fund", "venture capital fund", "hedge fund", "real estate fund", …); adviser identifiers (CRD, SEC file number); fund identifiers; whether it lists fund names usable for fund→adviser links; exempt reporting advisers.
- IRS: Exempt Organizations Business Master File (and/or Pub 78 / Form 990 data) — formats, fields (EIN, name, subsection code), cadence; how it identifies nonprofit owners.
- Licensing/terms.


## How to resolve

AFK. A subagent invokes the `research` skill and writes findings, every claim cited to its primary source, to `.scratch/api-spec/research/form-adv-irs.md`. No branches, commits or pushes (map scope ruling 2026-10-26). Then append `## Answer` here: a short summary + link to the findings file.

## Answer

- Form ADV bulk data comes as three SEC products: (A) the FOIA historical CSV archive, with full Schedule D 7.B.(1), one row per fund, **through 2024-12-31 only**; (B) monthly CSV files of registered advisers and ERAs, current, with per-adviser `Any PE Funds` / `Total number of PE funds`; (C) a daily IAPD XML feed, which has only the Item 7.B yes/no flag.
- The fund-type field is Schedule D 7.B.(1) **Q10**: one of hedge, liquidity, private equity, real estate, securitized asset, venture capital, or other. "Private equity fund" is defined by exclusion: not any other type, and no ordinary-course redemption rights.
- Identifiers: adviser CRD (`1E1`), SEC file number (`801-` registered / `802-` ERA), CIK; fund ID `805-…`, which is stable and shared across advisers; Form D file number. In the archive, fund → adviser links via `FilingID`, and each fund carries its name and GP/manager names.
- ERAs file Item 7 / Schedule D 7.B.(1) too, and all three products include them. State-registered advisers and advisers exempt from reporting are absent.
- IRS EO BMF: monthly cumulative CSV by state/region, keyed by EIN, with `SUBSECTION`, `STATUS`, `FOUNDATION`, `NTEE_CD` and other fields. It identifies an *entity* as exempt but not its holdings. Unapplied churches and revoked organizations are absent. Only Form 990 **Schedule R** (e-file XML, 2019+) names related corporations and partnerships with % ownership.
- Terms: sec.gov content is public and may be redistributed (10 req/s cap). IRS files are U.S. Government works (17 U.S.C. §105). IAPD terms of use were not found.
- Main gap: no bulk source found for fund-level 7.B.(1) data from 2025 on. It exists only in per-adviser IAPD PDFs, where the fund-type checkbox does not extract as text.

[findings](../research/form-adv-irs.md)
