# OpenTable (Booking Holdings) — Business Intelligence Engineer (data + applied AI) — London — 2026-09

## Metadata
- Date: 2026-09-30
- Fit Score: HIGH. A hybrid DE/BI/applied-AI role: Python + SQL ELT into Snowflake, Airflow, LLM API integrations (OpenAI/Anthropic), RAG, vector DBs, agentic workflows, evaluation/monitoring of AI outputs, dashboards with automated alerts. That covers pc_pipeline (Snowflake/dbt/Airflow + LLM agent) and LVMH (RAG + LLM-as-judge) almost exactly. Gaps: 2+ years (you have internship + projects), Superset/Preset (Power BI + Streamlit transfer), API development (light).
- Tailoring effort: MEDIUM, and worth it: a dedicated summary. No existing CV combines Snowflake/Airflow pipelines + RAG/agents + dashboards (McKinsey = AI data foundations, no BI; Booking = finance). See instructions.
- Source: LinkedIn (direct paste)
- Contract: Not stated (permanent expected)
- Location: London, hybrid (2 days/week in office)
- Compensation: Not stated
- Company: OpenTable (Booking Holdings), restaurant reservations platform. Reports to the Manager, Business Intelligence.

## UK work authorization (checked 2026-09-30, reference/check_sponsor.py, register 2026-09-29)
- Sponsor: CONFIRMED. "OpenTable International Limited", London, Worker (A rating), Skilled Worker (+ GBM).
- Salary must clear the Skilled Worker threshold (£41,700 or going rate). Confirm early.
- Right-to-work form: "I currently do not have the right to work in the UK and would require company visa sponsorship."

## CV Tailoring Instructions (for Claude Code)
Variant: B (General Modern Stack), AI + BI-forward. ENGLISH CV.
Branch: `variant-b-general` (edit `resume_base.tex`). Follow `CLAUDE.md`: comment-don't-delete, one page, no geometry/font changes, don't commit.
1. Summary: comment out the current active summary, add a `% OpenTable BI Engineer (London) —` label comment, then set as the active text:
   "Data and BI engineer combining pipelines with applied AI: Python/SQL ELT into Snowflake with dbt tests and Airflow orchestration, an LLM agent that turns business questions into validated SQL over a semantic layer, and a RAG chatbot with an LLM-as-judge evaluation framework (LVMH). Dashboards in Power BI and Streamlit; data-quality framework at BNP Paribas."
   Must not exceed the current summary's line count. If it wraps, drop "(LVMH)" then "and Streamlit".
2. Skills: BI & Semantic → "Power BI (DAX), Streamlit, dbt Semantic Layer" if it fits without wrapping. Programming → "Python, Git, LLM APIs (OpenAI, Anthropic)" only if true and it fits; otherwise leave. Warehousing → Snowflake first.
3. CFA: out of the summary (not a finance role).
4. Rebuild with tectonic, confirm one page, export: `cp build/resume_base.pdf output/cv_kris_huang_opentable_business_intelligence_engineer.pdf`. Attach under a neutral filename.

## Cover Letter Angle
They want someone who finds operational friction, then ships the fix, whether that's a pipeline, a dashboard, or an AI tool. pc_pipeline is that loop: dbt models on Snowflake with tests and an Airflow DAG, then an LLM agent that lets non-technical users ask questions in plain language and get SQL validated against a semantic layer (the LLM never writes free-form SQL). At LVMH you built a RAG chatbot and, crucially, the evaluation framework (LLM-as-judge) to know whether it was right. That's their "validation, evaluation and monitoring of AI outputs". At BNP you worked directly with business users to turn messy manual data into a trusted model. You'd bring the same instinct to sales/ops workflows at OpenTable.

## Preparation Gaps
- Superset/Preset: datasets, charts, alerts & reports; how to wire metric alerts (thresholds, anomaly triggers).
- Automated action triggers: event-driven alerts (Airflow sensors/callbacks, Slack webhooks), idempotency.
- RAG in production: chunking, embeddings, vector DB (pgvector/Pinecone/Snowflake Cortex Search), retrieval eval, guardrails, cost/latency.
- Agent frameworks: LangChain/LlamaIndex tool calling vs your hand-rolled validation-gate approach (and why you chose it).
- API development: small FastAPI service exposing a model/agent.
- Restaurant/marketplace metrics: covers, seated diners, no-show rate, restaurant churn, sales pipeline.

## Stack Analysis

### Have
- SQL, Python; Snowflake; Airflow; dbt; data modeling
- LLM agent (NL → validated SQL), RAG chatbot, LLM-as-judge eval
- Dashboards: Power BI, Streamlit
- Data quality/validation frameworks (BNP, dbt tests)
- Business-facing communication (BNP, LVMH)

### Missing
- 2+ years of hands-on DE/BI experience
- Superset/Preset/MicroStrategy
- Vector DB in production; API development

### Partial
- LLM API integrations: used in projects (confirm which providers)
- LangChain/LlamaIndex: concept + your own orchestration

### Green Flags
- Applied AI (RAG, agents, eval) is core: your differentiator
- Snowflake + Airflow + Python: your stack
- Business-first problem discovery; end-to-end ownership
- Booking Holdings group; licensed sponsor; generous benefits; 2 office days/week

### Red Flags
- 2+ years required
- Out-of-hours communication expectation (global team)
- UK move restarts the French residency clock
- No age-discrimination wording

## Notes
- Verdict: APPLY with the tailored build. One of the best London matches alongside Fitch and Gousto.

## Raw JD (abridged)
OpenTable (Booking Holdings), Business Intelligence Engineer, London hybrid (2 days). Reports to Manager, BI. At the intersection of DE, analytics and applied AI: ETL pipelines, dashboards, production AI tools, RAG pipelines, automated action triggers.
Responsibilities: business-first discovery with sales/strategy/ops; ETL/ELT, data models, automations in Python/SQL into Snowflake; LLM APIs (OpenAI/Anthropic), RAG, vector DBs, agentic workflows; Superset/Preset dashboards with automated alerts; validation/evaluation/monitoring of pipelines and AI outputs; evaluate Airflow, LangChain, LlamaIndex; explain to non-technical partners.
Minimum: CS/Stats/DS/IS/Econ degree + 2+ years in DE/BI/applied analytics; advanced SQL + Python (processing, integration, API dev, modeling); Snowflake + Airflow or similar; AI APIs, vector DBs, RAG, LangChain/LlamaIndex; dashboards (Superset, MicroStrategy, Tableau…); proactive, communicative, end-to-end ownership.
