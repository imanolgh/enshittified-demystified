# Task: Compare extraction models on audit documents

Type: task
Status: resolved
Blocked by: 75  (Research: Candidate extraction models and hosts)
Map: [engine](../map.md)

## Question

How do the candidate models compare on our own documents: claims found, quotes passing the exact-match check, valid structured output, long-filing reading, and cost per document?

## Context

- Created 2026-11-13 from "Extraction execution" (developer's ruling), so the model choice there is made on measured numbers, not reviews.
- **Test set:** about 50 documents from the category audit whose quotes were already checked against the source pages (chains research/category-audit-full.md §4: 943 quotes matched the re-downloaded page text), mixing press releases, news, portfolio pages and a few whole SEC filings. The expected claims come from the audit's evidence lines.
- **Run:** every candidate from "Research: Candidate extraction models and hosts" gets the same test prompt, drafted by Claude from the rules already recorded on "Extraction execution" (an eval prompt, not the approved production prompt; the developer reviews it before the run). No OpenAI models.
- **Scored:** claims found against the expected claims; share of quotes passing an exact-match check like `verify_citations`; share of responses that parse against the claim schema; behavior on long filings; cost and time per document.
- **The developer's part:** open the accounts (one OpenRouter key covers most open-weight models, plus an Anthropic key). The run spends real money: Claude gives a cost estimate from the research ticket's prices and waits for the developer's yes before running.
- Results go to `.scratch/engine/research/extraction-model-comparison.md`.
- **From "Research: Candidate extraction models and hosts"** (2026-11-13; findings in research/extraction-models.md): estimated cost for all nine candidates on 50 documents is about $13 (about $9.30 on cheaper OpenRouter routes), under $40 even if reasoning tokens run high. Pin DeepSeek to the `1017` snapshot (its API name changed underneath on 2026-10-17). OpenRouter's batch routes for DeepSeek and Kimi run on an FP4 host without structured outputs, so test them through routes that enforce the schema, or record which route was used.
- **DeepSeek search and fetch** (2026-11-13, from DeepSeek's docs: api-docs.deepseek.com/api/search/, news261113, news261017): since 2026-11-13 a chat request can turn on server-side tools `deepseek_web_search` and `deepseek_read_url`. The test runs DeepSeek with both off (the LLM never finds facts: it reads only stored documents, and quotes are checked against them); production would too. 1017's stated gains are for coding and project work ("stronger benchmark performance, faster task completion, and shorter outputs"), with no stated change to context, price or JSON output.

## Answer

Done 2026-11-13; results in [extraction-model-comparison](../research/extraction-model-comparison.md). Spend: $13.81 on OpenRouter, $0.09 on DeepSeek's own API.

- 50 documents (45 ordinary pages, 5 SEC filings including three whole 10-Ks), 70 known facts from the category audit, the same instructions and strict schema for every model, zero-retention hosts only. Qwen3.8-Max left out (no zero-retention host on OpenRouter).
- Known facts found: Qwen3.8-27B 40, Mistral Large 4 38, Kimi K3.1 Pro 38, Claude Opus 5.5 37, GLM-5.3 37, DeepSeek V4.1 Flash on DeepSeek's own API 35, the same model through OpenRouter 34, Claude Sonnet 5.5 33, Claude Haiku 5.5 31. Close enough to be mostly noise; precision not measured.
- In the long filings: Qwen3.8-27B 11 of 15, Opus 10, the others 5 to 7.
- Quotes matching exactly: 100% for Claude, Kimi and DeepSeek's own API; 99% Qwen3.8-27B; 94% GLM; 92% DeepSeek through OpenRouter (failures from two of nine hosts); 90% Mistral.
- Valid answers: 50 of 50 for most; GLM 43 (ran out of room while reasoning), Kimi and Qwen3.8-27B 49.
- Cost per document: DeepSeek's own API $0.0018, DeepSeek on OpenRouter $0.0042, Haiku $0.0057, Mistral $0.021, Qwen3.8-27B $0.026, Sonnet $0.037, GLM $0.048, Kimi $0.062, Opus $0.076. Median time: Haiku, Sonnet and DeepSeek's own API 5 to 7 seconds; Mistral, Qwen3.8-27B and GLM 73 to 90.

Handed on:
- "Extraction execution": the results table, the host effect (pin hosts, or use a provider's own endpoint), and that output room must allow for reasoning.
- "Citation verification rules": a failed quote differed by an en dash; whether dashes are normalized.
- **Precision check** (2026-11-14, developer's request; blind, 20 passing claims per route, judged by Claude before unblinding): fully correct Sonnet 20/20, Kimi 20/20, Opus 19/20, Qwen3.8-27B, Mistral, DeepSeek via OpenRouter and GLM 18/20, Haiku 17/20, DeepSeek's own API 15/20. No model invented a relationship. DeepSeek's own API's five wrong claims were one pattern on one page (a generic heading quoted instead of each brand's line); harmful details elsewhere: Haiku read "reinvested 100% of their interests" as a 100% stake, GLM marked a current controlling parent as former, DeepSeek via OpenRouter marked a completed investment as announced. Details in research/extraction-model-comparison.md.
- **From the DeepSeek prompt iteration** (2026-11-14; research/extraction-model-comparison.md "DeepSeek prompt iteration"; prompt in research/extraction-test-prompt-v5.md): DeepSeek's own API tested further at the developer's request: five prompt versions over 158 documents; v5 98% fully correct in a blind check, 99.3% exact quotes once the test's extraction artifacts are set aside. **Correction to this ticket's numbers:** most quote failures in the nine-model run were caused by the test's text extraction; with them set aside Mistral is 96.9%, GLM 99.2%, DeepSeek via OpenRouter 96.7% (Claude, Kimi and DeepSeek's own API stay 100%).
- **From the clean-text confirmation** (2026-11-14; research/extraction-model-comparison.md): with block-aware extraction (line breaks only around block elements, nothing between inline pieces), DeepSeek v5 read the clean text of 157 documents and 615 of 615 quotes matched it exactly. The model and the check must see the same cleanly extracted text; page-footer stripping made no difference in this set.
