# Research: USPTO trademark data as an official source

Type: research
Status: resolved
Map: [chains-and-brands](../map.md)

## Question

Can USPTO trademark bulk data tell us who owns a brand today, and when ownership changed, well enough to serve as an official-filing source?

## Context

- Pivot proposal (handoff §2): the bulk files describe ownership transfers (assignments); whether they give the current owner is unconfirmed. Source: https://www.uspto.gov/trademarks-application-process/checking-application-status-view-documents/trademark-bulk-data
- Adopting it would need a new source type (ADR 0003: one per publisher) and possibly official-filing self-verification. Both are schema decisions for the developer. This ticket only reports facts.
- A registered owner can differ from the brand's real owner: holding companies, IP subsidiaries, licensors.

## Find out

- Which bulk products exist (applications, assignments, daily vs annual), their format, size, update cadence, access and terms.
- Does any file state the current registered owner per mark, or must it be rebuilt from the assignment chain? How are mergers, security interests (loan collateral) and name changes recorded?
- Is there an official API for one mark's status and owner, and what are its limits?
- Test on 5–10 known brands from the pilot categories: does the registered owner match the operating owner a primary source names? Note IP-holding subsidiaries.
- What one citable unit would be (one assignment record? one mark record?) under the engine's RawDocument rule: one document per citable row.

## How to resolve

AFK. A subagent invokes the `research` skill and writes findings, every claim cited to its primary source, to `.scratch/chains-and-brands/research/uspto-trademarks.md`. No branches, commits or pushes. Then append `## Answer` here: a short summary + link.

## Answer

Researched 2026-11-04. Findings, each claim cited: [research/uspto-trademarks.md](../research/uspto-trademarks.md).

- **Current owner per mark: yes, but only as "last recorded owner".** USPTO's Trademark database (shown in TSDR as "Current Owner(s) Information") holds one owner per mark. It auto-updates only for six kinds of recorded documents, even when the chain of title is broken. Recording is "ministerial", not a validity check (TMEP §§503.01(c), 504; 37 CFR §3.54).
- **Changes are logged separately.** The Assignment database has one record per recorded document (reel/frame): free-text conveyance, parties, dates, and serial/registration numbers, but no mark text. Security interests and licenses are recorded for notice only. Mergers, name changes and entity conversions update the owner.
- **Bulk products.** Daily XML for applications, assignments and TTAB, plus yearly research CSVs that run about 2 years behind. All are on the Open Data Portal, marked public domain.
- **Access needs registration.** The ODP needs a USPTO.gov sign-in (since 2026-06-18), and its API needs an ID.me-linked key. The TSDR single-mark API needs its own key (60 requests per minute). Nothing was signed up for and no bulk file was downloaded.
- **Spot checks (8 brands).**
  - The registered owner never named the PE sponsor; for sponsor-owned brands it was a brand-level IP holder or franchisor entity.
  - Stock acquisitions left no USPTO record.
  - The public companies matched the filer or a named subsidiary.
  - In 1 of 8 (Jersey Mike's), the TSDR owner disagrees with an assignment recorded in 2019.
  - Every mark had recorded lender security interests.
- **Open for the developer** (facts only, no pick): whether to adopt USPTO as a source type; whether it self-verifies; one source type or two (the two databases are not independent); what a mark-level claim attaches to; whether security interests feed any relationship; and the citable unit.
