# Alma — Analytics Engineer (Central Data) — 2026-09

## Metadata
- Date: 2026-09-28
- Fit Score: High — strong AE match on your exact modern stack (dbt, BigQuery, Looker, GCP, Git, Claude) with a medallion/semantic-layer/metric-consistency/data-quality/lineage mandate that is squarely your wheelhouse. Soft 2-year gate + strong inclusive language. Main caveats: an explicit mentoring/enablement expectation (training experienced analysts) that's a stretch for entry-level, and Looker/Argo/BigQuery are tool swaps.
- Source: Direct paste
- Contract: Permanent (CDI) — Paris, hybrid, OR full-remote in France
- Location: Paris / full-remote France — English-working ("fluent in English")
- Compensation: "Competitive salary based on 12 months" (not stated) — confirm; Next40 fintech, likely solid. Check vs Passeport Talent floor.
- Company: Alma — BNPL leader in France, 10 EU countries, 25k+ merchants, 10M consumers, €100M+ ARR, 400+ staff, Next40. Modern payments fintech (NOT a traditional bank) — passes your filter.

## CV Tailoring Instructions
Variant: B (General Modern Stack) — engineering + AI-forward, PORTFOLIO-forward
Branch: variant-b-general
FRENCH CV: not required (English-working; JD in English). English canonical; French ready if they prefer.
Summary line (English): "Analytics Engineer building trusted data foundations — layered dbt models (staging→intermediate→mart), tests/freshness/docs, a semantic layer with consistent metric definitions, and an LLM agent enabling conversational, self-service analytics. Documentation-first, governance-minded."
Skills reorder: Variant B, portfolio-forward. Foreground dbt (models/macros/tests/docs), semantic layer + metric consistency, data quality/lineage/governance, and the AI agent (Claude is in their stack; they explicitly want conversational analytics). Note BigQuery (swap from Snowflake/DuckDB), Looker (from Power BI + dbt SL).
CFA positioning: Out of summary; keep in education. Mild plus — Alma's Data team serves Finance + Risk, so finance literacy helps with those stakeholders (mention in interview, not summary).
Optional adds: none. Portfolio (layered pipeline + semantic layer + AI agent) is the pitch.

## Cover Letter Angle
Alma's central Data team wants to rebuild and standardize its foundations "following a medallion-inspired approach with clear layers," strengthen the semantic layer and metric consistency, improve lineage/governance, and — explicitly — enable "more self-service and conversational analytics" so business teams can find, understand, trust, and use data. That maps almost line-for-line onto what you built in pc_pipeline: a layered dbt architecture (staging → intermediate → mart, i.e. medallion-style) with a full test suite, documentation as a first-class deliverable, a MetricFlow semantic layer with fixed metric definitions, and an LLM agent over it that turns natural-language questions into validated SQL — literally "conversational analytics" with data-quality guardrails. And because Claude is already in your stack (as it is in Alma's), an AI-native workflow isn't something you'd ramp into — it's how you already build. On the enablement side, your instinct is documentation-first: you keep rigorous, teachable notes of every modeling and tooling decision, which is exactly the raw material for training analysts on dbt, governance, and metric definitions. [Honest note: frame mentoring as enthusiasm + a documentation-teaching habit, not years of formal mentoring.]

## Preparation Gaps
Well-covered by the learning plan; this role sharpens the BI-tool priority:
- **Looker / LookML** — recurring across your search (Tarmac, Vinted, now Alma) and named here. Promote it alongside Omni: learn LookML modeling, explores, the semantic layer, and how it sits on dbt. Your dbt Semantic Layer work bridges it. (This + Omni is the BI-semantic-tool theme worth actually learning.)
- **BigQuery** — swap from Snowflake/DuckDB; partitioning/clustering and COST optimization (Alma explicitly wants cost-optimized models). SQL transfers.
- **Argo (Argo Workflows)** — orchestration on K8s; "nice if." Different from your Airflow but the orchestration concepts transfer; concept-level is enough.
- **Data contracts** — newer concept (schema agreements between data producers/consumers, enforced). Learn the idea; you validate them with Engineering here.
- **Medallion architecture** — you already build staging/intermediate/marts = bronze/silver/gold; just map the vocabulary.
- **GCP** — AWS-familiar; concept-level GCP.
- **Enablement/mentoring** — framing item, not study: lean on your documentation-first, teaching-oriented habit.
- BNPL/payments domain — mild; skim.

## Stack Analysis

### Have
- dbt — core (models, macros, tests, docs) — their central requirement
- Dimensional modeling (facts, dimensions, keys, relationships) — explicit requirement; your strength
- Data quality / tests / freshness / documentation — pc_pipeline + BNP DQ framework; documentation is first-class here and is your habit
- Semantic layer + metric consistency — MetricFlow; their explicit need
- AI agent / conversational analytics — you built exactly this; Claude is in their stack; they explicitly want it
- SQL — strong
- Git / PR-based development, code reviews — yes (advanced Git discipline)
- Layered/medallion architecture — staging→int→marts maps directly

### Missing
- Mentoring/enablement of (experienced) analysts — no formal mentoring track (framed via documentation-teaching habit)
- Looker / LookML hands-on (Power BI + dbt SL instead)
- BigQuery hands-on (Snowflake/DuckDB)
- Argo Workflows (Airflow instead)
- Data contracts (concept-level)
- 2 years experience — you're below, but strongly softened ("don't meet every requirement... value potential/curiosity/growth as much as experience")

### Partial
- GCP — AWS-familiar
- Orchestration — Airflow hands-on; Argo is the swap
- Semantic layer — MetricFlow, not Looker's (bridges)
- Cost/perf optimization — reasoned about incremental/idempotency; BigQuery cost tuning is new

### Green Flags
- dbt + semantic layer + metric consistency + data quality + lineage/governance + medallion — your exact core
- Claude in the stack + explicit "conversational analytics" goal — your AI-agent work is direct evidence
- Soft 2-year gate + strong inclusive language (value potential/growth)
- English-working; full-remote-in-France option; modern payments fintech (not a bank)
- Finance/Risk stakeholders — your finance literacy is a mild differentiator
- Case-study interview stage — rewards demonstrable skill (good for you)
- Strong benefits, Next40, healthy ARR

### Red Flags
- None on JD quality. Fit notes: the "mentor and train analysts" responsibility is genuinely aimed above entry level — address it honestly (enthusiasm + documentation-teaching habit, not overclaim). Looker/Argo/BigQuery are learnable swaps.

## Notes
- Ranking: strong AE fit, in your top lane with Alan/Emeria/Tarmac/Elax. The conversational-analytics + Claude-in-stack angle makes your AI-agent portfolio a direct hook again.
- Reinforces the Looker/Omni priority: the BI-semantic-tool layer is now the single most recurring learn-it item across your search. Worth promoting in the plan (pair with the Omni decision you paused).
- Case study stage means: prepare a tight, reproducible, documented mini-model + metric-definition example — your pc_pipeline habits are the base.

## Raw JD (abridged)

Company: Alma — installment/deferred payment (BNPL) for merchants + consumers; BNPL leader in France, 10 EU countries; 25k+ merchants, 10M consumers, €100M+ ARR, 400+ staff, Next40.

Team: central Data team serving Finance, Product, Marketing, Risk, Operations. 6 Data Analysts incl. experienced colleagues; works at the intersection of Data Engineering, Data Analytics, and business. Reports to Gil Marlard. Mission: strengthen data foundations for reporting/analytics/operational processes/decisions; rebuild + standardize foundations of varying maturity; enable more self-service + conversational analytics; improve lineage + governance via a medallion-inspired layered approach.

Data modeling & quality: build/maintain reusable models, macros, semantic layers in dbt + BigQuery; staging/intermediate/mart models; data quality tests, freshness checks, docs; improve lineage/ownership/discoverability; strengthen semantic layer + consistent metric definitions; remove duplicated/obsolete datasets; optimize queries/models for reliability, performance, cost.

Central Data Analytics community: build reusable data assets for analysts across domains; lead enablement — mentor analysts, train on dbt/Looker/governance/metric definitions; partner on data platform roadmap (GCP, BigQuery, Argo, dbt, Looker); keep stack clean/reliable/maintainable; code reviews + analytics engineering standards; discuss/validate data contracts with Engineering; collaborate with analysts/engineers/business.

Stack: dbt, BigQuery, Looker, GCP, Argo, Git, Claude.

About you: 2+ years in AE/DE/Data Analytics/similar; practical dbt (models, tests, docs); data modeling (facts, dims, keys, relationships); Git + PR-based dev; excellent communication (technical + business); fluent English. Nice: BigQuery, Looker, GCP, Airflow or Argo; Python. Strong inclusive language ("don't meet every requirement... value potential, curiosity, growth as much as experience").

Process: TA call → hiring manager call → case study with 2-3 team members → 1-2 tailored interviews. Paris/hybrid or full-remote France; CDI; strong benefits.
