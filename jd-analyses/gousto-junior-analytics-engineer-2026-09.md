# Gousto — Junior Analytics Engineer — London — 2026-09

## Metadata
- Date: 2026-09-29
- Fit Score: HIGH on content. A genuinely junior AE role (mentoring, "you don't need to be an expert") in an in-house product company, on dbt + Git/CI + Databricks, with semantic models "to enable self-service through agents and LLMs", which is exactly what your pc_pipeline LLM agent over a MetricFlow semantic layer does. The risk is not fit but the UK salary threshold (see below).
- Tailoring effort: ZERO. Send `output/cv_kris_huang_mckinsey_data_engineer_i.pdf` (summary = dbt + semantic layer + LLM agent + LLM-as-judge + BNP data quality). Optional: nothing else.
- Source: LinkedIn (direct paste)
- Contract: Not stated (permanent expected)
- Location: London, hybrid, 1 day/week in office
- Compensation: Not stated
- Company: Gousto, UK recipe-box scale-up, data-driven consumer product.

## UK work authorization (checked 2026-09-29, reference/check_sponsor.py, register downloaded 2026-09-29)
- Sponsor: CONFIRMED. "SCA Investments t/a Gousto", London, Worker (A rating), Skilled Worker route.
- The real risk is salary: Skilled Worker needs £41,700 or the occupation going rate, whichever is higher. The reduced new-entrant rate (70% of going rate, £33,400 floor) only applies if you meet its criteria (e.g. under 26 at application, switching from a UK Student/Graduate visa, or other listed cases). A "Junior" AE band in London may sit below £41,700.
- ACTION: apply, and at the first recruiter call ask (a) the salary band and (b) whether they sponsor Skilled Worker for this junior role. If the band is under the threshold and you don't meet new-entrant criteria, it's a no regardless of fit.
- Right-to-work form: "I currently do not have the right to work in the UK and would require company visa sponsorship."

## CV Tailoring Instructions
Variant: B, AI/semantic-layer-forward, ENGLISH. Reuse the McKinsey PDF; no new build.
If you want a dedicated file for tracking: `cp output/cv_kris_huang_mckinsey_data_engineer_i.pdf output/cv_kris_huang_gousto_junior_analytics_engineer.pdf` (same content).

## Cover Letter Angle
They name the thing you've already built: semantic models that let agents and LLMs answer business questions. In pc_pipeline you built dbt models tested against 6 defect classes, defined metrics once in a MetricFlow semantic layer, and put an LLM agent on top that turns natural-language questions into validated SQL. The lesson you can share is that the agent is only as reliable as the grain and metric definitions under it. At BNP you did the unglamorous part on real data (three messy sources, SCD Type 2, a data-quality framework), and at LVMH you built a RAG chatbot with LLM-as-judge evaluation. You want a team where you learn production dbt/Databricks practice from senior AEs while contributing on the semantic/agent side from day one.

## Preparation Gaps
- Databricks: Delta tables, dbt-databricks adapter, Unity Catalog at concept level (PySpark held from TripAdvisor).
- Recipe-box domain metrics: orders per active customer, retention/churn cohorts, AOV, menu/recipe popularity, fulfilment/waste. Sketch a subscriptions + orders star schema.
- Semantic layer on Databricks: metric views / dbt Semantic Layer; how you'd expose them to an LLM agent (and guardrails).
- Git/GitHub PR workflow + dbt CI (slim CI).

## Stack Analysis

### Have
- dbt, SQL, Python, Git; CI concepts
- Data modeling from business questions (BNP, pc_pipeline star schema)
- Semantic layer + LLM agent for self-service (pc_pipeline); LLM evaluation (LVMH)
- Pipelines + data quality (Airflow DAG, dbt tests, BNP DQ framework)
- Dashboards (Power BI, Streamlit); stakeholder communication
- Cloud: AWS familiar (any cloud accepted)

### Missing
- Databricks hands-on
- Production CI/CD ownership

### Partial
- Large/complex ingestion pipelines: project-level (PySpark 1M+ records)

### Green Flags
- Explicitly junior, mentored, "apply even if you don't tick every box"
- In-house product company; modern stack (dbt, Databricks)
- Semantic layer + agents/LLMs named as part of the role: your differentiator
- Only 1 day/week in office
- Licensed sponsor (A rating)

### Red Flags
- Junior salary band may fall below the Skilled Worker threshold (the deciding risk)
- Databricks instead of Snowflake (minor; transferable)
- Moving to the UK restarts the French residency timeline
- No age-discrimination wording

## Notes
- Verdict: APPLY. Best junior-level content match in London; the only open question is the salary band vs the Skilled Worker threshold, so raise it early.

## Raw JD (abridged)
Gousto, Junior Analytics Engineer, London, hybrid (1 day/week in office). Analytics team; build data foundations; learn from experienced engineers; dbt and Databricks in a modern cloud environment; semantic layers and AI/agentic tools for querying data.
Do: learn the data; support stakeholders; help maintain ingestion pipelines; build data models and dashboards; dbt workflows, Git/GitHub, CI/CD; collaborate with product squads; semantic modelling to enable self-service through agents and LLMs.
You: some SQL/data analysis experience (role, project, placement or degree); interest in SQL, Python, dbt, Databricks, cloud (AWS/GCP/Azure); open to AI and agentic workflows; good communicator; proactive learner; organised. "Apply anyway" if you don't tick every box.
