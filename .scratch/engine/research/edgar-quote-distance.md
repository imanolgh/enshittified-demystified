# Research: How far from a name do SEC filings state ownership?

For engine "Cost cuts before revenue" Q2 · Measured 2026-11-20 · Code only, no API calls.

## Question

If the engine read only a window of text around each mention of a searched name instead of the whole filing, how often would it miss an ownership statement because the statement sits far from the name?

## Method

- Data: the extraction tests' saved documents and outputs in `~/.local/share/extraction-eval/` ("Extraction execution", "Task: Draft prompt p9 and run the approval check"). These are DeepSeek's whole-document reads, so every fact was found without any window.
- Sample: all 33 SEC filings in the test set (21 over 100,000 characters: 10-Ks, proxies, an annual report; the rest 8-Ks and press-release exhibits). Two filings had no readable text. The union of facts from the three p9 runs, 677 facts whose quote was located in the stored text.
- For each fact: the distance in characters from its quote to the nearest mention of the fact's subject name (legal suffixes such as "Inc." removed), and, for facts about the brand the document was fetched for, to the nearest mention of the brand name. Distance 0 means the name is inside the quote. About 4 characters make a token.

## Findings

| Facts | Count | Name inside the quote | Within 2,000 chars | Within ~2,000 tokens (8,000 chars) | Within ~8,000 tokens (32,000 chars) | Farthest |
|---|---|---|---|---|---|---|
| All facts, distance to own subject | 677 | 569 (84%) | 648 (96%) | 665 (98%) | 676 | 39,311 chars |
| Facts about the searched brand, distance to the brand name | 181 (171 with a mention found) | 106 | 157 | 168 | 171 (all) | 19,370 chars |

- 12 facts (2%) sat more than 8,000 characters from their subject's name. They came from 5 of the 33 filings: Petco's 10-K and proxy, Mister Car Wash's 10-K, Chewy's 10-K and Unilever's annual report.
- Every far case is a company writing about itself or about a company it owns: "We are currently indirectly controlled by certain funds (the "CVC Funds")", "Our Principal Stockholder controls approximately 51.2%", "LGP has more than 50% of the voting power", "We have retained a minority stake of 19.85% in TMICC". A filer calls itself "we", "us" or "the Company", so its own ownership is stated far from its name.
- All 33 filings in the sample were filed by the brand's own company, its owner, or as a deal filing. The sample holds no third-party filings (landlords' tenant lists, lenders' schedules, mortgage-pool prospectuses), so this measurement says nothing directly about them. A third party doesn't call the brand "we", so the self-reference pattern behind every far case can't occur there, but that is reasoning, not measurement.

## What it means for Q2

- Windows would miss about 2% of facts if used on a company's own filings, and the misses are its most important facts (who controls it). Those filings should stay whole reads, as Q2 proposes.
- For third-party filings, the windowed class, nothing here measures the risk. A sample of third-party hits from EDGAR full-text search would.
