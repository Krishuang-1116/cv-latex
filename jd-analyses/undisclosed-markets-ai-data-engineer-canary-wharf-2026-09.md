# Undisclosed (recruiter) — Data Engineer, Markets & AI Data Platform — 2026-09

## Metadata
- Status: TO APPLY (recruiter post; ask sponsorship + salary on first contact)
- Date: 2026-09-30
- Fit Score: MEDIUM. The domain and architecture fit well: macro/markets data, bronze-silver-gold layers, data quality, instrument/ticker mapping, clean datasets for AI agents and quant models. Your CFA plus markets background, the pc_pipeline layered design + LLM agent, and BNP identity resolution all map onto that. What drags it down: "strong production DE experience", a "small, highly experienced team" (implies seniority), time-series/tick data at scale, kdb+, APIs and entitlements.
- Tailoring effort: LOW (summary only), and worth it. The finance/markets angle and CFA must be up front here. No existing build combines markets domain + DE platform + AI agents.
- Source: LinkedIn (recruiter post, employer undisclosed)
- Contract: Not stated
- Location: London (Canary Wharf), hybrid
- Compensation: Not stated
- Company: Undisclosed specialist global-macro research/data firm serving hedge funds, asset managers and banks (AI agents, quant research, client data products).

## UK work authorization
- Sponsor: UNKNOWN (employer undisclosed). First question to the recruiter: "Does the client hold a Skilled Worker sponsor licence and sponsor at this level?" Once named, grep `reference/uk-licensed-sponsors.csv`.
- Salary must clear £41,700 or the going rate. For London markets DE that's likely fine if they sponsor.
- Right-to-work form: "I currently do not have the right to work in the UK and would require company visa sponsorship."

## CV Tailoring Instructions (for Claude Code)
Variant: A (Financial Data Infrastructure), DE + markets-forward. ENGLISH CV.
Branch: `variant-b-general` (where all current London tailoring lives; edit `resume_base.tex`). Follow `CLAUDE.md`: comment-don't-delete, one page, no geometry/font changes, don't commit.
1. Summary: comment out the active summary, add a `% Undisclosed Markets & AI Data Platform DE (Canary Wharf) -- markets domain + layered platform + AI agents; CFA kept:` label, then set as the active text:
   "Data engineer with financial-markets depth: layered (staging → intermediate → mart) pipelines on Snowflake with dbt tests, Python and Airflow, entity-resolution and data-quality checks across three messy private-capital sources at BNP Paribas, and an LLM agent that answers questions only through validated, governed metrics. \textbf{CFA Charterholder}."
   Must not exceed the current summary's line count. If it wraps, drop "and Airflow", then "messy".
2. Skills: Programming → "Python, Git, LLM APIs (Anthropic, Gemini)" (keep the current line). Warehousing: Snowflake first. Add a Domain line if space allows: "Financial markets & private capital (CFA)".
3. Optional add: Guosen (PE product monitoring, 100+ products weekly) only if it fits on one page. It strengthens the "institutional investors" angle.
4. Rebuild with tectonic, confirm one page, export: `cp build/resume_base.pdf output/cv_kris_huang_markets_ai_data_engineer.pdf`. Attach under a neutral filename.
Fallback if no build: the Lendable PDF (Python-forward, CFA kept) is acceptable.

## Cover Letter Angle
Your platform turns fragmented market, economic and research data into model-ready layers for quants and AI agents. That's the pattern I built in pc_pipeline and at BNP Paribas. At BNP I reconciled private-capital deal data across three manually maintained systems, where the hard part was identity resolution: the same client or fund under different codes and names. That's the same problem as instrument and ticker mapping. In pc_pipeline, raw data flows through staging, intermediate and mart layers with dbt tests covering six defect classes, and an LLM agent answers questions only through governed metrics, so downstream consumers can trust the numbers. As a CFA Charterholder I can talk to researchers and PMs in their language, which matters in a flat team where engineers sit next to the people consuming the data.

## Preparation Gaps
- Medallion architecture on Databricks/Delta Lake: bronze/silver/gold, Delta features (ACID, time travel, MERGE, schema evolution), and how it maps to your staging/int/mart.
- Time-series market data: bitemporal modelling (as-of vs knowledge time), point-in-time correctness and look-ahead bias for quant backtests, corporate actions adjustments, calendars/holidays, and tick vs bar data.
- Security master / symbology: tickers vs ISIN/CUSIP/SEDOL/FIGI, ticker changes over time (SCD2 applies directly), and cross-vendor mapping (Bloomberg, Refinitiv).
- kdb+/q: concept-level only (columnar in-memory time-series DB, as-of joins). Know what `aj` does and why quants love it.
- Entitlements: row-level security / vendor licensing restrictions on market data (why data redistribution rights matter).
- Observability: freshness/volume/schema checks and alerting (Great Expectations, dbt source freshness, Monte Carlo concepts).
- APIs for datasets: a small FastAPI endpoint serving a gold table, with pagination and auth.
- Macro data sources: FRED, central-bank releases, vintages/revisions of economic data (this is where your finance background shines).

## Stack Analysis

### Have
- Python, SQL; Snowflake; dbt; Airflow
- Layered pipelines (staging → intermediate → mart ≈ bronze/silver/gold)
- Data quality and validation frameworks (BNP, dbt tests)
- Entity/identity resolution across sources (≈ instrument mapping)
- Clean datasets for downstream AI agents (pc_pipeline LLM agent)
- Financial markets domain (CFA, JHU econ/finance, Guosen, UOB)

### Missing
- Strong production DE track record (years)
- kdb+/q; high-volume time-series/tick data
- Azure/Databricks/Delta Lake hands-on
- Entitlements/permissions, API development, observability tooling

### Partial
- Metadata and lineage (dbt docs/lineage graph)
- Monitoring (dbt tests; no production alerting)
- Large datasets (PySpark ETL over 1M+ records, TripAdvisor)

### Green Flags
- Markets + AI + quant: your domain is a real differentiator
- Clear architecture described (medallion, DQ, mapping, lineage, entitlements)
- Ownership, flat structure, close to data consumers; "build, not maintain"

### Red Flags
- Small "highly experienced" team: likely wants several years of production DE
- Recruiter post: employer, salary and sponsorship all unknown
- Azure/Databricks listed first (though Snowflake counts as an alternative)

## Notes
- Verdict: APPLY (low cost, via recruiter), but qualify on sponsorship first. If the recruiter confirms sponsorship, do the summary build; if not, skip.

## Raw JD (abridged)
Data Engineer, Markets & AI Data Platform, Canary Wharf hybrid. Specialist global-macro/financial-markets business building AI, quant research and data products for hedge funds, asset managers, banks. Small, experienced, flat team; engineers work with researchers, quants, product.
Build core data platform for AI agents/research tools, quant models, market/economic analysis, internal and client products, dashboards and APIs. Market, economic, research, news, internal datasets into clean model-ready data. Architecture: production ETL/ELT, bronze/silver/gold, DQ/validation, instrument & ticker mapping, metadata/lineage, monitoring/observability, entitlements, APIs/structured datasets.
Requirements: Python, SQL; production DE and ETL/ELT; Azure/Databricks/Delta Lake/Snowflake; large/complex/time-series data; DQ, monitoring, reliability; clean datasets for downstream users/models. Plus: financial market/ticker-level data, kdb+.
