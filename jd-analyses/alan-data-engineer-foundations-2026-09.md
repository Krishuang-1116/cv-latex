# Alan — Data Engineer (Data Foundations) — 2026-09

## Metadata
- Date: 2026-09-28
- Fit Score: High — a NAMED Tier-2 target on your list, on YOUR exact stack (Python, Airflow, Snowflake, dbt, AWS/GCP), and it explicitly welcomes early-career ("from early-career to highly experienced", C0-E level range incl. entry). The AI-agents-as-warehouse-users theme is a rare authentic match for your portfolio. Main gaps: Terraform/IaC and that it's a platform/DE-leaning role (enabling other engineers), not pure analytics modeling.
- Source: Direct paste (LinkedIn)
- Contract: Permanent, full-time — hiring across France, Spain, Belgium, Canada
- Location: France (Paris HQ) or other Alan hubs — English-working ("no need to speak French!")
- Compensation: C0-E level range (Alan public salary grid) — entry level (C0) in scope; check grid vs Passeport Talent floor.

## Why this is a good one (not an off-lane role)
Unlike Heuritech (crawling/K8s) or Talan (Microsoft Fabric), this platform role runs on YOUR stack: Airflow + Snowflake + dbt + Python + AWS. The only genuinely new required item is Terraform/IaC — contained, not a whole platform track. And it's a named target company that passes your filters (modern insurtech product company, not a traditional FI; strong engineering culture). Worth pursuing despite the platform/DE lean.

## CV Tailoring Instructions
Variant: B (General Modern Stack) — engineering-forward, PORTFOLIO-forward
Branch: variant-b-general
FRENCH CV: not needed (English-working). English canonical.
Summary line (English): "Data/Analytics Engineer who builds reliable data foundations others depend on — dbt models and tests in a layered Snowflake-style warehouse, Airflow orchestration (idempotent DAGs, retries), and an LLM agent over the semantic layer with data-quality guardrails. Python + SQL, rigor-first."
Skills reorder: Variant B, portfolio-forward. Foreground Airflow, dbt, Python, Snowflake, and the AI-agent build. Make the AI-agent-over-the-warehouse work explicit — it maps to their headline theme.
CFA positioning: Out of summary; education only (platform role).
Optional adds: none. Portfolio is the pitch.

## Cover Letter Angle
Alan says it out loud: "agents are becoming first-class users of our data warehouse... concerns around security, data quality and governance. We are building the foundations that allow Alan to make the most of this new paradigm." That is precisely what you built in pc_pipeline: an LLM agent over your semantic layer that translates natural-language questions into validated SQL, with a validator/guardrail layer enforcing data-quality rules before anything runs — an early, hands-on take on the exact "safe agent access to the warehouse" problem their Data Foundations team owns. Pair that with the rest of the foundation you built solo — a layered dbt pipeline with a full test suite, a real Airflow DAG (task groups, retries, idempotency), a MetricFlow semantic layer — and you're not describing tools you read about, you're describing a data platform you built end-to-end. You'd join eager to bring that rigor to healthcare data at Alan's scale, and to keep pushing on the agent-on-the-warehouse frontier they're defining.

## Preparation Gaps
Mostly covered by the AE learning plan. The one real add for this role:
- **Terraform / Infrastructure as Code** — explicitly required. NEW for you; worth a contained primer: providers, resources, state, modules, plan/apply. Small, and it keeps recurring in DE-platform roles — a cheap unlock, not a whole platform track. Recommended even under your AE focus, since it's the gateway skill for platform-flavored AE/DE roles on your own stack.
- **Governance/security for AI agents on the warehouse** — POV on RBAC/least-privilege, PII handling, query guardrails, safe agent access. Connects directly to your agent's validator work — a strong specific talking point here.
- **Platform / developer-experience thinking** — "designing systems, tools, libraries used by other engineers." Frame your AI-agent modules + generators as reusable, documented, tested tooling.
- **GCP** — they use AWS/GCP; you're AWS-familiar. Concept-level GCP is enough.
- **Metabase** — BI tool (you have Power BI); trivial concept-level swap.
- Production reliability — same as synthesis; your Airflow/testing work is the base.

## Stack Analysis

### Have
- Python + SQL — strong, with real rigor/craft discipline
- Airflow orchestration — HANDS-ON (DAG, task groups, retries, idempotency) — a required skill you actually hold
- dbt — layered pipeline + tests
- Snowflake — on CV (their warehouse)
- AWS — familiar (they use AWS/GCP)
- AI / agents / custom skills / MCP — authentic; your AI-agent-over-the-warehouse is a near-exact match for their headline mission
- Data quality / governance mindset — pc_pipeline tests + BNP DQ framework
- Git rigor, documentation discipline
- Ownership / autonomy / self-driven learning — strong culture fit

### Missing
- Terraform / IaC — the one real required gap
- "Production" infrastructure at company scale + systems/libraries used by other engineers (yours is solo portfolio + internal BNP work)
- Health/insurance domain (finance instead; less critical for a platform team)
- 3+ years nominal — but explicitly softened ("early-career to highly experienced", C0 in range)

### Partial
- GCP — AWS-familiar, GCP not yet
- Metabase — Power BI transfers
- Platform/DX (tooling for other engineers) — you build tooling, not yet team-shared libraries

### Green Flags
- NAMED Tier-2 target; passes your filters (modern insurtech product co., not a traditional FI)
- Exact stack: Python, Airflow, Snowflake, dbt, AWS/GCP
- Explicitly early-career-friendly + "hire people, not roles" + "don't check every box" — softest effective gate of any 3+ yr posting; explicitly encourages women to apply
- AI-agents-on-the-warehouse is their core theme — your rarest authentic differentiator
- English-working (no French needed); strong culture; healthy company (€800M ARR, 1M+ members)
- Reliability / data-quality / governance centric — your strengths

### Red Flags
- None on JD quality. Minor fit notes: platform/DE-leaning (enabling others via infra/tooling), a bit further from pure analytics modeling; Terraform/IaC is a real gap; process caveat — "you may join a different engineering team based on where we think you'll have the most impact", so you might be routed off Data Foundations.

## Notes
- Ranking: top-tier fit — named target, exact stack, early-career-welcomed, authentic AI hook. Comparable to Qonto/In Tandem/Emeria as a priority application. The Terraform gap is the only meaningful prep, and it's small.
- This is the role where your pc_pipeline AI-agent work pays off most directly — lead with it.

## Raw JD (abridged)

Company: Alan — prevention health insurance; integrates insurance, prevention, care in one UX. 40K+ companies, 1M+ members, €800M+ ARR, 1000+ people; hiring across France, Spain, Belgium, Canada.

Team: Data Foundations (within Tech Foundations) — builds/maintains/improves the Data Platform used by everyone at Alan; enables Alan's data-driven nature; partners with technical + non-technical colleagues; owns all data tooling. AI/agents becoming first-class warehouse users → new usage + security/quality/governance concerns; building foundations for that. Rapid expansion (4→6 countries this year; onboard new countries in weeks) → data foundations are the cornerstone. Missions: improve developer experience for data pipelines; reliable+secure warehouse access for Alaners and AI agents; strengthen security/governance; define standard data practices; evolve core data infra for international expansion. Core tools: Python, Airflow, Snowflake, AWS/GCP, Metabase, Terraform, dbt.

Expected skills:
- Owning ambitious problems, simple solutions
- 3+ years demonstrating impact in Data positions; welcomes early-career to highly experienced
- Building/operating production data infrastructure: orchestration (Airflow or similar), cloud DW, IaC
- Designing systems/tools/libraries used by other engineers/scientists/analysts
- Proficient in Python and SQL; high rigor/precision
- Curious about AI, eager to use it thoughtfully
- Great communication; humble, kind, collaborative, willing to grow
- Fluent English (no French needed)

Level: C0-E range. "We hire people, not roles" — apply even if you don't check every box; explicitly encourages women/underrepresented applicants. Note: may join a different engineering team based on impact.
