# Multiverse — Analytics Engineer — 2026-09

## Metadata
- Status: APPLIED 2026-09-30 ("Why Multiverse?" answered: semantic layer for AI agents + upskilling mission)
- Date: 2026-09-30
- Fit Score: HIGH. dbt + Kimball (facts, dims, SCDs) + dbt tests/docs + a semantic layer built for AI agents over MCP + AI-assisted development as the normal workflow. That covers pc_pipeline (star schema, SCD2, dbt tests, dbt Semantic Layer + LLM agent) and the way you build (Claude Code). Snowflake/Airflow/semantic layer/CI are all "desirable", and you have them. No year gate stated. Main gap: "production dbt" (your dbt is portfolio; BNP modelling was done without dbt).
- Tailoring effort: LOW–MEDIUM. The OpenTable build is NOT the right one (see below). A new summary + one skills line.
- Source: LinkedIn (direct paste)
- Contract: Not stated (permanent expected)
- Location: London, hybrid (3 days/week in office)
- Compensation: Not stated
- Company: Multiverse, AI/tech upskilling apprenticeships (EdTech, ~800 staff, $2.1bn valuation after Apr 2026 round). Reports to Director of Data Engineering, Data & Insight team.

## UK work authorization (checked 2026-09-30, grep on reference/uk-licensed-sponsors.csv, register 2026-09-29)
- Sponsor: CONFIRMED. "Multiverse Group Limited", London, Worker (A rating), Skilled Worker. Confirm it is the employing entity.
- Salary must clear the Skilled Worker threshold (£41,700 or going rate). Confirm early.
- Right-to-work form: "I currently do not have the right to work in the UK and would require company visa sponsorship."
- A Basic DBS check is required for all hires (safeguarding). Routine, but they may also ask for overseas criminal-record certificates.

## Why not the OpenTable CV
The OpenTable summary (committed as 7efa909, never exported to a PDF) is built around BI + applied AI: "Data and BI engineer", RAG chatbot, dashboards. Multiverse is a pure AE role. It screens on Kimball modelling, dbt tests/docs, semantic-layer metrics for AI agents, and AI-assisted coding. The OpenTable summary leaves out dimensional modelling/SCD and the AI-coding workflow, and it leads with BI (which this skill flags as a red flag for AE targets). The McKinsey summary is closer, but it's positioned as DE/data foundations and keeps the CFA. A short dedicated build is worth it.

## CV Tailoring Instructions (for Claude Code)
Variant: B (General Modern Stack), AE + AI-self-service-forward. ENGLISH CV.
Branch: `variant-b-general` (edit `resume_base.tex`). Follow `CLAUDE.md`: comment-don't-delete, one page, no geometry/font changes, don't commit.
1. Summary: comment out the active OpenTable summary (keep its label comment). Add a `% Multiverse Analytics Engineer (London) -- Kimball + semantic layer for AI agents + AI-assisted dev; CFA out:` label, then set as the active text:
   "Analytics Engineer building trusted data models for AI-driven self-service: Kimball star schemas with SCD Type 2, tested and documented dbt pipelines on Snowflake with Airflow, and a dbt Semantic Layer that an LLM agent queries to turn business questions into validated SQL. AI-assisted development (Claude Code) as a daily workflow; data-quality framework at BNP Paribas."
   Must not exceed the current summary's line count. If it wraps, drop "with Airflow", then "and documented".
2. Skills: Programming → "Python, Git, AI coding tools (Claude Code), LLM APIs (Anthropic)". If that wraps, use the McKinsey line "Python, Git, coding agents (Claude Code)". Order: Transformation → Modeling → Warehousing (Snowflake first) → BI & Semantic.
3. CFA: out of the summary (EdTech, not finance).
4. Do not claim MCP or Cursor/Copilot unless Kris confirms she has used them.
5. Rebuild with tectonic, confirm one page, export: `cp build/resume_base.pdf output/cv_kris_huang_multiverse_analytics_engineer.pdf`. Attach under a neutral filename.

## Cover Letter Angle
Multiverse is doing what pc_pipeline was built to demonstrate: keep the Snowflake/dbt/Airflow core stable and redesign the layer on top so that people and AI agents query governed metrics instead of raw tables. In pc_pipeline, the LLM agent never writes free-form SQL. It resolves questions against metric definitions in the dbt Semantic Layer, and the output is validated before it runs. That's the "trusted metrics for AI/MCP self-service" design problem, and it's why you document models and metrics for machine consumption, not just humans. You build with Claude Code every day. You also review its output line by line (grain, join fan-out, SCD logic), because at BNP you had to design the dimensional model for three messy private-capital sources by hand, from grain declaration to surrogate keys. Their mission (skills unlocking potential) connects naturally to your path: moving from finance into engineering by upskilling.

## Preparation Gaps
- MCP: what the Model Context Protocol is (servers, tools, resources) and how a semantic layer is exposed through it: dbt's MCP server (Semantic Layer tools: list metrics, query metrics), Omni's and Cube's MCP/AI endpoints. Be ready to sketch "agent → MCP → semantic layer → Snowflake" and explain where governance lives.
- Metric design for agents: descriptions, synonyms and allowed dimensions per metric; why ambiguous metric names break agents; certified vs exploratory metrics.
- Omni vs Cube vs dbt Semantic Layer: trade-offs (they are "rethinking" the layer and may ask your opinion).
- Reviewing AI-generated dbt: a concrete story of Claude Code getting a model wrong (a fan-out join, a wrong grain, SCD2 validity windows) and how you caught it with tests.
- Snowflake on a data lake: external/Iceberg tables, clustering, warehouse sizing, incremental models (merge vs delete+insert), query profile reading.
- CI/CD for dbt: slim CI (state:modified+, defer), PR checks, dbt docs generation.
- EdTech domain: learner funnel (applications → enrolment → completion), apprenticeship levy funding, cohort retention, employer ROI metrics.
- Live SQL without AI: window functions and optimisation drills. They state explicitly they'll test fundamentals without tooling.

## Stack Analysis

### Have
- Complex SQL (CTEs, window functions)
- Kimball dimensional modelling: facts, dimensions, SCD Type 2, grain (BNP + pc_pipeline)
- dbt with generic + singular tests and documentation
- dbt Semantic Layer + an LLM agent consuming metrics (pc_pipeline)
- Snowflake, Airflow, Python, Git/GitHub
- Daily AI-assisted development (Claude Code)
- Translating business logic (private-capital deal pipeline) into models

### Missing
- Production dbt in a team setting (portfolio only)
- MCP hands-on
- Omni / Cube; Terraform/IaC

### Partial
- CI/CD for data workflows (slim CI planned/being built in pc_pipeline v2)
- Code review culture: solo repo; can speak to self-review of AI output
- BI: Power BI (not Omni/Tableau/Metabase)

### Green Flags
- Core stack stable and explicit (Snowflake, dbt, Airflow); the role owns modelling + metric definitions
- Semantic layer for AI agents is central: your strongest differentiator
- AI-assisted dev is expected, and they want fundamentals under it. That rewards substance.
- No year gate; well-funded scale-up; licensed A-rated sponsor; reports to a Director of DE

### Red Flags
- "Production dbt experience" required: portfolio dbt may be challenged. Frame BNP as production modelling and pc_pipeline as the dbt implementation.
- 3 days/week in office; UK move restarts the French residency clock
- Salary not stated (check it clears £41,700)

## Notes
- Verdict: APPLY with the tailored build. Top-tier London match with Fitch and Gousto. Arguably the best-aligned AE JD so far on the semantic-layer-for-agents angle.
- OpenTable: posting deactivated. Its tailored summary stays commented in `resume_base.tex` for reuse.

## Raw JD (abridged)
Multiverse, Analytics Engineer, London hybrid (3 days). Reports to Director of Data Engineering (Data & Insight). Build/maintain dbt models powering analytics and DS; platform Snowflake + dbt + Airflow (stable); rethinking the semantic/BI layer for AI/MCP-driven self-service so analysts, stakeholders and AI agents query trusted metrics. AI-assisted development (Claude Code, Cursor, Copilot) expected, with fundamentals to catch tooling errors.
Work: dbt models with AI assistants; business requirements → scalable models; Kimball schemas (facts, dims, SCDs); design/code reviews incl. AI-generated code; define/expose metrics via semantic layer for MCP consumption; dbt tests; docs for human and AI consumption; GitHub + CI/CD; optimise dbt/SQL; Snowflake on a data lake.
Required: complex SQL; Kimball modelling; production dbt incl. tests/docs; AI coding tools as a real workflow; fundamentals without AI; GitHub; independent business-logic translation; code review.
Desirable: Snowflake; semantic layer (Omni, Cube, dbt SL); BI (Omni, Tableau, Metabase); AI agent tooling/MCP; CI/CD for data; Python/Airflow; Terraform/IaC.
Benefits: 27 days + 5 extra days; Bupa; Wellhub; hybrid 3 days; 10 days work-from-anywhere. Basic DBS check required.
