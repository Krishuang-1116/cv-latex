# Valtech — Data Engineer (Snowflake) — 2026-09

## Metadata
- Date: 2026-09-28
- Fit Score: Medium-High — strong stack match on YOUR modern lane (Snowflake + dbt + Python + advanced SQL + Git/CI-CD + data quality/testing + layered architecture), and Agentic AI / Snowflake Cortex / AI-enabled data products is a listed nice-to-have (your differentiator). Gaps: production-DE-at-scale (fault-tolerance, observability, monitoring, Snowflake cost/perf tuning on large datasets), a consulting/agency model (client-facing), and it's DE-ops-leaning. No hard years number; softened by strong "apply even with gaps" language.
- Source: Direct paste
- Contract: Permanent — Paris, France; remote/hybrid options (country-dependent)
- Location: Paris — English-working ("professional English", international teams). French CV not required.
- Compensation: Not stated ("competitive") — confirm, check vs Passeport Talent floor.

## Where this sits vs your other consultancies
Valtech is a digital-experience agency/consultancy (clients: L'Oréal, Mars, Audi, P&G, VW) — client-facing delivery model like Aubay/Talan. BUT the stack is modern Snowflake + dbt + Python (NOT Microsoft Fabric like Talan, NOT Power-BI-heavy like Ipsos). So tech-wise it's squarely your lane; the only reservation is the consulting/agency model (client missions, less product ownership) you've been cautious about. Best-fitting of your consultancy options by a wide margin.

## This is DE-ops-leaning, but on your stack (not the Heuritech divergence)
Emphasis on production pipelines, fault-tolerance, observability, monitoring, RCA, cost/perf optimization. That's DE-production-ops — but on Snowflake/dbt/Python (your stack), NOT crawling/K8s/Celery. So it's within reach of your AE lane leaning DE, not the separate infra track you declined. The one real new area is production-at-scale reliability + Snowflake cost/perf tuning.

## CV Tailoring Instructions
Variant: B (General Modern Stack) — engineering + AI-forward, PORTFOLIO-forward
Branch: variant-b-general
FRENCH CV: not required (English-working). English canonical.
Summary line (English): "Data/Analytics Engineer on the modern stack — dbt models with tests and documentation on Snowflake, Python ELT, Airflow orchestration (idempotent DAGs, retries), Git/CI-CD, plus an LLM agent over the warehouse. Reliability- and quality-first."
Skills reorder: Variant B, portfolio-forward. Foreground Snowflake + dbt (models/tests/docs) + Python + SQL + Git/CI-CD + Airflow. Surface the AI-agent as the Agentic-AI nice-to-have. Note Azure as the cloud env (AWS-familiar).
CFA positioning: Out of summary; education only.
Optional adds: none. Portfolio (dbt + Airflow + AI agent) is the pitch.

## Cover Letter Angle
Valtech wants a Data Engineer who builds reliable, testable, observable production pipelines on Snowflake + dbt, with Git/CI-CD discipline and ownership from technical design through production support — and lists Agentic AI / Snowflake Cortex as a plus. That maps onto what you built solo in pc_pipeline: a layered dbt pipeline on a warehouse with a full test suite and documentation, an incremental model with a late-arriving-data guard, real Airflow orchestration (task groups, retries, idempotency — the building blocks of fault-tolerant, recoverable pipelines), and an LLM agent over the semantic layer (your take on AI-enabled data products). You pair that with strong SQL/Python and a rigor-first, documentation-heavy way of working. Be honest that production-at-scale reliability and Snowflake cost tuning on large datasets are where you'd ramp — the engineering fundamentals and quality discipline are already how you build.

## Preparation Gaps
Covered by the learning plan; two sharpen here:
- **Snowflake performance & cost optimization at scale** — named explicitly ("optimise Snowflake queries and data models for performance, scalability and cost across large datasets"). You have Snowflake on CV but not deep tuning. Learn: virtual warehouses/sizing, clustering keys, query profile, result/caching, partition pruning, cost monitoring. RECURRING theme (Tarmac Redshift, Alma BigQuery cost, now Snowflake) — worth owning warehouse perf/cost generally.
- **Production reliability at scale** — fault-tolerance, observability/monitoring, recovery mechanisms, RCA. Your Airflow retries/idempotency are the base; extend to monitoring/alerting and a clear RCA narrative.
- **Terraform / IaC** (nice-to-have) — same contained add flagged at Alan.
- **Azure** — AWS-familiar; concept-level (here it's just the cloud env, data stack is Snowflake/dbt).
- Nice-to-haves you can speak to: Airflow/Dagster (have Airflow), Agentic AI / Snowflake Cortex (your agent work), AWS S3/RDS/etc (AWS-familiar), Power BI (have). Kafka/streaming is a genuine gap (skip unless pursuing).

## Stack Analysis

### Have
- Snowflake — on CV (their core platform)
- dbt — models, tests, documentation, dependency management (their must-have)
- Advanced SQL + layered data architecture — pc_pipeline (staging→int→marts) + BNP modeling
- Python — ingestion/transformation/automation/API (their must-have)
- Git / CI-CD / engineering best practices — advanced Git discipline; CI concept
- Airflow orchestration — hands-on (fault-tolerance building blocks)
- Data quality / testing / documentation — pc_pipeline + BNP DQ framework
- AI agent / Agentic AI / AI-enabled data products — authentic (listed nice-to-have)
- RCA / troubleshooting mindset — BNP data-quality debugging + your build-log discipline

### Missing
- Production-grade pipelines at scale (fault-tolerant, observable, monitored) — yours is solo/small-data
- Snowflake cost/perf optimization on large datasets — named requirement
- Years of production DE experience (no number stated, but "strong hands-on... deep knowledge" implies it) — softened by "apply with gaps" language
- Kafka / streaming (nice-to-have)
- Terraform/IaC (nice-to-have)

### Partial
- Azure — AWS-familiar; Azure is the cloud env here
- Observability/monitoring — retries/idempotency yes; monitoring/alerting new
- CI/CD — Git strong, full CI/CD pipeline practice partial

### Green Flags
- Modern Snowflake + dbt + Python stack — your exact lane (unlike Talan/Ipsos Microsoft roles)
- Agentic AI / Snowflake Cortex nice-to-have — your differentiator is rewarded
- Strong "apply even with gaps / value potential" language — you're in scope
- English-working, international, Paris, remote/hybrid options; not a bank
- dbt + data quality + Git/CI-CD centric — your strengths

### Red Flags
- None on JD quality. Fit notes: consulting/agency model (client-facing delivery, less product ownership) — your recurring reservation, though the modern stack offsets it; DE-ops-leaning (production reliability at scale + Snowflake cost tuning are real gaps); Azure environment (manageable — data stack is Snowflake/dbt, not Fabric).

## Notes
- Ranking: the STRONGEST of your consultancy options (modern stack + AI-agent plus + soft gate), well above Aubay/Talan. Sits just below your in-house product targets (Alan/Emeria/Elax/Alma/Tarmac) because of the agency model + production-at-scale gap. A solid application if you're open to client-facing consulting on a modern stack.
- The recurring warehouse perf/cost theme (Snowflake/Redshift/BigQuery) is now worth owning generally — pairs with the Terraform add as the two cheapest DE-adjacent unlocks on your own stack.

## Raw JD (abridged)

Valtech — "experience innovation company" (digital agency/consultancy); clients incl. L'Oréal, Mars, Audi, P&G, VW. Role: Data Engineer - Snowflake, Paris (permanent), remote/hybrid options.

Role: strong hands-on modern data engineering, specifically Snowflake + dbt, with Azure experience; advanced SQL + Python; build/maintain production-grade ELT/data pipelines; autonomous across data modelling, orchestration, monitoring, troubleshooting. Agentic AI a plus (not core).
- Design/develop/maintain dbt models, tests, documentation; strong data quality + modelling.
- Git, CI/CD, engineering best practices for maintainable/testable/reliable data products.
- Collaborate with client teams, architects, analysts, external partners (international).
Responsibilities: robust batch/scheduled pipelines in production; reliable/fault-tolerant/observable pipelines with monitoring/testing/recovery; ownership of complex workstreams design→production support; documentation; optimise Snowflake queries/models for perf/scalability/cost on large datasets; root cause analysis.

Must-have: strong dbt (models, testing, docs, dependency mgmt, deployment); strong hands-on Snowflake in production incl. perf optimisation/troubleshooting; advanced SQL + layered data architectures; Python (ingestion/transformation/automation/API); build/maintain/monitor/troubleshoot production ELT pipelines; Azure + cloud data services; Git/CI-CD/SWE practices; autonomous, investigate prod issues, communicate; professional English + international teams.
Nice-to-have: Dagster/Airflow; Terraform/IaC; Agentic AI / Snowflake Cortex / AI-enabled data products; AWS (S3/RDS/Secrets Manager/CloudWatch); Kafka/streaming; Power BI. Strong "apply even with gaps / value potential" language.
