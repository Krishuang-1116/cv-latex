# Tarmac — Analytics Engineer (Customer Analytics Platform) — 2026-09

## Metadata
- Date: 2026-09-28
- Fit Score: High — one of your cleanest AE stack matches: dbt + semantic layer + metric definitions + data quality/tests/governance/lineage + CI/CD + AI tools/MCP, on an OMNI-native embedded analytics platform. Redshift is a warehouse swap (SQL transfers). Main caveats: 3-5 years, a heavy solo-ownership scope ("own and scale the platform"), and aviation domain (new, but a "plus"). No hard "senior/lead" gate.
- Source: Direct paste
- Contract: Not stated (full-time)
- Location: Not stated — international / English-working environment. Confirm (likely France/EU aviation-tech); French CV probably not required but have it ready.
- Compensation: Not stated — confirm, check vs Passeport Talent floor.

## Why this is a strong one
Almost your exact profile: dbt models, a semantic layer, consistent metric definitions, data-quality testing/governance, Git CI/CD, and explicit AI tools + MCP integrations — the last being your authentic differentiator. It's OMNI-native ("Powered by Omni Analytics," "configure and structure Omni"), and Omni has now recurred across many of your JDs (Qonto, Dashlane, In Tandem, + Vinted's Looker) — so learning Omni properly pays off here AND across your pipeline. The "analytics as a user-facing product, not a collection of dashboards" + "own from problem definition through production and adoption" framing suits your self-driven, end-to-end portfolio style.

## CV Tailoring Instructions
Variant: B (General Modern Stack) — engineering + product-forward, PORTFOLIO-forward
Branch: variant-b-general
FRENCH CV: probably not needed (English-working); keep ready if the role is France-based.
Summary line (English): "Analytics Engineer who ships analytics as a product — reliable dbt models, a semantic layer with consistent metric definitions, data-quality testing/governance, and an LLM/MCP agent for self-service insights. Owns problems end-to-end, from definition to production and adoption."
Skills reorder: Variant B, portfolio-forward. Foreground dbt, semantic layer / metric definitions, data quality, and AI/MCP. Note Redshift as a warehouse swap (Snowflake/Postgres/Redshift-ready). Surface Omni/Looker-family (via dbt Semantic Layer bridge).
CFA positioning: Out of summary; education only (aviation-ops SaaS, not finance).
Optional adds: none. The pc_pipeline solo end-to-end build + AI agent is the pitch — it directly answers the ownership + AI + self-service requirements.

## Cover Letter Angle
Tarmac wants someone to own a customer analytics platform end-to-end: a semantic layer on Omni, meaningful and consistent metric definitions, self-service for users of varying data expertise, data-quality/governance, and AI-generated insights. That is a near-perfect map of what you built solo in pc_pipeline: a layered dbt pipeline with a full test suite (quality-first), a MetricFlow semantic layer with fixed metric definitions (consistency), and an LLM agent over it — using an MCP-style setup — that lets a non-expert ask a question in natural language and get validated SQL back (self-service + AI insights). You didn't build a pile of dashboards; you built a product with a semantic contract and a safe query interface — exactly the "analytics as a user-facing product" philosophy Tarmac is hiring for. And because you built it from problem definition through to a working app entirely on your own initiative, "ownership from definition through production and adoption" isn't aspirational for you — it's how you already work. [If pursuing: add one line on genuine interest in operationally complex domains — aviation turnaround/ground-handling — as a systems-thinking challenge.]

## Preparation Gaps
Well-covered by the learning plan; this role sharpens two priorities:
- **Omni — learn it properly, not just a POV.** It's now recurred across ~5 of your JDs and is CENTRAL here (the platform is Omni-native). Go beyond concept: Omni topics, semantic modeling, embedded experience, permissions, and its AI features. Bridge from your dbt Semantic Layer work. This is the single highest-ROI item across your whole search now — promote it in the plan.
- **Redshift** — warehouse swap from Snowflake/DuckDB. Learn dist/sort keys, incremental models on Redshift, query perf/tuning, deployment workflows (the JD names all of these). SQL transfers directly.
- **Embedded / customer-facing analytics + multi-tenant permissions** — new concept: embedding analytics in a product, per-customer data-access controls (RLS-style), self-service "topics." Connects to your guardrail/governance instincts.
- **Metric consistency across products/customers** — extend your single-project semantic layer thinking to consistent business definitions across many customers.
- **AI/MCP** — authentic strength; lead with it (they explicitly want AI tools + MCP integrations).
- Aviation/ops domain — a "plus," skim if pursuing.

## Stack Analysis

### Have
- dbt — core; reliable/scalable models + tests (their central requirement)
- Semantic layer + metric definitions — MetricFlow; consistent definitions (their explicit need)
- Data quality / testing / governance / documentation — pc_pipeline + BNP DQ framework
- Advanced SQL — strong
- Git / CI-CD concept — transferable to their Git-based deployment workflows
- AI tools + MCP — authentic (you work in MCP, built an agent) — a named requirement here
- Incremental models — built one (mart_fee_revenue) with late-arriving-data handling
- End-to-end ownership / product mindset — solo portfolio build; semantic-contract + self-service agent = "analytics as product"

### Missing
- 3-5 years experience — the main gate (moderate; no "senior/lead" framing)
- Omni hands-on (concept via dbt SL; not the platform)
- Redshift hands-on (Snowflake/DuckDB instead)
- Embedded / customer-facing analytics products
- Multi-tenant / per-customer permissions at product scale
- Aviation/transport/logistics domain (a "plus")

### Partial
- Semantic layer — dbt SL/MetricFlow, not Omni specifically (bridges over)
- Warehouse perf tuning — reasoned about incremental/idempotency, not Redshift-specific
- Self-service enablement (topics, training, docs) — you built a self-service agent; the "topics/dashboards/training" packaging is new

### Green Flags
- dbt + semantic layer + metric definitions + data quality + CI/CD — your exact core
- AI tools + MCP explicitly required — your rarest authentic differentiator
- Omni-native (recurring theme worth owning) — learning it compounds across your search
- "Analytics as a product, not dashboards" + full end-to-end ownership — matches your build style
- Autonomy / product mindset / fast-moving — culture fit for a self-driven candidate
- English-working, international; product company; not a bank

### Red Flags
- None on JD quality. Fit notes: 3-5 years + a solo "own and scale the whole platform" scope is significant ownership for an entry-level profile — your portfolio (solo end-to-end build) is the counter-evidence, so lead with it. Redshift + Omni + embedded analytics are real (learnable) gaps.

## Notes
- Ranking: strong AE fit, comparable to Alan/Emeria/In Tandem. The ownership scope makes it a stretch-but-well-matched role where your portfolio does the heavy lifting.
- ACTION for the learning plan: promote Omni from "form a POV" (Week 3) to "learn it properly" — it's now the highest-recurring tool across your entire search and central to this Omni-native role.

## Raw JD (abridged)

Role: Analytics Engineer to own and scale Tarmac's customer analytics platform — powered by Omni Analytics, embedded in products, used by airports/airlines/ground-handling to understand performance and make operational decisions, and by internal teams for support + product development. Own the data models AND the overall customer analytics experience: understand user needs, define metrics, enable access/exploration/dashboards/AI insights.

Responsibilities: own platform dev + improvement (architecture, semantic layer, embedded experience, permissions, reliability, roadmap); understand customers' operations and translate to scalable analytics; build/maintain reliable scalable dbt models (customer-facing + internal); configure/structure Omni for an intuitive AI-powered experience; work with customers + Product/Eng/Design/Ops/CS to turn recurring needs into reusable capabilities; define meaningful metrics + consistent business definitions; enable self-service (topics, reusable dashboards, docs, training); monitor usage/performance/adoption; maintain data quality/security/governance (automated testing, monitoring, lineage, docs, access controls); optimize Redshift + dbt (incremental models, query perf, reliability, deployment); use AI tools + MCP integrations to accelerate work.

Preferred: 3-5 years in Analytics Engineering / Data Engineering / BI / similar; advanced SQL + hands-on dbt + a cloud DW (Redshift, Snowflake, or BigQuery); modern BI/analytics platform (Omni, Looker, Tableau, Power BI); strong dimensional modeling, semantic layers, metric definitions, incremental pipelines, data governance; customer + product mindset (analytics as a user-facing product); data-quality tests, monitoring, docs, Git-based CI/CD; excellent communication (technical + non-technical, international); comfortable autonomous, fast-moving, ownership from problem definition through production + adoption.

Additional (plus): Python for analysis/automation/pipelines; embedded analytics / customer-facing data products; AI-powered analytics / AI dev tools / MCP integrations; aviation/transport/logistics/operationally complex industry.

## UPDATE (2026-09-29) — company + process revealed
- Company: Tarmac Technologies (product: AGOA) — aircraft-turnaround / ground-operations SaaS. STATION F startup, Paris 2nd, CDI, "> 3 ans" / 3-5 years, partial remote. Small fast-growing team; clients = airports/airlines/ground-handlers.
- Process (startup-light, human, NO recruiter): 1) 45-min call with Vincent Desmazières (team lead) — assesses SOFT skills (ownership, communication), motivation, understanding of the role; 2) technical interviews with the data team; 3) reference checks; 4) offer.
- Fit unchanged: HIGH. The reveal IMPROVES practical attainability — direct, lead-driven process where your portfolio + communication + genuine interest are seen (no ATS/recruiter filter), and the FIRST round is explicitly soft-skills/motivation (a round you can win). The counterweight is unchanged: it's a SOLO "own and scale the whole platform" mandate + 3-5 years — a heavy ownership ask for an entry profile. Lean HARD on your solo end-to-end pc_pipeline build as proof you can own a platform alone.
- Direct-outreach opportunity: Vincent is named and does the first call. A short, specific LinkedIn note to him (Omni-native platform + your AI-agent-over-a-semantic-layer + solo end-to-end build) is high-value here — small team, lead-driven, no recruiter in the way.
- Prep priority reminder: Omni (this is the Omni-native role) + Redshift perf/cost. Your AI/MCP work is a direct match for their "use AI tools and MCP integrations" line — foreground it.
