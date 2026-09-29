# [Company undisclosed] — Data Analytics Engineer II (GenAI Applications) — Netherlands — 2026-09

## Metadata
- Date: 2026-09-29
- Fit Score: Medium-High on content, Medium overall. It's an analytics-engineering role on GenAI product data (chatbots, search, support automation, LLM evaluation, AI telemetry), and nearly every technical line is on your CV: SQL, Python, hands-on PySpark (TripAdvisor), data modeling, text/unstructured data, LLM evaluation (LVMH LLM-as-judge), plus all the nice-to-haves (dbt, Snowflake, Airflow, Streamlit). It's held back by 3+ years ("II" level), experimentation/A-B analysis you haven't done in production, and an unknown employer (sponsor status unverifiable until named).
- Tailoring effort: LOW (summary swap, English CV).
- Source: Direct paste. The company name is hidden, likely a recruiter/agency post. The stack (PySpark + Argo) and product scope suggest a large NL consumer-tech company; unconfirmed.
- Contract: Full-time; not stated if permanent
- Location: Netherlands, hybrid (city not stated)
- Compensation: Not stated

## Before applying / first recruiter call
- Ask the company name and city. Then check the IND recognised-sponsor register (as you did for Marktlink). Large NL tech firms almost always are; verify anyway.
- Ask whether 3+ years is firm for "II", or whether a strong junior with directly relevant GenAI eval work is considered.
- Same trade-off as Marktlink: an NL move restarts the French residency clock (orientation-year route or HSM at the €3,122/mo post-zoekjaar threshold).

## CV Tailoring Instructions (for Claude Code)
Variant: B (General Modern Stack), AI/analytics-forward. ENGLISH CV.
Branch: `variant-b-general` (edit `resume_base.tex`). Follow `CLAUDE.md`: comment-don't-delete, one page, no geometry/font changes, don't commit.
1. Summary: comment out the current active summary (whichever variant is active), add a `% Data Analytics Engineer II (GenAI, NL) —` label comment, then set as the active text:
   "Analytics Engineer working on data for GenAI products: built an LLM-as-judge evaluation framework for a multi-turn RAG chatbot (LVMH), an LLM agent over a dbt semantic layer, and PySpark ETL over 1M+ semi-structured records. Tested, documented data models and a data-quality framework at BNP Paribas."
   Must not exceed the current summary's line count. If it wraps, drop "multi-turn".
2. Skills: no change (PySpark, dbt, Snowflake, Python, SQL, semantic layer are already visible). Only if it fits without wrapping: Programming → "Python, Git, Streamlit". Only if the Streamlit app is real.
3. CFA: out of the summary (general tech / product analytics target).
4. Rebuild with tectonic, confirm one page, export: `cp build/resume_base.pdf output/cv_kris_huang_undisclosed_nl_data_analytics_engineer_ii_genai.pdf` (rename once the company is known).
Optional adds: none.

## Cover Letter Angle
The hard part of GenAI product analytics isn't the dashboards, it's defining what "good" means for an LLM output and making that measurable at scale. At LVMH you built exactly that: an LLM-as-judge evaluation framework for a multi-turn RAG chatbot, plus a similarity engine over product data. In pc_pipeline you built the structured side: an LLM agent that answers business questions through a semantic layer, sitting on tested dbt models (6 defect classes). The lesson you can speak to is that model-quality metrics are only trustworthy if the underlying data model and definitions are. TripAdvisor shows PySpark at 1M+ records on semi-structured text. BNP shows owning a data domain end to end: grain, SCD Type 2, data quality, stakeholder delivery. Frame yourself as someone who can own the "AI evaluation + telemetry" analytical domain.

## Preparation Gaps
- Experimentation analysis: A/B test design, power/sample size, guardrail metrics, novelty effects, CUPED at concept level; how you'd A/B test a chatbot change (resolution rate, containment, CSAT, escalation).
- LLM/AI product metrics: containment/deflection rate, resolution, hallucination/groundedness rates, latency and cost per conversation, thumbs-up/down bias, offline eval vs online metrics and why they diverge.
- AI telemetry data modeling: session → conversation → turn → tool-call/retrieval events; grain choices; handling long text fields; sampling for LLM-as-judge at scale.
- PySpark depth: window functions, skew, partitioning, and working with nested JSON (explode, from_json).
- Argo (Workflows) at concept level vs Airflow.
- Search/discovery metrics: CTR, NDCG/MRR at concept level.

## Stack Analysis

### Have
- Advanced SQL; Python data processing
- PySpark hands-on (TripAdvisor, 1M+ semi-structured records)
- Data modeling + modern warehouse concepts (dbt layers, star schema, SCD2, semantic layer)
- Unstructured/text + AI-generated content: LVMH RAG chatbot, embeddings/similarity; LLM agent outputs
- LLM evaluation frameworks: LLM-as-judge (LVMH)
- Data quality/reliability: BNP DQ framework, dbt tests
- Nice-to-haves: dbt, Snowflake, Airflow, Streamlit (all held)
- Stakeholder delivery: BNP, LVMH

### Missing
- 3+ years of experience
- Production experimentation/A-B analysis
- Argo
- Data governance/classification in production

### Partial
- Product analytics/user behavior: Sales Analytics + LVMH market research; no in-product event analytics yet
- Large-scale production environments: PySpark on projects, not production clusters

### Green Flags
- Explicitly an analytics-engineering role (owns data domains, models, quality), not BI-first
- GenAI evaluation + telemetry is the domain: your differentiator
- Nice-to-have list = your exact stack
- Clear, specific JD

### Red Flags
- 3+ years for a "II" level
- Employer hidden (agency post): sponsor status and team unknown
- Outside France: residency-clock trade-off
- No age-discrimination wording

## Notes
- Verdict: apply. It's one of the strongest content matches of the search, and the tailoring is a single summary swap. Get the company name first so you can verify the sponsor and adjust the export filename.
- Pairs well with the McKinsey analysis: the same AI-data story, framed as analytics (eval + telemetry) instead of data foundations.

## Raw JD (abridged)
Data Analytics Engineer II (GenAI Applications), Netherlands, Hybrid, full-time. Team building AI/GenAI products; analytics × product × data engineering; not an infrastructure/platform DE role.
Own data domains end to end: scalable analytical data models; data quality/accuracy/reliability; reusable data products; governance/stewardship/classification/security/compliance; pipeline health monitoring.
Insights: large complex datasets → insights; monitoring frameworks, operational dashboards, quality reporting; analyze product experiments, user behavior, AI model performance and evaluation outcomes; exploratory analysis pre-launch; partner with PMs, Engineers, DS, Analytics.
GenAI data: conversational AI/chatbots, search & discovery, customer-support automation, LLM evaluation workflows, AI telemetry & performance analytics.
Requirements: 3+ years in AE/DA/Product Analytics; business/product mindset; ownership definition→delivery; independent in ambiguity; stakeholder delivery + production contribution. Advanced SQL (large scale); strong Python; hands-on PySpark; data modeling + modern DW concepts; scalable maintainable transformations; structured/semi-structured/unstructured incl. AI-generated text.
Nice to have: dbt, Snowflake, Airflow, Argo, Streamlit; AI/ML/LLM products, evaluation frameworks, model performance analysis; experimentation and product metrics.
