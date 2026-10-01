# Voodoo — Finance Data Engineer — 2026-09

## Metadata
- Date: 2026-09-30
- Status: To apply — existing CV, no tailored build (Kris's call: stretch role)
- Fit Score: Medium-Low — the domain and mission are a strong match (Finance migrating from spreadsheets to dbt/Airflow on AWS, reporting to the CFO), but it's a senior solo-owner role ("significant experience", "own the technical transformation", define the roadmap), plus Terraform/K8s/Athena/StarRocks gaps and a French-fluency requirement
- Source: LinkedIn
- Contract: unknown (likely CDI)
- Location: Paris, France

## Visa / Contract
- France, Passeport Talent salarié qualifié: needs a CDI or a 3-month+ CDD at or above the threshold (≈€39.6k per Parakar, ≈€43.8k if strictly 2× SMIC; confirm). A Paris Finance DE at a $1b-revenue company should clear it easily. No sponsor-register check is needed.

## CV Tailoring Instructions
- Decision: reuse an existing PDF, no tailored build.
- File: `output/cv_kris_huang_booking_holdings_data_analytics_engineer_i_treasury.pdf`
- Why this one: it's the finance-engineering version. The summary leads with finance domain depth, dbt on Snowflake, reconciliation checks over three source systems (the spreadsheet-to-code story), Airflow with idempotent reruns, an LLM agent over a semantic layer, and CFA. Its skills box already lists Airflow, PySpark (for Spark), Streamlit and Python, which lines up with Voodoo's stack.
- Runner-up: `cv_kris_huang_lendable_analytics_data_engineer_python_infrastructure.pdf` (more Python-tooling-forward, but weaker on the finance angle).
- Language: the JD is in English, so the English CV is fine. Don't use the French CV unless the application form asks for it.
- CFA: keep it in the summary (already the case). A CFO-reporting role values it directly.
- If it progresses (interview stage), a tailored build would add: "Claude Code" (on the Hellebore build already), an AWS mention, and a spreadsheet→code migration framing in the BNP bullets (the VBA/Excel deal-monitoring automation and the Power BI → pandas/openpyxl flow).

## Cover Letter Angle
At BNP Paribas I work exactly where Voodoo's Finance team is starting from: critical data maintained by hand in Excel across three source systems. I designed the dimensional model that replaces it (grain, SCD Type 2 client versioning, staging-to-mart), built the data-quality checks that surface identity and code mismatches before they reach reporting, and automated the deal-monitoring workbook commercial teams use every day. My portfolio project, pc_pipeline, is that same migration in code: dbt models with a test suite, Airflow orchestration and an LLM agent that answers only through validated metrics. As a CFA Charterholder I speak the Controlling and FP&A language on the other side, which is what a Finance-embedded engineer reporting to the CFO has to do daily.

## Preparation Gaps
- **French accounting basics (PCG):** plan comptable structure (classes 1–7), the grand livre / balance / FEC export, and how a GL feeds P&L and balance-sheet reporting. Expect "model our month-end close" style questions; know the grain of a journal-entry fact table and why FEC is the natural source.
- **Finance data modeling:** a GL fact at journal-line grain, chart-of-accounts hierarchy as a dimension, multi-entity and FX conversion (daily vs. closing rate), actuals-vs-budget for FP&A. Tie it to your SCD Type 2 experience (restated account mappings).
- **Mobile gaming revenue flows:** ad revenue (mediation networks, eCPM) and in-app purchases through app-store payouts with a lag and currency conversion. That's the reconciliation problem Finance will care about.
- **AWS data stack, concept level:** S3 + Athena (query on files, partitioning, cost per scanned byte), what StarRocks is for (fast OLAP serving), where dbt fits (dbt-athena), and why Terraform/K8s sit with the central Data team rather than a Finance DE.
- **Build vs. buy:** have a view on FP&A tools (Pigment, Anaplan) vs. in-house dbt + Streamlit, and when spreadsheets should stay.
- **MCP / Claude Code:** they use both internally. Be ready to describe how you direct coding agents daily, and what an MCP server over a finance semantic layer would expose.
- **French interview readiness:** the JD requires French with non-technical stakeholders. You're at B2, so rehearse the BNP story and pc_pipeline in French.

## Stack Analysis

### Have
- SQL (advanced), Python, dbt (models, tests, docs), Git
- Airflow (portfolio DAG: retries, idempotency)
- Spark via PySpark (TripAdvisor, 1M+ records)
- Streamlit (on the Booking/Lendable/Hellebore builds)
- Data quality and testing standards; migrating spreadsheet workflows to code (BNP)
- LLM agent over a semantic layer; daily use of Claude Code
- Finance domain depth (CFA, credit analysis, private-capital data)

### Missing
- Terraform, Kubernetes
- Athena, StarRocks
- Scala
- French accounting principles (PCG) in practice
- Production ownership of a data platform ("significant experience")

### Partial
- AWS (familiar level; DEA-C01 in progress)
- French: B2 (the JD requires working in French and English)
- Dashboards/internal apps: Power BI in production at BNP; Streamlit at portfolio level
- AI prototype → production: the agent exists in the portfolio, not in a production deployment

### Green Flags
- A clear, modern stack is named (dbt, Airflow, AWS, Streamlit, Claude Code/MCP)
- A specific problem: migrating Finance off spreadsheets into tested, documented code
- Testing, version control, observability and documentation are explicit requirements
- Reports to the CFO with a central Data team as partner: real ownership and engineering support
- Finance and accounting knowledge is valued, which plays to the CFA

### Red Flags
- Seniority: "significant experience" plus owning the roadmap reads mid/senior as the first dedicated Finance DE hire
- A solo role embedded in Finance: there's a risk of drifting into BI/support ("training, day-to-day support")
- Terraform and Kubernetes are listed, though likely owned by the central team

## Raw JD
About Voodoo — Voodoo is a consumer tech company founded in Paris in 2013, with one mission: entertain the world. 1,000 people, $1b+ annual revenue, profitably. 7 billion+ downloads, 200 million+ monthly active users; #3 mobile publisher worldwide in downloads. Backed by Goldman Sachs, Tencent and GBL.

Team — Corporate (HR, Legal, Finance). Finance is moving from fragmented, spreadsheet-heavy workflows to a modern, reliable, increasingly automated Finance data platform.

Role — Finance Data Engineer, reporting to the CFO, working with Finance stakeholders and the central Data team.
- Define and drive the roadmap for Finance data, automation, and internal tooling
- Build and progressively scale Voodoo's Finance data platform, prioritising the highest-value use cases
- Migrate critical data transformations and workflows from spreadsheets and legacy tools to tested, documented, code-based solutions
- Create reliable data models and pipelines for Finance reporting, analysis, forecasting, and operational processes
- Establish standards for data quality, observability, documentation, security, and access management
- Partner with Accounting, FP&A, Controlling, Treasury and other Finance stakeholders
- Collaborate with Data leadership and engineering teams on architecture, tooling, and best practices
- Build dashboards and internal applications for Finance self-service
- Identify AI and automation opportunities, take them from prototype to production, and measure value
- Help Finance teams adopt data and AI tools through documentation, training, and support

Profile
- Significant experience in data engineering, analytics engineering or similar, including ownership of production-grade data solutions
- Proven track record of building or substantially improving a modern data platform or analytics stack
- Highly proficient in SQL; comfortable building production systems in Python
- Strong software-engineering practices: testing, version control, code review, documentation, monitoring
- Solid understanding of corporate Finance and accounting; French accounting principles a strong advantage
- Translate ambiguous business needs into pragmatic technical solutions
- Autonomous, prioritises competing needs, delivers incrementally
- Strong communication with technical and non-technical stakeholders, in French and English
- Curious about the data and AI ecosystem
- Rigorous, detail-oriented, pragmatic about build / open-source / buy

Nice to have: tools or data products for Finance teams; AI agents or AI-enabled workflows in production; mobile gaming / consumer apps / advertising / digital analytics; data infrastructure on AWS.

Stack: AWS; Python, SQL, Scala; dbt, Airflow, Spark; Athena, StarRocks; Terraform, Kubernetes; Streamlit; Claude Code, MCP-based internal tooling.

Benefits: competitive salary, Swile, Gymlib, SideCare healthcare, wellness activities, remote Fridays.
