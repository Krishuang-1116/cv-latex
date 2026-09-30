# Marktlink Capital — Analytics Engineer (greenfield platform) — Amsterdam — 2026-09

## Metadata
- Status: REJECTED 2026-09-30 (Bart Schuil, Recruitment & HR Ops): location-based, prioritizing candidates already in NL; invited to reapply if relocating. Reply drafted confirming relocation at own initiative (sent).
- Date: 2026-09-29
- Fit Score: Medium. Best domain + stack match of the whole search: a PE/VC fund manager building a Fivetran → Snowflake → dbt platform from an empty account, integrating CRM (DealCloud/HubSpot), fund administration, portfolio monitoring and investor systems. That's pc_pipeline and your BNP private-capital model almost word for word, plus CFA, Streamlit/Power BI and Claude Code. It's held back by a hard seniority ask: 5+ years, prior "from scratch" platform build, sole owner of the architecture.
- Tailoring effort: LOW–MEDIUM (Variant A: summary swap + skills-column reorder).
- Source: LinkedIn (direct paste)
- Contract: Not stated (permanent expected); competitive salary + bonus + fund co-investment
- Location: Amsterdam (CitySide), office-based
- Company: Marktlink Capital, ~70 people, €3.5bn commitments, ~2,750 investors, 150+ PE/VC funds; a fund-access platform (feeder/fund-of-funds style). Growing via acquisitions ("integrating additional businesses"). Not a bank; squarely private markets.

## Netherlands work authorization (check before investing time)
- Your path (from earlier research): the orientation-year permit (zoekjaar hoogopgeleiden) lets you work for any employer without a sponsor, and you can switch to Highly Skilled Migrant at the reduced graduate salary threshold. Eligibility isn't the barrier; it's a strategy choice vs. staying in France for the residency clock.
- Sponsor check (2026-09-29, via indsponsors.nl, a third-party mirror of the IND register): "Marktlink Capital Management Coöperatief U.A." (KvK 80340180) is listed as an IND Recognised Sponsor. To do: confirm on the official IND public register (ind.nl, recognised sponsors → highly skilled migrants), and confirm in the process that this entity is the employing one (the hiring contract could sit in a different Marktlink entity).
- 2026 HSM salary thresholds (per the same site): €3,122/mo after a zoekjaar, €4,357/mo under 30, €5,942/mo 30+. An AE salary at a PE firm should clear the post-zoekjaar threshold comfortably.
- Moving to NL restarts the French residency timeline. Decide how much a top-domain role outweighs that before you interview.

## CV Tailoring Instructions (for Claude Code)
Variant: A (Financial Data Infrastructure). ENGLISH CV.
Branch: `variant-a-finance` (edit `resume_base.tex`). Follow `CLAUDE.md`: comment-don't-delete, one page, no geometry/font changes, don't commit.
1. Summary: comment out the current active summary (canonical line), add a `% Marktlink Capital (AE, Amsterdam) —` label comment, then set as the active text:
   "Analytics Engineer with private capital domain depth: designed a dimensional model for a private capital deal pipeline at BNP Paribas Securities Services (three source systems, SCD Type 2, data-quality framework), and built pc\_pipeline on dbt, Snowflake and Airflow — tested models, a semantic layer and an LLM agent. \textbf{CFA Charterholder}."
   Must not exceed the current summary's line count. If it wraps an extra line, drop "and Airflow" → "dbt and Snowflake".
2. Skills (Variant A order): in the left paracol column, reorder to Modeling → Transformation → Warehousing (same three lines, just moved). Warehousing: put Snowflake first ("Snowflake, PostgreSQL, DuckDB").
3. Right column, only if neither line wraps: BI & Semantic → "Power BI (DAX), Streamlit, dbt Semantic Layer"; Programming → "Python, Git, Claude Code". Add Streamlit only if the pc_pipeline Streamlit app is real. Skip whichever wraps.
4. Rebuild with tectonic, confirm one page, export: `cp build/resume_base.pdf output/cv_kris_huang_marktlink_capital_analytics_engineer.pdf`.
CFA positioning: summary (domain evidence; PE/VC affinity is explicitly a plus).
Optional adds: none (Guosen secondary-PE product work would fit the domain, but costs a line; not worth the one-page risk).

## Cover Letter Angle
Lead with the domain match, because it's rare for this role and the thing a 5-years-of-generic-AE candidate won't have. At BNP Paribas Securities Services you designed the data model for a private-capital deal pipeline from scratch: declared the grain, versioned clients with SCD Type 2, and reconciled three manually maintained source systems, with a data-quality framework for identity-resolution failures, duplicates and cross-source code inconsistencies. That's exactly the problem of joining DealCloud, fund administration and portfolio-monitoring data into one set of trusted definitions. pc_pipeline shows the stack they're about to build: layered dbt models with tests covering 6 defect classes from real private-capital data patterns, a semantic layer with agreed metric definitions, Airflow orchestration, and an LLM agent on top (relevant to their AI Hub). You build with Claude Code daily. Be direct about seniority: you haven't had 5 years, but you have built this exact platform shape end to end on this exact domain, and the CFA means you can talk commitments, calls, distributions, NAV and TVPI/DPI with Investments and IR without translation.

## Preparation Gaps
- Fund data model: LP commitments, capital calls, distributions, NAV, unfunded commitment, TVPI/DPI/IRR, fund → vehicle → investor hierarchy, feeder structures. You know the finance (CFA); practise drawing it as dbt marts (grain per fact: cash flow event, NAV snapshot, commitment).
- Greenfield Snowflake setup: account/database/schema layout (raw/staging/marts), RBAC roles and warehouses per workload, environments (dev/prod, zero-copy clone), cost controls (auto-suspend, resource monitors). This is the "empty account" question they'll ask.
- Fivetran: connector vs custom pipeline trade-offs (API limits, unsupported sources like fund-admin PDFs/Excel), schema drift, incremental syncs, cost (MAR pricing).
- dbt engineering fundamentals: CI (slim CI, state:modified), dbt docs + exposures, source freshness tests, monitoring/alerting.
- DealCloud/HubSpot data shapes at concept level (entities, pipelines, activities).

## Stack Analysis

### Have
- Snowflake + dbt + SQL + Git (core stack)
- Private equity / private capital domain: BNP deal-pipeline model, CFA, pc_pipeline built on private-capital data patterns
- Multi-source business-system integration: BNP three-source reconciliation
- Tested, documented analytics layer with agreed metric definitions: dbt tests, MetricFlow semantic layer
- Dashboarding (tool-open): Power BI; Streamlit (pc_pipeline)
- Python; orchestration (Airflow)
- AI coding tools (Claude Code) + AI Hub fit (LLM agent, RAG)
- English (TOEFL 120)

### Missing
- 5+ years of experience; prior production greenfield platform ownership
- Fivetran hands-on
- CI/CD and monitoring owned in production
- DealCloud/HubSpot hands-on
- Dutch (not required; the JD is in English)

### Partial
- Architecture decisions: made solo in pc_pipeline (layering, testing, semantic layer), not in a company
- Stakeholder management with senior business users: BNP + LVMH client work

### Green Flags
- A genuine build role on Fivetran/Snowflake/dbt: your exact lane
- Private equity / VC fund manager: your target domain (private markets)
- Engineering fundamentals explicitly valued (version control, tests, CI/CD, docs, auditability)
- Tool-agnostic dashboarding (Streamlit counts)
- AI coding tools + internal AI Hub
- Compact team, high ownership; fund co-investment

### Red Flags
- 5+ years + "built from scratch" + sole architecture owner: a real seniority gate, not a soft one
- Single-AE setup: little senior technical mentorship for a junior
- Outside France: residency-clock trade-off; possible sponsor-registration issue
- No age-discrimination wording

## Notes
- Verdict: apply, with a targeted CV + a short direct note to the hiring manager / Head of Data & Technology on LinkedIn. The seniority gate makes odds modest, but this is the most on-thesis role in the whole search (private markets + greenfield dbt/Snowflake + AI). A domain-matched junior can beat generic seniors in a 70-person firm where the AE must talk to Investments and IR daily.
- If they won't go junior on this role, the note may still open a conversation about a later/junior hire as the platform grows ("integrating additional businesses").
- Also add Marktlink-type firms to the target list: PE/VC fund managers and fund platforms building first data teams. This is the Tier-1 thesis in a smaller, reachable form.

## Raw JD (abridged)
Marktlink Capital, PE/VC/Private Income fund manager, Amsterdam (CitySide). 70+ people, €3.5bn+ commitments, ~2,750 investors, 150+ PE & VC funds; growing internationally and integrating additional businesses.
Role: Analytics Engineer in Data & Technology; build the analytics platform from the ground up with Fivetran, Snowflake, dbt. Design/build ELT from CRM, fund administration, portfolio monitoring and investor systems; tested, documented analytics layer with clear ownership and agreed metric definitions; dashboards replacing manual reporting; engineering fundamentals (version control, testing, CI/CD, monitoring, docs; auditable); onboard new sources/entities; work with Investments, IR, Sales, Fund Management, Finance, Ops, HR; hands-on analysis; own platform architecture; optionally internal tools/automation and the internal AI Hub.
Profile: hands-on AE/DE/BI Engineer; 5+ years incl. building a data platform from scratch; strong SQL + dbt, Git/modern SE practices; cloud DW (Snowflake preferred; Databricks/BigQuery transfer); architecture decisions from an empty account; Fivetran + judgement on custom pipelines; dashboarding (Power BI, Streamlit, Tableau, Looker…); solid Python; AI coding tools (Claude Code, Codex, Cursor); CRM (DealCloud, HubSpot) + finance/ERP/fund-admin integration; ownership from loose question to documented product; prioritisation; senior stakeholder communication; PE/VC/finance affinity a plus.
Offer: competitive salary + bonus, unlimited holidays, fund participation, laptop/iPhone, learning + FD subscription, lunches, ski trip, Amsterdam office. Pre-employment screening.
