# Chains and brands first; local businesses parked

Status: accepted (2026-11-04). Changes the launch product in `decisions.md` §4, §5 and §11 and `pre-launch-seeding.md`. ADRs 0001–0003 still stand.

The first product maps private equity ownership of **national chains and brands**. It is a website. The **local-businesses** plan (NPPES census, launch states, SoS and vet license board connectors) is **parked** on record, not dropped. We chose this mainly because of the work per business. A local census needs state-by-state connectors and still leaves most businesses unclassified: WhoIsMyDentist has classified about 2% of New York offices. Chains and brands are a bounded set that can be fully checked, they are the highest-volume pain (`painpoints.md`), and people look them up more often than a dentist. Live local competitors (Grass, WhoIsMyDentist, Private Equity Vet) and doubts about local revenue added to the case.

## Rules

- **Active product:** chains and brands. Version 1 is a website. A native app and barcode scanning come later.
- **Money model:** search is free and never metered (`monetizationideas.md`: never meter evidence). Paid alerts tell a user when a followed brand changes hands. Product categories may carry affiliate links with a visible disclosure, ranked by a published rule and never by commission. Prices live in `monetizationideas.md`.
- **Retirement side deferred:** the employer → plan lookup and Form 5500 exposure number (ticket 35) are deferred. BDC loan data (ticket 36) is the first follow-up, so a PE-owned chain's page can show which public funds lend to it or its parent. Form ADV ingestion (ticket 34) stays, because that is how a PE firm is identified (ADR 0001).
- **Local parked:** its tickets and its launch plan stay on file and are not rewritten for chains. Unparking it is a developer decision.
- **Ticket layout:** shared engine questions live in `.scratch/engine/`. Product questions live in `.scratch/chains-and-brands/` (active) and `.scratch/local-businesses/` (parked), and the deferred retirement lookup in `.scratch/retirement/` (parked; added 2026-11-04). Each has its own spec: `engine/spec.md` plus one spec per product. Ticket numbers stay unique across all three folders (`docs/agents/issue-tracker.md`).

## Consequences

- `GLOSSARY.md` defines an ownership chain as starting from "a local business". The brand and chain model ticket owns that change. Until it is settled, that wording is a known open conflict with this ADR.
- The launch-state and census sections of `decisions.md` §4 and §11 and `pre-launch-seeding.md` describe the parked local plan, not the launch. A chains-and-brands seeding plan follows the category audit.

## Considered options

- **Stay local-first:** keeps the dentist and vet story and the only per-location ownership data, but every state adds connectors and most businesses still read "no PE evidence found".
- **Run both products at once:** keeps both stories, but splits one developer's time and makes every doc serve two launches.
- **Lead with a barcode scanner app:** Buy'r already does it, and most grocery scans would say no PE. A test of USDA branded data put about 1–4% of products under PE or similar investors.
