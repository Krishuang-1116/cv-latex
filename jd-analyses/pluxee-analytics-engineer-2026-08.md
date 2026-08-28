# Pluxee — Hub Analytics Engineer — 2026-08

## Metadata
- Date: 2026-08-28
- Fit Score: Medium — excellent modeling/transformation fit (dimensional modeling, SCD, star schema, data quality = your pc_pipeline wheelhouse) AND hands-on PySpark (TripAdvisor project, 1M+ records). Gated mainly by the Azure-native operational stack (ADF/Azure DevOps) you don't yet touch and a "2 years ETL/ELT" requirement against intern status.
- Source: Direct paste (LinkedIn/company site)
- Contract: Full-time, hybrid — CDD/CDI unstated, almost certainly CDI (permanent role, 2-yr experience ask)
- Location: France (Pluxee HQ: Issy-les-Moulineaux / Greater Paris) — confirm exact office

## CV Tailoring Instructions
Variant: B (General Modern Stack)
Branch: variant-b-general
Summary line (English): "Analytics Engineer building end-to-end, tested data pipelines — dbt/SQL transformation, dimensional modeling (star schema, SCD), and Power BI reporting — with a rare domain foundation in financial data and a CFA charter."
Summary line (French): French CV not yet available — placeholder: "Analytics Engineer, je construis des pipelines de données de bout en bout, testés et documentés — transformation dbt/SQL, modélisation dimensionnelle (star schema, SCD) et reporting Power BI — avec une solide culture de la donnée financière (CFA)."
Skills reorder: Lead with Transformation (dbt, SQL) → Data Modeling (dimensional, star schema, SCD) → Warehousing → BI/Semantic (Power BI/DAX) → Domain. Surface Power BI, SCD, and star schema explicitly by name — the JD names all three.
CFA positioning: Experience section (Tier 2-style company, not private-capital infra). Do NOT put CFA in the summary as the lead; keep it as a closing signal only.
BNP entry: Add — current AE-adjacent work; frame as data/reporting infrastructure, not finance advisory.

## Cover Letter Angle
Pluxee sits on a B2B2C ecosystem — 500,000+ clients, 37M+ consumers, 1.7M+ merchants — which means the analytics engineering challenge is fundamentally about reconciling multi-domain transactional data (meal/food, well-being, rewards, public benefits) into reusable, trustworthy models across many business teams. That is precisely the problem your pc_pipeline project rehearses at a smaller scale: synthetic data seeded with six real-world defect classes, run through a staging → intermediate → mart dbt architecture with a generic + custom singular test suite specifically so that downstream marts are trustworthy before anyone builds a dashboard on them. Tie your line to their phrase "discovering, modeling, and delivering high-quality, reusable data assets" — say that data-quality auditing (checking aggregations, verifying relationship integrity, managing inconsistencies) is not an afterthought in how you build but the reason your marts exist.

## Preparation Gaps
- **Azure ecosystem is the decisive gap.** The role is Azure-native end to end: Azure Data Factory (pipelines/orchestration), Azure DevOps (CI/CD, branches, PRs, test environments), Azure Boards (agile tracking), and generic "understand each Azure resource." You have none of this hands-on. Before interviewing: spin up a free Azure account, build one small ADF pipeline (copy activity + a data flow) so you can speak to the pipeline/dataset/linked-service/trigger model, and map ADF concepts onto the Airflow/Dagster DAG mental model you already have. You can honestly say "I orchestrate via dbt + DAG principles and am transferring that to ADF."
- **PySpark — you have this; sharpen the framing.** Your TripAdvisor project (PySpark ETL pipeline, 1M+ semi-structured records, large-scale validation) already satisfies the "distributed computation with Spark" line — lead with it. Before interviewing, be ready to go one level deeper than the CV bullet: partitioning, lazy evaluation, wide vs narrow transforms, and why Spark over a single-node run at that record volume. This is a strength to surface, not a gap.
- **SCD and Data Vault — turn conceptual into demonstrable.** You know these patterns; the JD calls them out by name. Be ready to whiteboard an SCD Type 2 (effective/expiry dates, surrogate keys, current-flag) and articulate when Data Vault beats a plain star schema (auditability, source-system flexibility, historization). Your pc_pipeline marts give you a concrete example to anchor this.
- **NoSQL + REST/OAuth backend.** JD lists NoSQL databases and REST API (OAuth, Swagger, backend services). Your FastAPI work is the hook — extend it to expose one authenticated endpoint (OAuth2 bearer flow + a Swagger/OpenAPI spec) so this stops being theoretical.
- **Table physical design.** JD emphasizes distribution and indexing choices for performance — a warehouse-engineering concern (think Synapse-style distribution keys). Read up on distribution strategies (hash vs round-robin vs replicated) and when each applies; you can currently speak to logical modeling but not physical distribution.
- **Real/near-real-time.** JD wants batch-to-streaming latencies. Be able to articulate the architectural difference (batch snapshot vs event/stream) and when a periodic snapshot is insufficient — even at concept level this reads as maturity.

## Stack Analysis

### Have
- Strong SQL: CTEs, window functions, subqueries (JD: "strong SQL, querying and procedures")
- Dimensional / relational data modeling; star schema (JD names it directly)
- Data quality & testing discipline: dbt generic + custom singular tests, aggregation/integrity auditing (JD emphasizes this heavily)
- Power BI: DAX, Power Query (JD: "proficiency with Power BI")
- Python (JD: "at least one of C#, Python or PySpark" — Python satisfies it)
- PySpark — hands-on ETL: TripAdvisor Restaurant Analytics, PySpark pipeline over 1M+ semi-structured records with large-scale validation (JD: "distributed computation with Spark", "PySpark")
- Git version control; comfort reading/reverse-engineering others' code
- Documentation-first pipeline habits (JD: "documented, easy to maintain, traceability")
- Python-applied-to-ML awareness (JD "plus" section) — enough to be conversant

### Missing
- Azure specifically: Azure Data Factory, Azure DevOps, Azure Boards, Azure resource architecture (Snowflake incoming is NOT Azure)
- 2 years professional ETL/ELT experience (you're a graduating intern)
- NoSQL databases — hands-on
- REST API backend with OAuth/Swagger — beyond basic FastAPI
- C# (not required — Python covers the "at least one language" clause)
- Physical table design: distribution/indexing strategy for performance
- Real/near-real-time (streaming) pipeline implementation

### Partial
- CI/CD & DevOps: Git basics yes; Azure DevOps branches/PRs/test-envs workflow not yet
- Orchestration: DAG principles via Airflow/Dagster concepts + dbt — transferable to ADF but not on ADF
- SCD / Data Vault: know the patterns; need to demonstrate implementation
- REST API: FastAPI basic in progress — partial toward OAuth/Swagger/backend
- Cloud computing (storage, serverless, API): Snowflake trial incoming gives cloud-warehouse footing, but role wants Azure PaaS specifically
- Agile/international transversal work: BNP internship gives some; not "2 years in an agile org"

### Green Flags
- True AE role — "perfect fusion of Data Analyst and Data Engineer," end-to-end ownership from ingestion to reporting
- Owns real engineering decisions: pipeline design, distribution/indexing choices, SCD/Data Vault pattern selection
- Transformation and modeling layer is central, not incidental
- Specific, concrete stack named (not vague) — ADF, PySpark, SQL/NoSQL, Power BI, Azure DevOps
- Clear AE/DE vs pure-analyst distinction
- Data quality / auditing given real weight — matches your testing-first approach
- Not a traditional bank/FI — B2B2C benefits fintech, product-and-infrastructure component present
- No age-discriminatory or vague-buzzword language

### Red Flags
- **Experience gate:** "At least 2 years building and managing ETL and ELT processes." This is a permanent, mid-level role, not a junior/grad posting — the biggest structural mismatch. Worth applying if you can frame the internship + pc_pipeline as equivalent depth, but calibrate expectations.
- **Azure lock-in:** the entire operational stack is Azure-native; your transferable-but-not-hands-on position is a genuine gap an interviewer will probe.
- Minor: role is business-embedded with broad scope (analyst + engineer + platform user + DS-plus) — well-defined here, but confirm in interview that engineering depth won't get diluted into reporting work.

---

## Country / Visa Note
France (primary target — aligns with your residency-timeline preference). If you pursue this, confirm the current Passeport Talent minimum annual gross salary threshold before negotiating — it changes yearly; do not assume last year's figure. A permanent mid-level AE role at a company this size should clear it comfortably, but verify the exact current number.

## French CV Flag
Pluxee is French-headquartered. Even though this JD is in English, a French CV is standard for a France-based role at a French company. **French CV needed** — use the French placeholder summary above until the French CV is created.

---

## Raw JD

Pluxee is a global player in Employee Benefits and Engagement that operates in 28 countries. Pluxee helps companies attract, engage, and retain talent thanks to a broad range of solutions across Meal & Food, Well-being, Lifestyle, Reward & Recognition, and Public Benefits.

Powered by leading technology and more than 5,600 engaged team members, Pluxee acts as a trusted partner within a highly interconnected B2B2C ecosystem made up of more than 500,000 clients, 37 million+ consumers and 1.7 million+ merchants.

Conducting business for more than 45 years, Pluxee is committed to creating a positive impact on local communities, supporting well-being at work for employees, and protecting the planet.

Reporting to the Hub Lead Data Engineer, the Hub Analytics Engineer is a member of the Hub Data Analytics team. Perfect fusion of the Data Analyst and the Data Engineer, passionate about data and capable of handling end-to-end projects, he/she is responsible for the entire data lifecycle, from ingestion to reporting and analysis. With dual technical and business skills, the Analytics Engineer plays a crucial role in understanding business requirements, designing optimized data flows, and delivering robust and high-performance analytical model to improve commercial strategies and decision-making on multi-domain projects.

The Analytics Engineer is key in Pluxee's Data & AI Transformation by acting as the bridge between raw data and business value. The Analytics Engineer is responsible for discovering, modeling, and delivering high-quality, reusable data assets that enable dashboards, self-service analytics, and AI applications across the organization.

Mission & Responsibilities

Expert in Design and Management of Data flows
- Develop and maintain robust, cost efficient, high-performance data pipelines, end-to-end, mixing several technologies like Azure Data Factory pipelines, Pyspark, Python, Rest API, SQL & NoSQL databases, batch and files… with different latencies (from batch to Realtime)
- Orchestrate jobs following DAG principles
- Ensure that data flows are reliable, documented, and easy to maintain
- Design optimized tables (choosing the right distribution, indexing types) to ensure maximum performance
- Implement proven patterns such as Slowly Changing Dimensions (SCD) or Data Vault to address needs related to data historization or flexibility
- Adopt established designs like Star Schema or relational models to facilitate analysis and reporting
- Document transformations and models comprehensively to ensure traceability and understanding by stakeholders
- Proficiency with Business Intelligence tools (Power BI) to ensure consistency between models and reporting

Data Analyst closely embedded with Business teams:
- Actively participate in discussions with business teams to understand their specific data needs and decision-making processes
- Translate these requirements into concrete solutions, ensuring that the models delivered meet business objectives
- Conduct thorough data exploration to understand the relationships between different tables and identify relevant data sources to design data model structured correctly to support business goals
- Validate data quality and consistency against the provided business information by testing and auditing data to ensure it meets business rules and expectations for reliability: checking aggregations, verifying the integrity of table relationships, and managing errors or inconsistencies
- Facilitator in the iterative process of developing data flows to ensure that business expectations are clearly understood throughout the design process, adjusting models or data processes based on continuous feedback from business teams

Data Analytics Platform User:
- Understand the data platform architecture and the purpose of each Azure resources
- Ensure compliance with data protection law (PII encryption)
- Monitor data ingestion jobs
- Develop, test, and deploy code and jobs within a DevOps framework, expertly managing branches, pull requests, and test environments
- Collaborate with other Analytics Engineers and Data Engineers and follow the guidelines set by the Hub team, ensuring alignment with our highest standards and best practices
- Capacity to read and understand code developed by other members to allow maintenance and evolution (reverse-engineering)
- Maintain and update project boards with accurate, up-to-date information, providing a clear view of project development progress and milestones

Data Science skills (as a plus):
- Proficiency in Python or R for advanced data analysis and modelling
- Experience in developing and deploying predictive models (e.g., regression, classification, time series forecasting) to address business challenges
- Knowledge of statistical methods for data analysis, hypothesis testing, A/B testing, and understanding of concepts such as p-values, confidence intervals, and model evaluation metrics
- Familiarity with neural networks and deep learning techniques (if applicable) to solve more complex business problems

Profile, Experience & key Competencies
- Master's degree in computer science/data engineering/statistical engineering/information processing or equivalent
- At least 2 years building and managing ETL and ELT processes
- Strong SQL skills: querying and procedures
- Advanced knowledge of relational and dimensional database management (indexing, distribution choices)
- At least one of the following languages: C#, Python or PySpark
- Data modelling for Analytical purposes
- Data modelling for OLTP databases
- Cloud computing: storage, serverless, API … (Azure is a plus)
- Distributed computation with Spark
- Good understanding of python applied to Machine Learning
- Devops principles with CI/CD (azure devops) and infrastructure as code
- Rest API: Oauth, Swaggers, backend services
- Real or near real-time data process design and implementation
- Advanced knowledge of data lake and data warehouse for analytical and operational purposes
- Experience in working transversally in an international company and in an agile organization
- Agile Project Management Knowledge (tracking on Azure Boards)
- Good understanding of company business
- Ability to understand business needs and co-build solutions that meet those needs
- Excellent communication skills, especially with non-technical stakeholders
- Curiosity and proactive problem-solving approach
- Fluency in English is required
- Ability to work autonomously
- Team spirit and engagement in projects

Working Conditions: Full-time. Hybrid: on site and work from home.
