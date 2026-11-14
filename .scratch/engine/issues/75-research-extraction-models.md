# Research: Candidate extraction models and hosts

Type: research
Status: resolved
Blocked by: none
Map: [engine](../map.md)

## Question

For each candidate model for claim extraction, what are the facts a choice depends on: price (per million tokens, cache and batch discounts), context length and output limit, structured-output support, license and open weights, data terms (retention, training on inputs, where it runs), which hosts serve it and at what precision, and what self-hosting would need?

## Context

- Created 2026-11-13 from "Extraction execution" (developer's ruling). The developer wants DeepSeek V4.1 Flash and other open-weight models (Kimi and others) considered alongside Anthropic's models, hosted on OpenRouter, DigitalOcean, RunPod, vast.ai or similar. **No OpenAI models of any kind**, open-weight ones included (developer's personal reasons).
- The job is narrow: read one stored document (a press release, news article, portfolio page, or a whole SEC filing of 100,000+ tokens) and return a strict JSON list of claims, each with a quote that must match the stored text exactly (`verify_citations` rejects any mismatch). No web search, no agent loop.
- Findings go to [extraction-models](../research/extraction-models.md), every claim cited to a primary source. They feed "Task: Compare extraction models on audit documents" (its cost estimate) and "Extraction execution".

## Answer

Resolved 2026-11-13 by a research subagent; findings in [extraction-models](../research/extraction-models.md), every claim cited.

- **Nine candidates, all with 1M-token context:** Claude Haiku 5.5, Sonnet 5.5 and Opus 5.5 (closed); DeepSeek V4.1 Flash (MIT); Kimi K3.1 Pro (MIT-style with conditions); Qwen3.8 flagship/Max and Qwen3.8-27B (Apache 2.0 for the 27B); GLM-5.3 (MIT-style); Mistral Large 4 (modified MIT, though its blog says Apache 2.0). No OpenAI models.
- **Price and features, first-party:** Haiku $0.10/$0.50 per million (above 100K tokens $0.50/$2.50), Sonnet $2/$10, Opus $4/$20, all with 50% batch and strict JSON schemas; DeepSeek $0.30/$1.20 (off-peak half), no batch, JSON mode only; Kimi $2/$10, batch at 60%, strict schemas; Qwen Max $2/$6; Qwen 27B $0.50/$3; GLM $1.40/$4.40, no strict schemas; Mistral $0.70/$2.10, 50% batch, strict schemas.
- **Data terms:** Anthropic: no training by default, deleted within 30 days. DeepSeek: stored in China, kept while the account exists, may be used for training (opt-out by email). Kimi: terms allow using content, but its zero-retention page says enterprise data isn't trained on (contradictory). GLM: not stored, Singapore. Mistral: kept 30 days, trains unless you opt out. Qwen: stays in the region called.
- **Cost, cheapest sensible route (1,000 ordinary documents at 10K in/2K out; one 10-K at 150K in/4K out):** Haiku $1.00 / $0.043; DeepSeek off-peak $2.70 / $0.025; Mistral batch $5.60 / $0.057; Qwen 27B $11 / $0.087; Qwen Max batch $16 / $0.16; Sonnet batch $20 / $0.17; GLM $22.80 / $0.23; Kimi batch $24 / $0.20; Opus batch $40 / $0.34.
- **Comparison run (50 documents, all nine models):** about $13 ($9.30 on cheaper OpenRouter routes); reasoning tokens billed as output could raise it, but under $40.
- **Caveats:** DeepSeek's API name moved to the "1017" snapshot on 2026-10-17 and also serves V4-Pro requests, so a test must pin 1017; OpenRouter's batch routes for DeepSeek and Kimi run on an FP4 host listed without structured outputs; Anthropic's native citations copy quotes exactly but can't be combined with structured outputs. Unconfirmed: Mistral Large 4's long-context score, Qwen Cloud's retention period, whether OpenRouter's Batch API passes a JSON schema through.

Handed on:
- "Task: Compare extraction models on audit documents": the cost estimate and the pinning caveat.
- "Extraction execution": the price, feature and data-terms table.
