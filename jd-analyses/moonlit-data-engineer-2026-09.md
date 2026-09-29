# Moonlit — Data Engineer — Amsterdam — 2026-09

## Metadata
- Status: APPLYING (low priority, zero tailoring). NOT an IND recognised sponsor (checked 2026-09-29), so only the orientation-year (zoekjaar) route would work.
- Date: 2026-09-29 (LinkedIn "job match": Low)
- Fit Score: Medium-Low. The gate is open (1–3 years) and you hold the core: Python + PySpark at scale (TripAdvisor 1M+), SQL + data modeling, data-quality/freshness monitoring, messy semi-structured data, RAG/semantic-search exposure. But the job's centre of gravity is a document-ingestion + search DE role (scraping/parsing HTML/XML/PDF, Databricks, Elasticsearch, vector DB, Azure infra), not analytics engineering. No dbt, no warehouse modeling, Azure-managed infra.
- Tailoring effort: ZERO. Reuse the NL GenAI CV (`output/cv_kris_huang_undisclosed_nl_data_analytics_engineer_ii_genai.pdf`, once built). Its summary (LLM eval + RAG + PySpark 1M+ + data quality) is the right angle here too.
- Source: LinkedIn (direct paste)
- Contract: Full-time, likely permanent; equity package
- Location: Amsterdam HQ, IN OFFICE (full-time on site)
- Company: Moonlit, a legal-tech publisher / scale-up: Europe's largest legal database, served via platform, API and MCP server to legal professionals and legal-AI products.

## Why LinkedIn says "Low"
- LinkedIn's match is keyword overlap between your profile and the JD. The JD's distinctive keywords (Databricks, Elasticsearch, Turbopuffer, Azure, scraping, XML/PDF parsing) aren't on your profile. Your strengths (dbt, Snowflake, dimensional modeling, CFA/private capital) aren't in the JD.
- So it's partly right, for the wrong reason: you're not unqualified (the gate is 1–3 years, and PySpark/Python/SQL/DQ match), but the role is off your AE lane. Don't treat LinkedIn's score as a verdict; it ignores seniority fit and project evidence.

## Before applying
- IND sponsor check (2026-09-29): Moonlit is NOT on the IND recognised-sponsor register, so it can't sponsor a Highly Skilled Migrant permit directly. The only route is the orientation-year permit (zoekjaar hoogopgeleiden), which lets you work without a sponsor; switching to HSM later would need a recognised-sponsor employer, or Moonlit applying for recognition.
- In-office Amsterdam = relocation; same French-residency trade-off as Marktlink.

## CV Tailoring Instructions
Variant: B, AI/analytics-forward, ENGLISH. No new build: send the NL GenAI PDF.
If you want a Moonlit-specific version (optional, via Claude Code on `variant-b-general`): same summary but swap the last sentence for "Data-quality, freshness and coverage monitoring over heterogeneous sources at BNP Paribas." Export `output/cv_kris_huang_moonlit_data_engineer.pdf`. Not worth it unless you get a response.

## Cover Letter Angle
Legal AI is only as good as its document layer: structure, references between documents, versioning, freshness. You've built both ends: a RAG chatbot with LLM-as-judge evaluation (LVMH), where retrieval quality depended entirely on how the source data was structured, and a data-quality framework that catches duplicates, identity-resolution failures and cross-source inconsistencies (BNP) — the same failure modes as duplicate or mis-versioned legal documents across sources. PySpark at 1M+ semi-structured records (TripAdvisor) shows the processing side. Mention that you build with MCP-aware tools (Claude Code) and understand why an MCP server needs clean, well-referenced data behind it.

## Preparation Gaps
- Document ingestion: scraping etiquette/robustness, HTML/XML parsing (lxml, XPath), PDF extraction (pdfplumber/OCR limits), normalization into a canonical schema.
- Legislation versioning: effective-dated versions, amendments, consolidated texts. Map it to SCD Type 2, which you know.
- Elasticsearch basics: mappings, analyzers, reindexing with aliases, relevance tuning; hybrid lexical + vector search (Turbopuffer).
- Databricks: Delta Lake, jobs/workflows, Unity Catalog at concept level.
- Azure: storage, ADF/Databricks on Azure. Not held (a known gap).

## Stack Analysis

### Have
- Python, PySpark, large-scale processing (TripAdvisor 1M+)
- SQL + data modeling (dimensional, SCD2 → versioning)
- Data quality / freshness / coverage monitoring (BNP DQ framework, dbt tests incl. freshness)
- Messy semi-structured/unstructured data; RAG/semantic search (LVMH)
- Cloud: AWS familiar (they accept any major cloud)
- ETL pipelines + orchestration (Airflow)

### Missing
- Databricks, Elasticsearch, Turbopuffer
- Azure infrastructure management
- Scraping/parsing HTML/XML/PDF at production scale

### Partial
- Vector/semantic search: RAG built, no search-index ops
- Cloud: AWS familiar only

### Green Flags
- Junior-friendly gate (1–3 years)
- Mission-driven, AI-adjacent (semantic search, AI assistants, MCP server)
- Clear ownership: source → searchable, enriched document
- Pragmatic, quality-first culture; equity

### Red Flags
- Off-lane: document-ingestion/search DE, no dbt/warehouse modeling
- Azure-managed infra (known gap)
- Full in-office in Amsterdam; relocation + residency-clock trade-off
- Not an IND recognised sponsor (orientation-year route only)
- No age-discrimination wording

## Notes
- Verdict: optional, low-priority. Apply only because it costs nothing (reuse the GenAI PDF) and the junior gate is real. Don't spend prep time until they respond. Rank it below Marktlink and the GenAI analytics role for NL.

## Raw JD (abridged)
Moonlit, legal publisher, Amsterdam HQ; platform, API and MCP server; Europe's largest legal database for semantic search and legal AI. Data Engineer, in office, full-time, 1–3 years.
Do: ETL with Python, PySpark, Databricks; add legal data sources (scraping, parsing, normalizing HTML/XML/PDF); enrich/structure datasets (metadata, cross-document references, legislation versioning); maintain/optimize Elasticsearch indexes; monitor data quality, freshness, coverage; improve performance/reliability/cost; manage Azure data infra; collaborate with platform devs, AI engineers, legal experts, business.
Ownership: end-to-end source → searchable enriched document; production-grade (tested, monitored, scalable); go-to person for data structure/provenance.
Stack: Python, PySpark, Databricks; Elasticsearch, Turbopuffer, Azure SQL; Azure, AWS, GCP.
Profile: 1–3 years DE or related; strong Python + PySpark, large-scale processing; solid SQL + data modeling; hands-on with one major cloud; ETL/transformation workflows; comfortable with messy unstructured data; Databricks/Elasticsearch a plus; pragmatic.
Offer: competitive salary + equity, office with garden, international mission-driven environment.
