# Van Lanschot Kempen — Data Engineer (Finance & Risk Insights, DAQS) — 2026-10

## Metadata
- Date: 2026-10-01
- Status: To apply — reuse `cv_kris_huang_eng.pdf` (byte-identical to the Booking treasury build)
- Fit Score: Medium — an explicit 0–3 year band (a real junior opening), finance & risk data reporting to the CFO, private banking/investment-product affinity (CFA), and an AI-first mandate all fit. But the stack is Azure/Databricks/ADF/T-SQL, which is fully outside your experience, and it's a bank (private bank / wealth manager).
- Source: LinkedIn
- Contract: Permanent (assumed); €3,784–5,676 gross/month + 19.47% flexible budget (13th month + 8% holiday allowance)
- Location: Netherlands, not stated (HQ 's-Hertogenbosch; Kempen in Amsterdam). Confirm which office DAQS sits in.

## Visa / Contract
- **Van Lanschot Kempen N.V.** is on the IND recognised-sponsor register (KvK 16038212).
- HSM salary: even the bottom of the band (€3,784/mo excluding holiday allowance) clears the reduced post-study threshold (€3,122/mo, 2026). Ask them to place you high enough in the band if the standard threshold ever applies.
- Location questions: answer honestly (Paris, relocating at your own cost, available January 2027), as with Qogita.

## CV Tailoring Instructions
- Decision: reuse `output/cv_kris_huang_eng.pdf` (byte-identical copy of the Booking treasury build). It leads with finance-domain data engineering (reconciliation over three sources, grain, SCD Type 2), with CFA in the summary, Power BI + Streamlit for "interactive information products", PySpark (the closest thing to Databricks/Spark on the CV), and the LLM agent for "AI-first".
- Alternative if built: the Columbia Threadneedle Variant A build (Guosen restored) speaks more to "investment products", but the Booking one is the better finance/risk match.
- Don't add Azure, Databricks, ADF or T-SQL; they are not held.
- English CV (the JD asks for excellent English; no Dutch requirement).

## Cover Letter Angle
FRI turns financial and risk data into management information that controllers, risk managers and senior management can trust. That's the problem I work on at BNP Paribas Securities Services, where I designed a dimensional model for private-capital deal data across three source systems and built a data-quality framework that catches identity mismatches, duplicates and inconsistent codes before they reach reporting. In my portfolio project I took the same logic past dashboards: dbt models with tests on Snowflake, Airflow orchestration, and an LLM agent that answers business questions only through validated metrics, which is the "beyond traditional dashboards" approach your team describes. As a CFA Charterholder with experience monitoring 100+ private equity products and analysing corporate credit, I understand the investment and risk products behind the numbers, and I'd bring the Spark and pipeline patterns I know to Databricks and Azure quickly.

## Preparation Gaps
- **Databricks (biggest gap, closable fast):** use the Databricks Free Edition to port pc_pipeline's staging → mart layers to Delta Lake with a medallion layout (bronze/silver/gold), then try Delta Live Tables (DLT) expectations as the analogue of your dbt tests. Know Unity Catalog basics. Also consider the Databricks Data Engineer Associate certification (listed).
- **Azure, concept level:** ADF pipelines and linked services, ADLS Gen2, Key Vault, managed identities; serverless options (Azure Functions, Databricks serverless SQL). AZ-900 is a cheap, quick listed certification and signals intent.
- **T-SQL:** the differences from Postgres/Snowflake SQL (TOP vs LIMIT, MERGE syntax, CROSS APPLY, temp tables). It's a small step from your SQL.
- **Finance & risk MI:** regulatory reporting context for a Dutch bank (capital: CET1/RWA; liquidity: LCR/NSFR at concept level), P&L by business line, AUM and net new money for private banking. Your CFA covers most of it; refresh the terminology.
- **AI-first story:** the LLM agent over a semantic layer, why metrics must be governed before an LLM touches them (risk and controls framing for a bank).

## Stack Analysis

### Have
- Python, SQL (advanced)
- Data modeling (dimensional, SCD Type 2, grain), data quality across sources
- Dashboards/insight products: Power BI (DAX) at BNP; Streamlit
- AI technologies: LLM agent, RAG chatbot, LLM-as-judge evaluation (LVMH)
- Spark via PySpark
- Master's degree; CFA (private banking/investment-product affinity)

### Missing
- Microsoft Azure (ADF, ADLS), Databricks, Delta Lake/DLT
- T-SQL specifically
- Any of the listed certifications

### Partial
- Cloud/serverless: AWS familiar; DEA-C01 in progress (transferable concepts, wrong cloud)
- Private banking: adjacent via securities services, PE product monitoring and credit analysis

### Green Flags
- An explicit 0–3 year experience band: a junior role you meet on seniority
- Reports to the CFO; a finance & risk domain that uses the CFA
- AI-first, "beyond dashboards" mandate; learning budget, mentoring, hackathons
- A transparent salary band; IND recognised sponsor

### Red Flags
- A bank (private bank/wealth manager): against the original "no traditional banks" filter, though closer to the investment side (like Columbia Threadneedle) than retail banking
- Azure-centric stack (flagged as not held): ADF, Databricks, T-SQL
- Some reporting/MI weight ("interactive insights, visualizations")

## Raw JD
Data Engineer, Van Lanschot Kempen. DAQS department (Data, Analytics & Quant Solutions), Finance & Risk Insights (FRI) team. FRI works with financial and risk data so Finance, Risk and Control can deliver reliable management information. Databricks + Microsoft Azure; pipelines and information products for commercial, financial and risk management processes; interactive visualizations, data products, AI-driven solutions.

Responsibilities
- Develop and maintain scalable data pipelines using Azure Data Factory, Delta Lake, Databricks DLT and workflows
- Enable stakeholders through interactive insights, visualizations, data products and AI-driven applications
- Collaborate with business stakeholders, data providers and platform teams
- Present and advocate data-driven solutions to decision-makers
- Evaluate and apply new technologies and AI capabilities
- Root-cause complex problems

Profile: AI-first, innovation-driven; Master's degree; 0–3 years in data modelling, data engineering and insights for end users; dashboards/visualizations/analytical apps; affinity with Private Banking and investment products; cloud (serverless, scalable); Python, Databricks, T-SQL, Microsoft Azure; analytical skills; experience with AI technologies; excellent English.

Preferred certifications: Databricks Data Engineer; AZ-900; DP-203; DP-100; DP-080; PSM I; PL-300.

About: 300+ years, ~2,300 colleagues, wealth management. DAQS is in the Finance domain and reports to the CFO; teams FRI, Commercial Insights, Quant/Efficiency & Data (QED).

Offer: €3,784–€5,676 gross/month; flexible budget 19.47% (13th month, 8% holiday allowance, 7 extra leave days); 27 vacation days; commuting reimbursement; pension (~20% employer); flexible hybrid; childcare budget; L&D. Recruiter: Minne van der Zaag (m.vanderzaag@vanlanschotkempen.com).
