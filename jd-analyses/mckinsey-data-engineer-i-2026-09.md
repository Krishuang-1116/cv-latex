# McKinsey & Company (QuantumBlack / Labs) — Data Engineer I — 2026-09

## Metadata
- Status: REJECTED (2026-10-01): CV-stage rejection email
- Date: 2026-09-29 (2000+ LinkedIn applicants)
- Fit Score: Medium-High on fit, low odds on volume. One of your best profile matches so far: explicitly junior (0–2 years, internships/academic projects count), and the core is data foundations for LLM/RAG/agentic systems, which is exactly your differentiator (pc_pipeline NL→SQL agent over a semantic layer, LVMH RAG + LLM-as-judge, dbt data-quality tests). The only real risks are the applicant volume and "strong communication in English AND French" (you're B2).
- Tailoring effort: LOW–MEDIUM (summary swap + one skills word, English CV).
- Source: LinkedIn (direct paste). Apply via the McKinsey careers site, not Easy Apply.
- Contract: Not stated (CDI)
- Location: Paris office; client-facing
- Compensation: "Competitive". Very likely clears the Passeport Talent threshold.
- Company: McKinsey & Company, Data Engineering community working with QuantumBlack (AI) and Labs. Consulting, but a tech/AI practice, not an ESN staffing model.

## On the 2000 applicants
- Adding one application doesn't lower your odds. Each application is screened on its own, and the cost is ~30 minutes.
- LinkedIn counts are inflated by one-click interest; a large share won't match "Python + SQL + data platform + GenAI data" at all.
- McKinsey screens are structured (CV screen → online assessment/coding test → technical + personal-experience interviews). A precise CV matters more than the pile size.
- The best lever: a referral. Search LinkedIn for ESSEC or CentraleSupélec alumni at QuantumBlack / McKinsey Paris (data engineers, not partners) and ask for a 15-minute chat, then a referral. That beats the pile.

## CV Tailoring Instructions (for Claude Code)
Variant: B (General Modern Stack), AI-forward. ENGLISH CV (English JD; French is spoken in the office).
Branch: `variant-b-general` (edit `resume_base.tex`). Follow `CLAUDE.md`: comment-don't-delete, one page, no geometry/font changes, don't commit.
1. Summary: comment out the current active summary (the Ledger version), add a `% McKinsey Data Engineer I —` label comment, then set as the active text:
   "Data engineer building data foundations for AI: a tested dbt pipeline on Snowflake with a semantic layer and an LLM agent that turns natural-language questions into validated SQL, and a RAG chatbot with LLM-as-judge evaluation (LVMH). Data-quality framework over heterogeneous sources at BNP Paribas. \textbf{CFA Charterholder}."
   Must not exceed the current summary's line count. If it wraps an extra line, drop "on Snowflake".
2. Skills: in the Programming line, change "Python, Git" → "Python, Git, coding agents (Claude Code)". Only if it doesn't wrap to a second line in the half-width column; otherwise skip.
3. Everything else unchanged. LVMH already mentions RAG + LLM-as-judge; pc_pipeline already mentions the LLM agent over MetricFlow.
4. Rebuild with tectonic, confirm one page, export: `cp build/resume_base.pdf output/cv_kris_huang_mckinsey_data_engineer_i.pdf`.
Summary line (French, if asked for a French CV): "Data Engineer qui construit les fondations data de l'IA : pipeline dbt testé sur Snowflake avec couche sémantique et agent LLM traduisant des questions en langage naturel en SQL validé, et chatbot RAG avec évaluation LLM-as-judge (LVMH). Framework de qualité des données sur des sources hétérogènes chez BNP Paribas. Titulaire du CFA."
CFA positioning: keep it at the end of the summary. For a client-facing consulting role, business/finance literacy is a plus, not noise.
Optional adds: none.

## Cover Letter Angle / "why you" (for the form and referral note)
Most junior data engineers have pipelines; few have built the data layer an LLM system actually depends on. In pc_pipeline you built the whole chain: tested dbt models (6 defect classes) → a MetricFlow semantic layer that defines each metric once → an LLM agent that turns business questions into SQL validated against that layer. The lesson you can speak to is that agent reliability is a data-modeling problem (grain, metric definitions, data quality), not a prompt problem. At LVMH you built the unstructured side: a RAG chatbot over product data with an LLM-as-judge evaluation framework. At BNP you did the unglamorous foundation work on messy real data: identity resolution, duplicates, cross-source inconsistencies. That covers structured + unstructured + evaluation + data quality, plus the business literacy (CFA) to talk to C-level clients. And you work daily with coding agents (Claude Code), which they list as a plus.

## Preparation Gaps
- RAG data engineering: ingestion + parsing of unstructured docs, chunking strategies, embeddings, vector stores (pgvector / managed), metadata filtering, freshness/re-indexing, PII handling, retrieval evaluation (recall@k, groundedness). Be able to draw the pipeline end to end.
- Agentic data access: tool/function design, text-to-SQL guardrails, semantic layers as agent interfaces. This is your home turf; prepare the 3-minute pc_pipeline story with failure modes.
- LLMOps basics: eval datasets, LLM-as-judge pitfalls, tracing/observability, versioning prompts + data.
- Batch vs streaming at concept level (listed).
- Databricks + Spark: PySpark is held; know Delta Lake basics.
- McKinsey process: an online coding/SQL assessment, technical case interviews (design a data pipeline for an AI use case), and Personal Experience Interviews (prepare 3–4 stories: impact, leadership, handling a setback, entrepreneurial drive). Practise some answers in French too.

## Stack Analysis

### Have
- Python, SQL (clean, documented code; Git discipline)
- Structured + unstructured data for AI: pc_pipeline LLM agent + semantic layer; LVMH RAG + LLM-as-judge
- Data quality fundamentals: BNP DQ framework, dbt tests
- Platforms/tools named: Snowflake, dbt, Spark (PySpark), Pandas, PostgreSQL, AWS (familiar)
- Git, CI/CD concepts; MLOps background (profile)
- Coding agents (Claude Code), a named plus
- 0–2 years with internships/projects: exact match
- English (TOEFL 120)

### Missing
- LangChain (or equivalent framework) on the CV, if not used
- Databricks, BigQuery, Azure/GCP hands-on
- Streaming pipelines

### Partial
- French "strong communication": B2 (workable in a Paris office; be ready for part of the interview in French)
- DevOps/CI-CD: principles + Git discipline, no pipeline-ops ownership
- Vector stores/retrieval infra: RAG built at LVMH; depth to verify

### Green Flags
- Explicitly junior (0–2 years), internships/projects count
- GenAI/agentic data foundations = your differentiator is the job
- Named stack overlaps yours (Snowflake, dbt, Spark, Pandas, Git)
- Structured apprenticeship/training; top brand; Paris
- Coding agents listed as a plus

### Red Flags
- 2000+ applicants: extreme volume (odds, not fit)
- Consulting model: client-facing, varied stacks, demanding culture ("high performance/high reward")
- French at "strong" level required; you're B2
- No age-discrimination wording

## Notes
- Verdict: apply, and prioritize a referral. It's the rare large-brand role where your AI + data-quality combo is the core requirement, and the junior gate is real, not aspirational.
- It's consulting, but closer to "AI engineering practice" than to an ESN. It builds exactly the skills (RAG/agentic data infra) your profile is heading toward.

## Raw JD (abridged)
McKinsey & Company — Data Engineer I, Paris, global Data Engineering community with QuantumBlack and Labs. Build foundational data infrastructure for AI applications (LLMs, retrieval systems, workflows, agentic architectures): scalable, reproducible data pipelines and components for ML/agentic/autonomous AI; secure data environments; assess data landscapes, apply data quality fundamentals, prepare data for AI; translate hypotheses into engineered features; R&D on next-gen AI. Cross-functional Agile teams with Data Scientists, ML Engineers, industry experts; client-facing up to C-level.
Qualifications: CS/Engineering degree or equivalent; 0–2+ years in a data-focused role (internships, academic projects); clean documented code (Python, SQL preferred); interest/exposure to DE for Agentic AI, GenAI, ML or BI across structured/unstructured and streaming/batch; familiarity with Databricks, Snowflake, BigQuery, PSQL; AWS/Azure/GCP; Pandas, Spark, dbt, LangChain; Git, DevOps, MLOps/LLMOps, CI/CD; strong communication in English and French; time management and autonomy; fast learner; coding agents (Cursor, Claude Code, Codex) a plus.
