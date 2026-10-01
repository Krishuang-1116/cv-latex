# Qogita — Data Engineer — 2026-10

## Metadata
- Date: 2026-10-01
- Status: To apply — reuse `cv_kris_huang_valtech_data_engineer_snowflake.pdf` (optional summary swap below)
- Fit Score: Medium — the stack and duties are a near-exact match (ELT into a cloud warehouse, dbt modeling with tests and docs, Airflow, data-quality monitoring, cost/partitioning). The blocker is "3+ years building production data pipelines", stated once as a requirement rather than a restated hard gate (unlike Pyl.Tech).
- Source: LinkedIn
- Contract: Permanent (assumed); €60–75k base + bonus + equity
- Location: not stated; the EUR salary points to Amsterdam (HQ). Qogita also has a London entity.

## Visa / Contract
- NL: **Qogita EU B.V.** is on the IND recognised-sponsor register (KvK 74714643). Highly skilled migrant: €60k/yr ≈ €4.6k/mo excluding holiday allowance, comfortably above the reduced post-study threshold (€3,122/mo in 2026). Also likely above the standard under-30 threshold; confirm.
- UK (if London): **Qogita UK Ltd** is an A-rated Skilled Worker sponsor; €60k ≈ £50k+ clears £41,700.
- NL employers have screened on location (Marktlink). State the relocation upfront: self-funded move, available from January 2027.

## CV Tailoring Instructions
- Decision: reuse `output/cv_kris_huang_valtech_data_engineer_snowflake.pdf`. Its summary already reads like this JD: dbt models with tests and docs on Snowflake, Python ELT, Airflow (idempotent DAGs, retries), Git/CI-CD, LLM agent.
- Optional summary swap (variant-b-general, output `cv_kris_huang_qogita_data_engineer.pdf`) if you want the data-quality monitoring angle up front, since Valtech's summary doesn't mention the BNP framework:
  Data Engineer on the modern ELT stack: tested, documented dbt models on Snowflake, Python ingestion and Airflow orchestration with retries and idempotent reruns, and a data-quality framework that flags identity, duplicate and code mismatches across three source systems before they reach reporting (BNP Paribas Securities Services).
- CFA: not in the summary (general-tech target).
- Don't add Dagster, Redshift or BigQuery.

## Cover Letter Angle
Qogita's catalogue problem (the same branded product arriving from many suppliers under different codes, prices and currencies) is the data problem I've been solving in a different domain. At BNP Paribas Securities Services I built a data-quality framework that catches identity-resolution failures, duplicates and inconsistent codes across three manually maintained source systems before they reach reporting, and designed the dimensional model that sits on top of it. In pc_pipeline I run the same discipline as code: dbt models with generic and singular tests for six defect classes, Airflow with retries and idempotent reruns, and a semantic layer so metrics are defined once. That's the "trust the data you build on" mandate in your JD.

## Preparation Gaps
- **Production depth (the 3+ years gap):** prepare a concrete incident story. What breaks in an ELT pipeline (schema drift, late-arriving data, duplicates from at-least-once loads) and how your tests and alerts would catch it. Use the BNP data-quality findings as real examples.
- **Warehouse cost and performance:** Snowflake warehouse sizing, auto-suspend, clustering keys vs BigQuery partitioning/clustering, incremental models (`is_incremental()`, merge vs insert_overwrite), query profile reading. They explicitly own costs.
- **Ingestion tooling:** Fivetran/Airbyte vs custom Python loaders, CDC from a production Postgres (logical replication / Debezium, concept level).
- **Monitoring:** dbt source freshness, `dbt test` severity/warn thresholds, Elementary or Monte Carlo-style observability, alert routing.
- **Wholesale marketplace domain:** product/SKU matching across suppliers (EAN/GTIN), price and FX normalisation, order → fulfilment funnel metrics.
- **Dagster:** know its asset-based model vs Airflow's task-based DAGs, in case it's their orchestrator.

## Stack Analysis

### Have
- dbt (models, generic + singular tests, docs), SQL, Python
- Snowflake (one of the named warehouses)
- Airflow (retries, idempotency)
- Data-quality detection across sources (BNP), dimensional modeling, SCD Type 2
- Git; semantic layer and metrics definitions

### Missing
- 3+ years of production pipeline ownership
- On-call style incident management and alerting in production
- Ingestion/CDC tooling from production databases

### Partial
- Warehouse cost/performance tuning (concepts, portfolio scale)
- CI/CD for dbt (slim CI planned in pc_pipeline v2)
- Dagster (concept only); Redshift/BigQuery (not held, Snowflake transfers)

### Green Flags
- A clear modern stack and a clear ownership split (ingestion, transformation, delivery)
- Testing, documentation, monitoring and cost ownership are explicit
- Salary transparency (€60–75k) and equity
- Sponsor-registered entities in both NL and UK

### Red Flags
- 3+ years of production experience required
- "Work independently with minimal guidance": little ramp-up support for a junior
- Office-led culture (hybrid)

## Raw JD
The role — Data engineer building and maintaining reliable pipelines that turn raw commercial and operational data into trusted, queryable datasets; hands-on modern ELT experience; pipelines that hold up under production load. The Data Engineering team owns ingestion, transformation and delivery, working with Analytics, Product, Science and Engineering.

What You'll Do
- Build and maintain ELT pipelines from production systems into the data warehouse
- Manage the modeling layer in dbt: tested, documented, performant at scale
- Deliver new datasets and metrics with Analytics and Product
- Own monitoring and alerting for pipeline failures and data-quality issues
- Analyse query performance and warehouse costs; improve schema design and partitioning
- Develop internal tooling and documentation
- Work in the platform team with other platform engineers

What You'll Bring
- 3+ years building production data pipelines with a modern ELT stack
- Hands-on dbt
- Working SQL and Python for pipeline development and data validation
- A cloud data warehouse (Snowflake, BigQuery or Redshift)
- Orchestration (Airflow or Dagster)
- Work independently; catch data-quality issues before downstream impact
- Comfortable in a fast-moving scale-up

Perks: €60,000–€75,000 base; 26 days leave + 4 personal days; performance bonus; equity; pension; L&D budget; office-led hybrid; dog-friendly offices; home-office package; socials and offsite.

Who We Are — Qogita: a B2B wholesale procurement marketplace for branded products; one of the fastest-growing B2B companies; backed by investors behind Facebook, Etsy and Shopify.
