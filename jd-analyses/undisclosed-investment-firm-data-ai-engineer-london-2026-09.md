# Undisclosed (recruiter) — Data & AI Engineer (greenfield), global investment firm — London — 2026-09

## Metadata
- Status: TO APPLY (recruiter says "get in touch"; no CV needed up front. Message the recruiter, attach a CV anyway)
- Date: 2026-09-30
- Fit Score: MEDIUM-HIGH. Greenfield DE + applied AI next to a Lead Data & AI Engineer. Interviews with the CTO and investment partners, "prior financial experience useful": your CFA + private-capital domain + pc_pipeline (pipeline + LLM agent) fit that combination unusually well. Pitched as a "second role", so they expect ~1–3 years of production work; you have an internship + projects. Gaps: Azure/Databricks, APIs, CI/CD maturity.
- Tailoring effort: NONE. Use the McKinsey build (DE + data foundations for AI, CFA kept), same as the Canary Wharf markets role.
- Source: LinkedIn (recruiter post, employer undisclosed)
- Contract: Not stated (permanent implied: bonus, pension, benefits)
- Location: London, hybrid
- Compensation: Not stated ("package reflects..."); bonus, 25 days, pension matched up to 10%, private medical
- Company: Undisclosed "global firm that puts technology at the centre"; "investment partners" suggests a PE/VC/investment firm, possibly private markets (a core target area).

## UK work authorization
- Sponsor: UNKNOWN. Ask the recruiter first: "Does the client hold a UK Skilled Worker sponsor licence and sponsor for this role?" Once named, grep `reference/uk-licensed-sponsors.csv`.
- Salary must clear £41,700 or the going rate. The benefits suggest it will, if they sponsor.

## CV Tailoring Instructions
No new build. Send the McKinsey Data Engineer I PDF (locate the sent copy; it is NOT in `output/`. Otherwise have Claude Code rebuild it from the commented McKinsey summary in `resume_base.tex`). Neutral filename.
If the recruiter names a private-markets firm, consider a Variant A summary (private capital first) before the CTO/partner interviews.

## Recruiter message (draft)
See chat.

## Cover Letter Angle
A greenfield data + AI build inside an investment firm is exactly what pc_pipeline rehearses. I designed a private-capital deal pipeline from raw sources to tested marts, then put an LLM agent on top that answers questions only through governed metrics. At BNP Paribas I do the same on real, messy private-capital data. As a CFA Charterholder I can talk to investment partners in their language, which matters when they're the ones consuming the data and interviewing you.

## Preparation Gaps
- Azure data stack: ADLS Gen2, Data Factory, Databricks on Azure, Unity Catalog; Delta Lake basics (medallion, MERGE, time travel).
- APIs: consuming vendor APIs (pagination, rate limits, auth) and exposing data via a small FastAPI service.
- Automated testing + CI/CD: pytest for pipeline code, dbt tests in CI (GitHub Actions / Azure DevOps), environments.
- Applied AI at an investment firm: RAG over deal documents/CIMs, extraction from PDFs, eval (your LVMH LLM-as-judge story), data security/confidentiality.
- Greenfield judgement: how you'd sequence a data platform from zero (sources → ingestion → warehouse/lakehouse → models → AI use cases), build vs buy.
- Investment-partner conversation: fund structures, deal flow, portfolio monitoring KPIs (your private-capital strength).

## Stack Analysis

### Have
- Python, SQL; Git; pipelines (dbt/Airflow on Snowflake, pc_pipeline); LLM agent + RAG/eval (applied AI)
- Financial domain: CFA, private capital (BNP), PE products (Guosen), credit (UOB)

### Missing
- Azure / Databricks hands-on
- Production pipeline ownership over years

### Partial
- APIs (light), automated testing (dbt tests; pytest limited), CI/CD (planned slim CI)

### Green Flags
- Greenfield, real ownership, a Lead to learn from; DE + applied AI blend
- Financial experience explicitly valued; meets CTO + investment partners
- Strong benefits (pension match to 10%)

### Red Flags
- Recruiter post: employer, salary and sponsorship unknown
- "Second role": prior production experience expected
- Azure/Databricks lean

## Notes
- Verdict: APPLY (message the recruiter today). Potentially a target-type employer (investment firm + data/AI). Qualify sponsorship first.

## Raw JD (abridged)
Greenfield Data & AI Engineer at a global, technology-centred firm; shape data platforms, analytical tooling and applied AI; work with the Lead Data and AI Engineer. Needs strong Python and SQL, production data pipelines, cloud exposure (Azure or Databricks), Git, APIs, automated testing, CI/CD. "Great second role." Bonus, 25 days, pension matched to 10%, private medical, gym, life insurance, cycle to work. Process: CTO, investment partners, data engineering lead; prior financial experience useful. Hybrid, London. "No up-to-date CV required."
