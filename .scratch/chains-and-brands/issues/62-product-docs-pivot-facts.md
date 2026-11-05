# Product docs: competitors and stale claims

Type: task
Status: open
Map: [chains-and-brands](../map.md)

## Question

Bring the product docs up to date with facts found during the pivot, so later grilling doesn't argue from stale claims. Facts only: anything that needs a decision goes to engine "Product-doc contradictions".

## Checklist

- **marketgaps.md**: add the live competitors from `.scratch/pivot-handoff-2026-11-02.md` §4 (Buy'r, Grass, WhoIsMyDentist, Private Equity Vet + Independent Vet, Ethos, Worse on Purpose, ShopFair), dated 2026-10-31, figures marked self-reported where they are.
- **Stale "local is uncovered" claims**: marketgaps.md:10, :38; painpoints.md:74, :207 (search by phrase if lines drifted). Reword to say who now covers it, with the date.
- **painpoints.md:237** (redemption limits): the pasted threads suggest it is out of date; flag it in the Answer for the developer, don't rewrite it.
- Docs that still describe a local launch as the launch (search for "launch state", "metro", "census") get a one-line parked note pointing at ADR 0004, as decisions.md §4/§11 and pre-launch-seeding.md already have. Don't rewrite their substance (ADR 0004: local stays on record).
- **On-demand research is gone** (decisions.md §15, 2026-11-05): monetizationideas.md:43 (the Premium perk "Priority on-demand research") and :81 (the on-demand meter) get a one-line note pointing at §15.

## How to resolve

AFK. Make the edits, then append `## Answer` listing what changed and anything skipped (with why). No commits.
