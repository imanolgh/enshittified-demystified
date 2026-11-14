# Research: Candidate extraction models and hosts

Ticket: [75-research-extraction-models](../issues/75-research-extraction-models.md) · Researched 2026-11-13 · Reading only: no account opened, no paid API called. Sources are providers' docs, pricing, terms and model cards, OpenRouter's public model API, and Artificial Analysis as the one independent benchmark. Prices are US dollars per million tokens as listed on 2026-11-13. Bracketed ids point to the sources at the end.

## Summary

| Model | Open weights, license | Context / max output | First-party price, in / out | Batch | Strict JSON schema | First-party data terms | Cheapest sensible route |
|---|---|---|---|---|---|---|---|
| Claude Haiku 5.5 | No | 1M / 128K | $0.10 / $0.50; $0.50 / $2.50 over 100K prompt tokens | 50% off | Yes | No training by default; deleted within 30 days; US company | Anthropic batch |
| Claude Sonnet 5.5 | No | 1M / 128K | $2 / $10 | 50% off | Yes | As Haiku | Anthropic batch |
| Claude Opus 5.5 | No | 1M / 128K | $4 / $20 | 50% off | Yes | As Haiku | Anthropic batch |
| DeepSeek V4.1 Flash (1017) | Yes, MIT | 1M / 384K | $0.30 / $1.20; off-peak $0.15 / $0.60 | None; off-peak is half price | No (JSON mode; strict only for tool calls, beta) | May train on inputs; kept while the account exists; stored in China | DeepSeek off-peak, or OpenRouter hosts |
| Kimi K3.1 Pro | Yes, MIT-style with revenue and display conditions | 1M / not stated | $2 / $10 | 60% of list | Yes | May use content to improve services unless agreed in writing; Singapore | Moonshot batch |
| Qwen3.8 flagship (2.4T-A95B, hosted as Max) | Yes, MIT-style with revenue and display conditions | 1M (262K native) / 131K | $2 / $6 | 50% off, hosted Max only | Hosted Max only | Content used only to run the service; stays in the region called | Qwen Cloud batch |
| Qwen3.8-27B | Yes, Apache 2.0 | 262K native, 1M with YaRN / 131K | $0.50 / $3 | None | No (JSON mode) | As Qwen flagship | OpenRouter FP8 host |
| GLM-5.3 | Yes, MIT-style; security review above $10B revenue | 1M / 128K | $1.40 / $4.40 | None found | No (JSON mode) | Not stored; Singapore | Z.ai, or OpenRouter FP4 host |
| Mistral Large 4 | Yes, modified MIT; serving it as a service needs a license | 1M / not stated | $0.70 / $2.10 | 50% off | Yes | 30-day abuse retention; trains unless you opt out; France | Mistral batch |

Not covered: Google Gemini and other closed non-OpenAI models, and every OpenAI model, open-weight ones included.

## Anthropic: Claude Haiku 5.5, Sonnet 5.5 and Opus 5.5

All three are closed models with a 1M-token context and 128K maximum output (300K on the Batch API with a beta header) [a-models]. The Batch API takes 50 percent off, finishes most batches within an hour and expires the rest after 24 hours [a-batch]. Structured outputs "guarantee schema-compliant responses through constrained decoding", but schemas may not use recursion, `minLength`, `maxLength` or numeric bounds [a-so]; batches accept them [a-batch]. Citations return `cited_text` copied by the API from the document, "guaranteed to contain valid pointers" and not billed as output, but they "cannot be used together with structured outputs" [a-cite].

Data terms: no training on API data by default, except feedback [a-train]; inputs and outputs deleted within 30 days, flagged content kept up to 2 years [a-retain]. Zero retention is available by agreement for these three models [a-zdr], but not for batches, whose results stay 29 days [a-batch]. US-only inference costs 1.1 times list [a-price].

Evidence: no launch page reports a long-context benchmark [a-haiku] [a-sonnet] [a-opus]. Artificial Analysis's AA-LCR (questions over 10K to 100K-token documents) scores Opus 5.5 at 84.7 and Sonnet 5.5 and Haiku 5.5 at 82.7, at maximum effort [aa-lcr]. Vendor claims: a grader that checked every figure and quote passed 16 of 18 Opus 5.5 reports [a-opus]; Haiku 5.5 beat Haiku 4.5 on AlphaSense's document Q&A, 0.84 to 0.76 [a-haiku]. No source documents paraphrasing.

- **Haiku 5.5**, released 2026-10-07: a whole 10-K crosses 100,000 prompt tokens and pays the higher tier; batch $0.05 / $0.25, or $0.25 / $1.25 above 100K [a-price]. Thinking is on by default, effort `medium` [a-haiku-doc].
- **Sonnet 5.5**, released 2026-09-28: batch $1 / $5 [a-price] [a-sonnet].
- **Opus 5.5**, released 2026-09-22: batch $2 / $10 [a-price] [a-opus]. Thinking cannot be turned off [a-models], so billed output exceeds the JSON.

## DeepSeek V4.1 Flash

What it is. DeepSeek released V4.1-Flash on 2026-09-10: a mixture of experts it describes as 552B parameters with about 8B active on input and 16B on output, on a new "Causal Encoder-Decoder" design [ds-news-0910]. A "minor update", V4.1-Flash-1017, followed on 2026-10-17 [ds-news-1017]. The API name `deepseek-flash` now serves 1017 [ds-price], and since 2026-09-14 even `deepseek-v4-pro` runs on V4.1-Flash, at Flash rates, until a V4.1-Pro ships [ds-news-0910]. The name is a moving target; the eval should pin 1017.

Weights. Both snapshots are MIT-licensed with no added restrictions [ds-hf] [ds-hf-1017]. The checkpoint mixes BF16, FP8 and INT8 tensors, 510 GB; Hugging Face counts 763B tensor elements against the card's 552B "backbone parameters" [hf-api].

Price and limits. 1M context, 384K output [ds-price]. No batch API; off-peak hours halve every price: $0.15 in, $0.003 cache hit, $0.60 out, doubled at peak (01:00 to 04:00 and 06:00 to 10:00 UTC on weekdays) [ds-price].

Structured output. JSON mode only, and content "may contain only spaces" even on a normal stop [ds-json]; a beta `strict` mode covers tool calls [ds-tools]. Alibaba's Qwen Cloud lists `deepseek-v4.1-flash-1017` with strict `json_schema` [qwen-so], and most OpenRouter hosts enforce schemas [or-api]. Thinking is on by default and can be switched off [ds-think].

Data terms. The privacy policy (updated 2026-02-10) names Hangzhou DeepSeek Artificial Intelligence Co., Ltd., stores personal data "in People's Republic of China", keeps inputs "for as long as you have an account", and lists model training as a purpose, with an opt-out requested by email [ds-privacy]. The platform terms apply mainland Chinese law [ds-tos].

Evidence. The card's only long-context figure is LongBench-V2 for the base model: 45.2, against 51.5 for V4-Pro-Base [ds-hf]. AA-LCR scores 1017 at 82.7, level with Sonnet and Haiku [aa-lcr].

## Kimi K3.1 Pro (Moonshot AI)

What it is. Moonshot's current model, on its API since about 2026-10-23 (the blog gives no date; OpenRouter and Artificial Analysis list that day) [kimi-blog] [or-api] [aa-lcr]. A 2.8T-parameter mixture of experts with 104B active, trained quantization-aware with MXFP4 weights [kimi-hf]; the weights reached Hugging Face in early November, 1,561 GB [hf-api].

License. MIT-style, but a model-as-a-service business with over $20 million revenue in 12 months needs a separate agreement, and a product with over 100 million monthly users or $20 million monthly revenue must display "Kimi K3.1-Pro"; neither applies to internal use [kimi-license].

Price. $2 / $10, cached input $0.20; batch is 60 percent of list, $1.20 / $6.00 [kimi-price] [kimi-batch]. Maximum output is not stated. It always reasons, at effort `low`, `high` or the default `max` [kimi-params].

Structured output. `strict` `json_schema` uses "token-level constrained decoding" for schemas in Moonshot's own dialect; known issues include Markdown fences around the JSON and `oneOf` / `$ref` "not strictly followed" [kimi-so].

Data terms. Moonshot AI PTE. LTD. runs the platform on servers in Singapore under Singapore law [kimi-privacy] [kimi-tos]. The terms (updated 2026-07-30) let Moonshot "use Content to provide, maintain, develop, support, and improve the Services" unless the customer agrees limits in writing [kimi-tos]. The ZDR page says enterprise data is not used for training by default and offers enterprises zero retention, except for batch jobs [kimi-zdr]; the terms are the contract.

Evidence. Vendor: OfficeQA Pro v2 at 64.4 and claim-level hallucinations down from 23.4 to 8.3 percent on an internal test [kimi-blog]. Independent: AA-LCR 86.3, the best of these candidates [aa-lcr].

## Other open-weight candidates

I picked 2026 open-weight models with a 1M context and either long-context results or strict schemas. Dropped: MiniMax M3.1-Flash, whose license conditions commercial use on a "Built with" notice and notifying MiniMax, and bans military use [minimax-lic]; Gemma 4 31B, with 256K context and AA-LCR 69.7 [gemma-hf] [aa-lcr]; Llama, with nothing newer than Llama 4 (April 2025) [hf-llama].

**Qwen3.8 flagship (Qwen3.8-2.4T-A95B, hosted as Qwen3.8-Max).** Alibaba, API since 2026-08-12; 2.4T total, 95B active [qwen-blog] [qwen-hf] [aa-lcr]. Its MIT-style license requires showing the name above 100 million monthly users or $20 million monthly revenue, and a separate license for a model-as-a-service business above $50 million a year [qwen-lic]. Native context 262,144, extensible to 1,010,000; Qwen Cloud serves 1M with 131,072 output at $2 / $6 [qwen-hf] [qwen-doc]. Batch (half price) and strict `json_schema` work on the hosted Max only [qwen-batch] [qwen-so]. Alibaba's agreement (Singapore law) limits use of content to running the service and complying with law; data stays in the region called, and only the "Global" scope can reach mainland China; no retention period found [qwen-terms] [qwen-regions]. Vendor: MRCR v2 at 256K 92.9, LongBench v2 66.3 [qwen-hf]; AA-LCR 80.3 [aa-lcr]. Self-hosting: 2,496 GB at FP8, on 16x B300 or 32x H200 [qwen-recipe].

**Qwen3.8-27B.** Dense 27B, Apache 2.0, 2026-08-14; 262,144 native context, 1M with YaRN, which may hurt short texts [qwen-27b-hf] [aa-lcr]. Qwen Cloud charges $0.50 / $3 with no batch and no strict schema [qwen-27b-doc] [qwen-so]; OpenRouter hosts enforce schemas, from PrimeIntellect at FP8 ($0.087 / $0.622, zero retention, 262K) to DeepInfra at BF16 ($0.15 / $1.875) [or-api]. Reasoning can be switched off. FP8 weights are 31 GB, one GPU [qwen-27b-recipe]. AA-LCR 82.0 with reasoning, 69.3 without [aa-lcr].

**GLM-5.3 (Z.ai).** API since 2026-08-18; 753B total, about 40B active (from the GLM-5 paper for the shared base) [zai-notes] [glm-hf] [glm5-paper]. MIT-style, except that a model-as-a-service business with revenue over $10 billion must pass Z.ai's security review [glm-lic]. 1M context, 128K output, always reasons [zai-glm]. $1.40 / $4.40, no batch API found [zai-price]; JSON mode only [zai-so]. Z.ai's API data addendum says it stores no content and processes it "generally" in Singapore, with no explicit training clause [zai-privacy]. On OpenRouter, Z.ai's own FP8 endpoint enforces schemas at list price; Wafer's FP4 endpoint costs $0.07 / $1.40 [or-api]. Self-hosting: 756 GB at FP8 on 8x H200 [glm-recipe]. AA-LCR 79.7 [aa-lcr].

**Mistral Large 4.** Weights 2026-10-29, generally available 2026-11-05; 1T total, 49B active [mistral-blog] [mistral-hf] [mistral-docs]. The license requires any model-as-a-service business to buy a commercial license; the blog's "Apache 2.0" label contradicts the LICENSE file [mistral-lic] [mistral-blog]. 1M context, maximum output not stated [mistral-docs]. $0.70 / $2.10, batch 50 percent off; EU and US endpoints cost 1.1 times, without batch [mistral-price] [mistral-batch] [mistral-regional]. Strict JSON schema supported [mistral-so]. Mistral keeps inputs 30 days for abuse monitoring unless granted zero retention (not for batch) [mistral-privacy] [mistral-zdr], and may train on products "set to opt-in by default" unless you opt out [mistral-terms] [mistral-optout]. Self-hosting: 1,061 GB at FP8 on 2x 8 H200 or 8x B200 [mistral-recipe]. AA-LCR has no score for the final model yet; a reported 81.3 for the preview is unconfirmed [aa-lcr].

## Hosts

### OpenRouter

No markup on token prices; 5.5 percent on credit purchases [or-faq] [or-pricing]. OpenRouter "does not store your prompts or responses" unless you opt in and does not train on them; upstream providers may [or-data] [or-privacy]. It screens all traffic for child sexual abuse material since 2026-10-27 [or-zdr]. `provider.zdr: true` routes only to zero-retention endpoints, and an endpoint with an unconfirmed policy counts as retaining and training [or-routing] [or-zdr]. The zero-retention list held Bedrock and Vertex for the Claude models (not Anthropic's own endpoint), Moonshot's own Kimi endpoint, and 42 of 48 DeepSeek 1017 endpoints (not DeepSeek's own) [or-zdr-list].

Strict schemas pass to the upstream provider, and "exact compliance is not guaranteed on every endpoint"; without `provider.require_parameters: true` a request can land on a provider that ignores the schema [or-so] [or-routing]. DeepSeek's own endpoint and Bedrock's Claude endpoints list no structured outputs [or-api].

The Batch API bills "typically" 50 percent of sync within 24 hours and keeps data 30 days, so it never runs under zero retention; its docs do not say whether `response_format` reaches the provider [or-batch]. The only batch endpoint for DeepSeek 1017 and for Kimi was Sail Research at FP4, listed without structured outputs [or-api].

Precision: of DeepSeek 1017's 48 endpoints, 21 declare FP8, 6 FP4 or MXFP4 and 21 nothing; DeepSeek's own is listed at its off-peak $0.15 / $0.60. Of Kimi's 24, 17 declare FP4 or MXFP4, its native format, Moonshot's own included. Claude runs only on Anthropic, Bedrock, Vertex and Azure, at list price [or-api].

### DigitalOcean

Its serverless inference sells the Claude models at list price, DeepSeek V4.1 Flash and 1017 at $0.30 / $1.20 (DeepSeek's peak rate), Kimi K3.1 Pro at $2 / $10, GLM-5.3 at $1.40 / $4.40 and Qwen3.8-Max at $2 / $6; no Gemma, one small Mistral [do-price]. Batch discounts cover only OpenAI and Anthropic models [do-price] [do-features]. Its docs claim structured outputs only for Qwen3.8-Max and GLM models, and its API reference shows no `response_format` [do-models] [do-api]; OpenRouter, though, lists DigitalOcean serving DeepSeek 1017 at $0.18 / $0.72 with structured outputs [or-api]. It does not train on, or pass on, data sent to models it hosts, and states no retention period or region [do-privacy].

### Self-hosting on RunPod or vast.ai

Neither DeepSeek nor Moonshot publishes BF16 weights, so full precision means the released 510 GB and 1,561 GB [hf-api]. vLLM and SGLang give the KV cache whatever memory remains and publish no sizing formula [vllm-mem] [sglang-args]. My arithmetic: DeepSeek squeezes onto 8x H100 80GB and fits comfortably on 8x H200 (1,128 GB) or 4x B300; Kimi needs 8x B300 (2,304 GB) or 16x H200 over two nodes.

| GPU | RunPod Secure / Community, per GPU-hour | vast.ai median (minimum) |
|---|---|---|
| H100 SXM 80GB | $4.39 / $2.69 | $2.27 ($1.77) |
| H200 141GB | $5.29 / $3.59 | $4.61 ($2.37) |
| B200 180-192GB | $7.99 / $5.98 | $10.63 ($6.25) |
| B300 288GB | $8.99 / $6.94 | not listed |

RunPod's page was updated 2026-11-12 [runpod]; vast.ai's feed (2026-11-14 01:30 UTC) does not say whether offers are interruptible [vast].

## Cost model

Per document: input tokens / 1M x input price + output tokens / 1M x output price. Ordinary document: 10,000 in, 2,000 out; whole 10-K: 150,000 in, 4,000 out; eval: 45 ordinary plus 5 filings per model; no caching. First line per model: first-party batch, else first-party rate. Second line: the cheapest OpenRouter endpoint that is zero-retention and lists structured outputs.

| Model and route | Prices, in / out | 1,000 ordinary documents | One 10-K | Eval run |
|---|---|---|---|---|
| Haiku 5.5, Anthropic batch | $0.05 / $0.25; over 100K $0.25 / $1.25 | 10 x 0.05 + 2 x 0.25 = $1.00 | 0.15 x 0.25 + 0.004 x 1.25 = $0.043 | 45 x 0.001 + 5 x 0.0425 = $0.26 |
| Sonnet 5.5, Anthropic batch | $1 / $5 | 10 + 10 = $20.00 | 0.15 + 0.02 = $0.17 | 0.90 + 0.85 = $1.75 |
| Opus 5.5, Anthropic batch | $2 / $10 | 20 + 20 = $40.00 | 0.30 + 0.04 = $0.34 | 1.80 + 1.70 = $3.50 |
| DeepSeek 1017, DeepSeek off-peak (peak doubles) | $0.15 / $0.60 | 1.50 + 1.20 = $2.70 | 0.0225 + 0.0024 = $0.025 | 0.12 + 0.12 = $0.25 |
| DeepSeek 1017, Particle AI (flex tier, precision undisclosed) | $0.03 / $0.25 | 0.30 + 0.50 = $0.80 | 0.0045 + 0.001 = $0.0055 | $0.064 |
| Kimi K3.1 Pro, Moonshot batch | $1.20 / $6 | 12 + 12 = $24.00 | 0.18 + 0.024 = $0.20 | 1.08 + 1.02 = $2.10 |
| Kimi K3.1 Pro, Wafer (MXFP4) | $0.253 / $8.80 | 2.53 + 17.60 = $20.13 | 0.038 + 0.035 = $0.073 | $1.27 |
| Qwen3.8-Max, Qwen Cloud batch | $1 / $3 | 10 + 6 = $16.00 | 0.15 + 0.012 = $0.16 | 0.72 + 0.81 = $1.53 |
| Qwen3.8-27B, Qwen Cloud | $0.50 / $3 | 5 + 6 = $11.00 | 0.075 + 0.012 = $0.087 | $0.93 |
| Qwen3.8-27B, PrimeIntellect (FP8) | $0.087 / $0.622 | 0.87 + 1.24 = $2.11 | $0.016 | $0.17 |
| GLM-5.3, Z.ai | $1.40 / $4.40 | 14 + 8.80 = $22.80 | 0.21 + 0.018 = $0.23 | $2.16 |
| GLM-5.3, Wafer (FP4) | $0.0699 / $1.40 | 0.70 + 2.80 = $3.50 | $0.016 | $0.24 |
| Mistral Large 4, Mistral batch | $0.35 / $1.05 | 3.50 + 2.10 = $5.60 | 0.0525 + 0.0042 = $0.057 | $0.54 |

The eval for all nine candidates on their first lines costs 0.26 + 1.75 + 3.50 + 0.25 + 2.10 + 1.53 + 0.93 + 2.16 + 0.54 = **about $13**, or about $9.30 using the cheaper second lines. Tripling output for reasoning keeps it under $40; OpenRouter adds 5.5 percent on credits [or-faq].

Self-hosting cannot serve a 50-document eval sensibly (hourly billing, 510 GB to 1.5 TB downloads). For bulk work, 8x H200 at RunPod Community's $28.72 an hour must clear about 10,600 ordinary documents an hour to beat DeepSeek's off-peak $2.70 per thousand; Kimi's 8x B300 at $55.52 must clear about 2,300 an hour to beat Moonshot's batch.

## What this doesn't tell us

Only the hands-on comparison (task 76) can show:

- How often each model copies quotes character for character, especially from 150,000-token filings; no source measures it, and AA-LCR stops near 100K.
- Whether FP4 and MXFP4 hosts quote as exactly as the labs' own endpoints.
- Real output size: Opus 5.5, Kimi, GLM and the open-weight Qwen flagship always reason, and reasoning bills as output.
- Real token counts: each model has its own tokenizer, so the same filing costs a different number of tokens per model.
- Whether strict schemas survive the cheap routes; OpenRouter's batch docs and DigitalOcean's API reference are silent.
- Recall against the audit's expected claims, and behaviour on documents with no ownership claim.
- The throughput that would make self-hosting pay.

## Sources

Anthropic
- [a-price] Pricing: https://platform.claude.com/docs/en/about-claude/pricing
- [a-models] Models overview: https://platform.claude.com/docs/en/about-claude/models/overview
- [a-haiku-doc] Claude Haiku 5.5 model page: https://platform.claude.com/docs/en/models/haiku-5-5/overview
- [a-batch] Batch processing: https://platform.claude.com/docs/en/build-with-claude/batch-processing
- [a-so] Structured outputs: https://platform.claude.com/docs/en/build-with-claude/structured-outputs
- [a-cite] Citations: https://platform.claude.com/docs/en/build-with-claude/citations
- [a-zdr] API and data retention (Covered Models are the Fable and Mythos models only): https://platform.claude.com/docs/en/manage-claude/api-and-data-retention
- [a-train] "Is my data used for model training?" (updated 2026-08-18): https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training
- [a-retain] "How long do you store my organization's data?" (updated 2026-07-01): https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data
- [a-haiku] https://www.anthropic.com/claude-haiku-5-5 · [a-sonnet] https://www.anthropic.com/claude-sonnet-5-5 · [a-opus] https://www.anthropic.com/claude-opus-5-5

DeepSeek
- [ds-news-0910] V4.1-Flash release: https://api-docs.deepseek.com/news/news260910
- [ds-news-1017] V4.1-Flash-1017 release: https://api-docs.deepseek.com/news/news261017
- [ds-price] Models and pricing: https://api-docs.deepseek.com/quick_start/pricing
- [ds-json] JSON output: https://api-docs.deepseek.com/guides/json_mode
- [ds-tools] Tool calls, strict mode: https://api-docs.deepseek.com/guides/tool_calls
- [ds-think] Thinking mode: https://api-docs.deepseek.com/guides/thinking_mode
- [ds-hf] https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash · [ds-hf-1017] https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017
- [ds-privacy] Privacy policy (updated 2026-02-10): https://cdn.deepseek.com/policies/en-US/deepseek-privacy-policy.html
- [ds-tos] Open Platform terms (effective 2026-04-29): https://cdn.deepseek.com/policies/en-US/deepseek-open-platform-terms-of-service.html

Moonshot AI
- [kimi-blog] https://www.kimi.ai/blog/kimi-k3-1-pro
- [kimi-hf] https://huggingface.co/moonshotai/Kimi-K3.1-Pro · [kimi-license] https://huggingface.co/moonshotai/Kimi-K3.1-Pro/raw/main/LICENSE
- [kimi-price] https://platform.kimi.ai/docs/pricing/chat (prices are in the page's embedded table data) · [kimi-batch] https://platform.kimi.ai/docs/pricing/batch
- [kimi-params] https://platform.kimi.ai/docs/api/models-overview · [kimi-so] https://platform.kimi.ai/docs/guide/response_format
- [kimi-zdr] https://platform.kimi.ai/docs/guide/zero-data-retention
- [kimi-tos] Terms (updated 2026-07-30): https://platform.kimi.ai/docs/agreement/modeluse · [kimi-privacy] https://platform.kimi.ai/docs/agreement/userprivacy

Alibaba (Qwen)
- [qwen-hf] https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B · [qwen-lic] https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B/raw/main/LICENSE
- [qwen-blog] https://www.alibabacloud.com/blog/alibaba-unveils-qwen3-8-27b-and-releases-weights-of-qwen3-8-flagship-model_603463
- [qwen-doc] https://docs.qwencloud.com/models/qwen3-8-2-4t-a95b.md and https://docs.qwencloud.com/models/qwen3-8-max.md
- [qwen-batch] https://docs.qwencloud.com/developer-guides/text-generation/batch · [qwen-so] https://docs.qwencloud.com/developer-guides/text-generation/structured-output.md
- [qwen-terms] Customer agreement (updated 2026-08-27): https://terms.alicdn.com/legal-agreement/terms/common_platform_service/20260319165752650/20260319165752650.html
- [qwen-regions] https://docs.qwencloud.com/developer-guides/getting-started/regions · [qwen-recipe] https://recipes.vllm.ai/Qwen/Qwen3.8-2.4T-A95B
- [qwen-27b-hf] https://huggingface.co/Qwen/Qwen3.8-27B · [qwen-27b-doc] https://docs.qwencloud.com/models/qwen3-8-27b.md · [qwen-27b-recipe] https://recipes.vllm.ai/Qwen/Qwen3.8-27B

Z.ai (GLM)
- [zai-notes] https://docs.z.ai/release-notes/new-released.md · [zai-glm] https://docs.z.ai/guides/llm/glm-5.3 · [zai-price] https://docs.z.ai/guides/overview/pricing
- [zai-so] https://docs.z.ai/guides/capabilities/struct-output · [zai-privacy] API data processing addendum: https://docs.z.ai/legal-agreement/privacy-policy.md
- [glm-hf] https://huggingface.co/zai-org/GLM-5.3 · [glm-lic] https://huggingface.co/zai-org/GLM-5.3/raw/main/LICENSE · [glm5-paper] https://arxiv.org/html/2602.15763 · [glm-recipe] https://recipes.vllm.ai/zai-org/GLM-5.3

Mistral AI
- [mistral-blog] https://mistral.ai/news/mistral-large-4-oss/ · [mistral-hf] https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B · [mistral-lic] https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B/raw/main/LICENSE
- [mistral-docs] https://docs.mistral.ai/models/mistral-large-4-0 · [mistral-price] https://docs.mistral.ai/inference/pricing · [mistral-batch] https://docs.mistral.ai/inference/batch-processing
- [mistral-regional] https://docs.mistral.ai/inference/regional-inference · [mistral-so] https://docs.mistral.ai/inference/conversations/structured-output/custom
- [mistral-privacy] Privacy policy (effective 2026-09-03): https://legal.mistral.ai/terms/privacy-policy · [mistral-zdr] https://docs.mistral.ai/admin/monitor-comply/zero-data-retention.md
- [mistral-terms] Commercial terms (effective 2026-09-25): https://legal.mistral.ai/terms/commercial-terms-of-service · [mistral-optout] https://help.mistral.ai/en/articles/455207-can-i-opt-out-of-my-input-or-output-data-being-used-for-training
- [mistral-recipe] https://recipes.vllm.ai/mistralai/Mistral-Large-4-1T-A52B

Dropped candidates
- [minimax-lic] https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash/raw/main/LICENSE · [gemma-hf] https://huggingface.co/google/gemma-4-31B-it · [hf-llama] https://huggingface.co/api/models?author=meta-llama&sort=createdAt&direction=-1

Hosts and shared
- [hf-api] Hugging Face model API (creation dates, tensor types, file sizes): https://huggingface.co/api/models/deepseek-ai/DeepSeek-V4.1-Flash-1017?blobs=true and the same path for the other repositories
- [aa-lcr] Artificial Analysis, AA-LCR (scores read from the page's embedded chart data): https://artificialanalysis.ai/evaluations/artificial-analysis-long-context-reasoning
- [or-api] OpenRouter model and endpoint API: https://openrouter.ai/api/v1/models and https://openrouter.ai/api/v1/models/deepseek/deepseek-v4.1-flash-1017/endpoints (same path per model)
- [or-zdr-list] https://openrouter.ai/api/v1/endpoints/zdr · [or-zdr] https://openrouter.ai/docs/features/zdr
- [or-data] https://openrouter.ai/docs/guides/privacy/data-collection · [or-privacy] Privacy policy (updated 2026-08-31): https://openrouter.ai/privacy
- [or-routing] https://openrouter.ai/docs/features/provider-routing · [or-so] https://openrouter.ai/docs/features/structured-outputs
- [or-faq] https://openrouter.ai/docs/faq · [or-pricing] https://openrouter.ai/pricing · [or-batch] https://openrouter.ai/docs/guides/features/batch-api
- [do-price] (updated 2026-11-10): https://docs.digitalocean.com/products/inference/details/pricing/ · [do-models] https://docs.digitalocean.com/products/inference/details/models/
- [do-features] https://docs.digitalocean.com/products/inference/details/features/ · [do-api] https://docs.digitalocean.com/products/inference/reference/api/serverless-inference/ · [do-privacy] https://docs.digitalocean.com/products/inference/details/data-privacy/
- [runpod] (updated 2026-11-12): https://www.runpod.io/pricing
- [vast] https://vast.ai/pricing.md and its feed https://storage.googleapis.com/vast-public-gpu-pricing/gpu-pricing-public.json
- [vllm-mem] https://docs.vllm.ai/en/latest/configuration/conserving_memory.html · [sglang-args] https://docs.sglang.io/advanced_features/server_arguments.html
