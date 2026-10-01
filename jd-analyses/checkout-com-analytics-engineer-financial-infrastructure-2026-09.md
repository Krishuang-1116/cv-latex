# Checkout.com — Analytics Engineer (Financial Infrastructure) — London — 2026-09

## Metadata
- Date: 2026-09-30
- Fit Score: HIGH on content, Medium on the experience gate. Financial Infrastructure team serving Finance & Treasury: an accurate record of financial data, data integrity, regulatory obligations, SLAs. That's your BNP financial-data model + DQ framework + CFA. The stack (cloud DW + dbt + SQL + data modeling) is yours. "2+ years in AE/DE" is the gap; the "I" level and "Python/Java/Flink a plus, not a necessity" suggest it's a lower-mid rung, so apply anyway.
- Tailoring effort: ZERO. Send `output/cv_kris_huang_booking_holdings_data_analytics_engineer_i_treasury.pdf` (Variant A; summary = grain + SCD2 + DQ/reconciliation + Airflow + semantic layer + CFA). It maps almost line for line.
- Source: LinkedIn (direct paste)
- Contract: Not stated (permanent expected)
- Location: London HQ, hybrid (3 days/week in office)
- Compensation: Not stated. London fintech AE salaries typically clear the Skilled Worker threshold, but confirm.
- Company: Checkout.com, global payments processor (eBay, Spotify, Klarna, Uber, Sony), 10bn+ transactions/year. A payments fintech, not a bank.

## UK work authorization (checked 2026-09-30, reference/check_sponsor.py, register 2026-09-29)
- Sponsor: CONFIRMED. "CHECKOUT LTD", London, Worker (A rating), Skilled Worker (+ Global Business Mobility). Ignore the unrelated Bradford/Wimbledon "Checkout" entities.
- Skilled Worker salary: £41,700 or the occupation going rate, whichever is higher (new-entrant rate if criteria met).
- Right-to-work form: "I currently do not have the right to work in the UK and would require company visa sponsorship."

## On "I" vs "2+ years"
- "I" is the entry rung of their AE ladder, but they still want some real AE/DE time. Your case: a 6-month graduation internship doing AE work on financial data (BNP) + substantial projects (pc_pipeline). It's under 2 years, but the content matches exactly, so present it as depth, not duration.
- Big fintechs often screen on keywords + relevance before years; a finance-data CV with dbt/Snowflake/DQ will pass more screens than the number suggests.

## Cover Letter Angle
Short. Their problem is keeping an accurate, auditable record of financial events at scale, with integrity and SLAs for Finance/Treasury. At BNP Paribas Securities Services you designed a financial-data model from scratch (declared grain, SCD Type 2 history, surrogate keys, staging-to-mart across three source systems) and a data-quality framework that catches duplicates, identity-resolution failures and cross-source inconsistencies. That's reconciliation thinking. pc_pipeline shows the stack (dbt on Snowflake, tests for 6 defect classes, Airflow with retries/idempotent reruns, semantic layer). As a CFA charterholder you speak Finance's language (settlement, FX, revenue recognition), which matters when translating their requirements into models and SLAs.

## Preparation Gaps
- Payments data: authorization → capture → settlement → payout; refunds/chargebacks; fees (interchange, scheme, processing); multi-currency/FX; merchant balances. Model a "merchant ledger/balance" fact and a settlement reconciliation.
- Ledger/double-entry concepts: immutability, append-only events, balance = sum of entries; reconciling internal ledger vs bank/scheme files.
- Monitoring/alerting for pipelines: freshness/volume/anomaly checks, SLAs, dbt source freshness, incident handling.
- Scale: incremental models, partitioning/clustering, idempotent backfills on hundreds of billions of events.
- Looker/Tableau basics (Power BI transfers).

## Stack Analysis

### Have
- Excellent SQL; dbt; Snowflake (cloud DW)
- Data modeling (dimensional, SCD2, grain)
- Data pipelines + reliability (Airflow retries/idempotency; dbt tests; BNP DQ framework)
- Finance/Treasury stakeholder translation (BNP, CFA)
- Software engineering practices (Git discipline, testing); Python (a plus)
- Visualization (Power BI, Streamlit)

### Missing
- 2+ years in an AE/DE role (internship + projects)
- Production monitoring/alerting at scale
- Looker/Tableau/Superset; Java/Flink (optional)

### Partial
- Data governance/security standards: concept + BNP exposure
- Large-scale transformation: project scale, not hundreds of billions of events

### Green Flags
- Financial data + Finance/Treasury stakeholders: your domain
- dbt + cloud DW + data modeling core; Python not required
- Ownership of data quality explicitly
- Licensed sponsor (A rating); big-fintech engineering standards

### Red Flags
- 2+ years AE/DE
- 3 days/week in office in London (relocation; restarts the French residency clock)
- Scale expectations (hundreds of billions of events)
- No age-discrimination wording

## Notes
- Verdict: APPLY. One of the strongest domain matches in London (payments finance data), zero tailoring, sponsor confirmed. Pairs with the Booking Treasury application: same CV, same story.

## Raw JD (abridged)
Checkout.com, Financial Infrastructure team: core systems for the internal financial ecosystem; hundreds of billions of financially impactful events/year; accurate record of financial data, data integrity, regulatory/compliance; scalable, reliable, fault-tolerant. Analytics Engineer: work with Finance and Treasury to translate requirements into robust data models; build pipelines; ensure accuracy/reliability; ownership of data quality.
Do: pipelines from systems/services/apps; monitoring and alerting; scalable data models with other AEs; data governance/security; evaluate new tech; translate Finance requirements into specs and SLAs.
Qualifications: 2+ years AE/DE (large-scale transformation, warehousing); excellent SQL; cloud DW (Snowflake, BigQuery, Redshift); dbt or Dataflow; data modeling; Looker/Tableau/Superset; SE best practices; Python/Java/Flink a plus; attention to detail; autonomy; communication.
Hybrid: 3 days/week in office.
