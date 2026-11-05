# Research: USPTO trademark data as an official source

Type: research
Status: open
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

AFK. A subagent invokes the `research` skill and writes findings, every claim cited to its primary source, to `.scratch/chains-and-brands/research/uspto-trademarks.md`. No branches, commits or pushes. Then append `
