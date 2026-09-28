# Heuritech — Data Engineer — 2026-09

## Metadata
- Date: 2026-09-22
- Fit Score: Medium (Medium-High on REQUIRED skills, pulled down by the DE/infra weighting + seniority). You hit every REQUIRED skill at least partially — and your pc_pipeline portfolio now carries real Airflow orchestration + incremental models + a semantic-layer AI agent, which is unusually strong evidence for your level. Gated by: this is a heavier DE/infra role (crawling stack, K8s, Celery, observability) than the AE roles, and it wants "several years... ideally 3-5+".
- Source: Direct paste (Heuritech)
- Contract: Not stated (CDI expected)
- Location: Paris (Heuritech HQ) — English-working, international team
- Compensation: Not stated — confirm, check vs Passeport Talent floor.

## This is a DATA ENGINEER role, not an Analytics Engineer role
It leans harder into software/infra than the AE postings: owning a crawling/ingestion stack, K8s, Celery task queues, Docker, AWS infra, Datadog/OpenTelemetry observability. Your dbt/Airflow/modeling core matches the pipeline half strongly; the infra half is where the real gaps are. Good news: those infra items are mostly in the NICE-TO-HAVE list, not required.

## CV Tailoring Instructions
Variant: B (General Modern Stack) — engineering-forward
Branch: variant-b-general
FRENCH CV: not required (English-working, international). English canonical is correct here; French CV available if they prefer.
Summary line (English): "Data/Analytics Engineer who owns pipelines end-to-end — dbt models and tests in a layered warehouse, orchestrated with Airflow (idempotent DAGs, retries, dependency management), plus an LLM agent built over the semantic layer. Reliability-first, comfortable in the guts of the stack."
Skills reorder: Variant B, but PORTFOLIO-FORWARD. This is a role where pc_pipeline IS the pitch — foreground Airflow orchestration, dbt (incremental + tests), Python, Git, and the AI-agent build. Make sure Airflow and the semantic layer are explicit.
CFA positioning: Out of summary and de-emphasized — irrelevant to a DE role. Education only.
Optional adds / domain note: Heuritech is fashion-trend forecasting — your LVMH (luxury/fashion) data project is a genuine domain resonance. Worth a line in the cover letter, not the summary.

## Cover Letter Angle
Heuritech's Data Engineering team owns the whole pipeline — crawling and ingestion, transformation and orchestration, through to reliable well-structured data for the rest of the company — on Snowflake + dbt + Airflow. That end-to-end ownership is exactly what your pc_pipeline project rehearses: a layered dbt build (staging → intermediate → QA → marts) with a full test suite, an incremental model with an explicit late-arriving-data guard, a MetricFlow semantic layer, and a real Airflow DAG you built and debugged — task groups in strict dependency order, retries, idempotency, and a selector bug you caught where `stg_+` silently matched zero models. Add the AI-agent you built over the semantic layer (a natural-language → validated-SQL translator), which speaks directly to their nice-to-have of "leveraging AI tools, including building custom skills or integrating MCP servers" — something you do daily, not in theory. And a light touch of domain resonance: your data work at LVMH (Maison Loewe) sits in the same luxury/fashion space Heuritech forecasts for. Be honest that the crawling-infra and containerization side is where you'd ramp; the pipeline, orchestration, and modeling core is already how you work.

## Preparation Gaps
NOTE: unlike the recent AE roles, this one needs prep BEYOND the one-month plan — the infra half is a different track. Only invest if you're pursuing DE-infra roles, not just AE.
- **Crawling / scraping pipelines + infrastructure** — central to Heuritech (they crawl social media at massive scale). Study distributed crawling: rate limiting, proxies, queueing, retry/backoff, dedup. Your TripAdvisor project touched semi-structured data but not crawling infra.
- **Containerization / Kubernetes / Docker** — pervasive in their stack. Learn Docker (images, containers, compose) and K8s concepts (pods, deployments, services). Nice-to-have but everywhere here.
- **Celery / task queues** — workers, brokers, task distribution; pairs with the crawling stack.
- **Observability: Datadog + OpenTelemetry** — traces/metrics/logs. Concept-level POV; this recurs across roles (AI-agent alerting, pipeline monitoring) and is worth owning generally.
- **Snowflake hands-on** — you're on DuckDB; dbt transfers, but get real Snowflake reps (your trial). Same as synthesis.
- **uv** (Python packaging) — named specifically; quick swap from your conda/pip habit. Learn uv basics.
- **CI/CD** — synthesis item; dbt-in-CI, test-on-PR.
- **AWS infra** — you're AWS-familiar; go one level deeper on the services a data platform uses (S3, ECS/EKS, IAM basics).

## Stack Analysis

### Have (much stronger now, per portfolio)
- Airflow orchestration — HANDS-ON: real DAG, task groups, dependency order, retries, idempotency reasoning, dbt-selector debugging (rare depth for your level; lead with it)
- dbt — full layered pipeline + tests + an incremental model with late-arriving-data handling
- SQL + data modeling (dimensional, star schema, QA layer)
- Python — generators + a multi-module LLM agent (translator/interpreter/parser/validator/compiler + Streamlit app)
- Git — advanced discipline (branch strategy, gitignore reasoning, stash recovery)
- Semantic layer (MetricFlow) + an AI agent over it
- Data quality / tests / reliability mindset — the spine of pc_pipeline
- AI tooling / custom skills / MCP — authentic (you build custom Claude skills and work in an MCP environment daily) — a rare, genuine match for that nice-to-have
- Linux/macOS + bash — comfortable

### Missing
- "Several years / ideally 3-5+" DE or SWE experience — you're a graduating intern; the real gate
- Crawling / scraping pipeline infrastructure
- Kubernetes / Docker / containerization
- Celery / task queues
- Datadog / OpenTelemetry / observability tooling
- Snowflake hands-on (DuckDB locally; on CV via skills)
- uv (named specifically)

### Partial
- CI/CD — strong Git, CI pipeline practice partial
- AWS — familiar, not deep on infra services
- Scalability at large data volumes — reasoned about it (incremental, idempotency) but not at their crawl scale

### Green Flags
- End-to-end pipeline ownership (ingestion → orchestration → modeling) — matches how you now work
- Snowflake + dbt + Airflow core — your exact modern stack
- Reliability/observability/data-quality emphasis — your strength
- "Real ownership + autonomy" — suits your self-driven portfolio style
- AI-tools/custom-skills/MCP nice-to-have — authentic differentiator few candidates have
- English-working; product team; not a bank; fashion domain resonates with your LVMH work

### Red Flags
- None on JD quality. Fit concerns only: it's a DE/infra role (crawling, K8s, Celery, observability) heavier than your AE core, plus the 3-5+ year framing. A stretch where the portfolio carries the argument.

## Notes
- Ranking: a stretch, but a GOOD stretch — your Airflow + AI-agent portfolio does more talking here than on a pure-AE posting, and the AI-tooling nice-to-have is a rare authentic match. Apply if you want to lean toward the DE/infra track; the portfolio is your strongest lever.
- Synthesis signal (for the next batch synthesis): DE-infra roles require a DISTINCT prep track from AE roles — crawling, containerization, task queues, observability — that the AE-focused one-month plan doesn't cover. Worth deciding whether you're targeting AE, DE-infra, or both, because the prep diverges here for the first time.

## Raw JD

Company: Heuritech — fashion-trend forecasting. Pipeline: crawling/ingestion of massive social-media & physical-events data → computer-vision models → predictions mapped to fashion trends → time series feeding product metrics/forecasts.

Team: Data Engineering owns the entire pipeline (crawling, ingestion, transformation, orchestration → reliable structured data for Data Science, Product, etc.). Stack: Snowflake, dbt, Airflow, Celery, K8s, AWS, Datadog.

Role (Data Engineer): build/maintain/scale systems turning raw crawled data into trustworthy usable data. Includes: design/maintain Airflow DAGs + orchestration logic; build/evolve dbt models in Snowflake; improve reliability/monitoring/data quality; work on the crawling stack + infra; contribute to internal tools; prototype new tools/architectures. Real ownership + autonomy.

Looking for: several years in Data Engineering or SWE with strong data focus (ideally 3-5+ years); comfortable owning full pipeline lifecycle (ingestion → orchestration → modeling); robust/observable/maintainable systems; large data volumes + scalability; prototype → production; structure/test/document code.

Required: Python + env/dependency tooling (uv); solid SQL + data modeling + dbt (or similar); workflow orchestration (Airflow or equiv); modern cloud DW (Snowflake or equiv); CI/CD familiarity; Git; comfortable in Linux/macOS + bash.

Nice-to-have: Celery/task queues; web crawling/scraping pipelines; Kubernetes/Docker; cloud platform (AWS); agile; observability (Datadog); OpenTelemetry (traces/metrics); comfortable leveraging AI tools (e.g. Claude) including building custom skills or integrating MCP servers.

Soft skills: ownership, autonomy, stakeholder engagement, end-to-end lead (scoping → implementation → communication), initiative. International company — comfortable in English (written + spoken).
