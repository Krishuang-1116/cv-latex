# Lendable — Analytics / Python Data Engineer (Python Infrastructure team) — London — 2026-09

## Metadata
- Date: 2026-09-29
- Fit Score: HIGH. In-house fintech (consumer credit: loans, cards, car finance), NOT a bank; the modern stack is exactly yours (Snowflake + dbt + Python); junior-friendly wording ("some experience building pipelines", "keen desire to learn"); role = AE + Python tooling/automation, which matches pc_pipeline (dbt + Airflow + LLM agent + Streamlit). The main question is the UK visa route (see below), not fit.
- Tailoring effort: LOW (summary swap, English Variant B).
- Source: LinkedIn / direct paste (exact title not in paste)
- Contract: Not stated (permanent expected)
- Location: London, hybrid (3 days/week in office)
- Compensation: Not stated
- Company: Lendable, UK fintech unicorn, 800+ people, profitable since 2017, expanding to the US.
- Interview process: phone call → take-home coding exercise → 60-min technical video → 30-min culture → final.

## UK work authorization (updated 2026-09-29 via reference/check_sponsor.py)
- Sponsor: CONFIRMED. Lendable Operations Ltd (London) is on the UK Home Office register of licensed sponsors, Worker A rating, Skilled Worker route.
- HPI: NOT available. JHU MA (2018) is outside the 5-year window; ESSEC/CentraleSupélec aren't on the list. UK roles therefore depend on Skilled Worker sponsorship.
- Salary must clear £41,700 or the occupation going rate, whichever is higher (new-entrant rate: 70% of the going rate, £33,400 floor, criteria apply). Confirm the band early with the Talent Partner.
- Right-to-work form answer: "I currently do not have the right to work in the UK and would require company visa sponsorship."
- Moving to the UK restarts the French residency timeline.

## CV Tailoring Instructions (for Claude Code)
Variant: B (General Modern Stack), Python-forward. ENGLISH CV.
Branch: `variant-b-general` (edit `resume_base.tex`). Follow `CLAUDE.md`: comment-don't-delete, one page, no geometry/font changes, don't commit.
1. Summary: comment out the current active summary, add a `% Lendable (AE/Python DE, London) —` label comment, then set as the active text:
   "Analytics Engineer building on Snowflake, dbt and Python: tested dbt models (6 defect classes), Python tooling around them — an Airflow DAG with retries and idempotent reruns, an LLM agent that turns natural-language questions into validated SQL, and a Streamlit app — plus a data-quality framework over three source systems at BNP Paribas. \textbf{CFA Charterholder}."
   Must not exceed the current summary's line count. If it wraps, drop "with retries and idempotent reruns", then "and a Streamlit app". (Streamlit only if the app is real.)
2. Skills: Warehousing → Snowflake first. Programming → "Python (pandas, PySpark), Git" only if it doesn't wrap. No other changes.
3. Rebuild with tectonic, confirm one page, export: `cp build/resume_base.pdf output/cv_kris_huang_lendable_analytics_data_engineer_python_infrastructure.pdf`.
CFA positioning: keep at the end of the summary. Consumer-credit fintech: credit literacy is a light plus, not the lead.
Optional adds: UOB credit-analyst background would fit a lending company, but it costs a line; skip for one-page safety.

## Cover Letter Angle
Short. The role is "analytics engineering + Python to automate and build tools", which is exactly how you built pc_pipeline: dbt on Snowflake for the modeling layer, with Python around it — an Airflow DAG (dependency-ordered task groups, retries, idempotent reruns), an LLM agent that answers business questions through a semantic layer with validated SQL, and a Streamlit front end. At BNP you did it on messy real data: three manually maintained source systems, a declared grain, SCD Type 2, and a data-quality framework for duplicates and identity-resolution failures, the same class of problems as customer/application data in lending. One line on credit: CFA (and earlier credit-analysis work) means you understand what the data is for: underwriting, arrears, portfolio performance.

## Preparation Gaps
- Take-home coding exercise: modern Python quality matters ("strong, modern Python"). Practise: type hints, dataclasses/pydantic, small functions, pytest, a clean README, a pyproject.toml / uv or poetry, ruff formatting. Treat it like a PR.
- Python for data workflows: API ingestion (requests/httpx, pagination, retries), idempotent loads to Snowflake (snowflake-connector, COPY/MERGE), logging.
- dbt on Snowflake depth: incremental models (merge strategy), snapshots, macros, tests/contracts, CI (slim CI).
- Lending data concepts: application funnel, approval rate, APR, vintage/cohort curves, arrears/default rates, early-settlement.
- Technical interview: SQL window functions + a modeling question (e.g., "design a loan-performance mart": grain = loan × month snapshot).

## Stack Analysis

### Have
- Snowflake, dbt, SQL (core stack)
- Python: Airflow DAG, LLM agent, Streamlit, PySpark ETL, data processing
- Pipelines/ETL: pc_pipeline end to end; TripAdvisor PySpark ETL; BNP staging→mart
- Data quality: BNP framework, dbt tests
- Communication with technical + non-technical stakeholders (BNP, LVMH)
- Finance/credit literacy: CFA (+ UOB credit background off-CV)

### Missing
- Production "data-intensive backend services"
- Professional software-engineering practices at company scale (code review, CI owned)

### Partial
- "Strong, modern Python": good project Python; the take-home is where to prove it

### Green Flags
- In-house fintech product company (your strong lane), not a bank or ESN
- Modern stack = Snowflake + dbt + Python exactly
- Junior-friendly requirements; learning culture
- Clear, structured interview process
- Cross-functional experience "a plus but not needed"

### Red Flags
- UK visa: Skilled Worker only (sponsor confirmed); salary threshold must be met
- 3 days in office in London (relocation)
- JD is light on specifics ("no two days look the same")
- No age-discrimination wording

## Notes
- Verdict: APPLY (high fit). Sponsor confirmed. The remaining gate is the salary threshold; raise it early.
- London pattern: filter for licensed sponsors (check_sponsor.py) + salary bands at or above the Skilled Worker threshold; HPI isn't an option.

## Sources (visa info, checked 2026-09-29; verify on GOV.UK)
- HPI list summary: https://london-immigrationlawyer.co.uk/high-potential-individual-visa/universities/
- Skilled Worker salary thresholds: https://www.davidsonmorris.com/skilled-worker-visa-minimum-salary/

## Raw JD (abridged)
Lendable — UK fintech unicorn (800+), profitable since 2017, backed by Balderton and Goldman Sachs; rebuilt loans, credit cards, car finance; expanding UK + US. Role in the Python Infrastructure team, at the intersection of analytics engineering and Python-based data engineering: transform/model data with SQL + dbt; Python for data workflows, automation, internal tools. Stack: Snowflake, dbt, Python.
Looking for: SQL/Snowflake or other modern data platforms; strong modern Python; some experience with pipelines/ETL/data-intensive backend services; collaborative, clear communication with technical and non-technical stakeholders; desire to learn; cross-functional experience a plus.
Process: phone call; take-home coding exercise; 60-min technical video; 30-min culture; final.
Benefits: hybrid 3 days in office; private health; retirement savings; referral bonus; meals; cycle-to-work/EV schemes.
