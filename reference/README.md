# reference/ — sponsor registers

Work-authorization checks for NL and UK roles. The register data is **gitignored**
(bulky, and stale within days); only the two scripts and this file are tracked.

## Refresh, then check

```bash
python3 reference/fetch_registers.py          # both; or: ... uk | nl
python3 reference/check_sponsor.py lendable   # both; or: ... --uk | --nl
```

Refresh before a check that matters. Every check prints the download date —
a stale register answers confidently and wrongly.

## Sources

| File | Source |
|---|---|
| `uk-licensed-sponsors.csv` | <https://www.gov.uk/government/publications/register-of-licensed-sponsors-workers> |
| `nl-recognised-sponsors.csv` | <https://ind.nl/en/public-register-recognised-sponsors/public-register-work> |

The GOV.UK asset URL changes on every refresh, so `fetch_registers.py` scrapes the
current link from the publication page. The IND register is a server-rendered HTML
table (Organisation, KVK), parsed straight out of the page. If either layout
changes, the script exits with a message rather than writing a truncated file.

## Matching

Registers list the **legal entity, not the brand**, so names are normalised
(lowercased, legal suffixes stripped) with a token-overlap fallback. Real cases:

- "Lendable" → **Lendable Operations Ltd** (London, Worker A rating, Skilled Worker)
- "Marktlink" → **Marktlink Capital Management Coöperatief U.A.**
- "Booking" → **Booking Holdings B.V.**, **Booking.com B.V.**, and ~9 more entities

With several entities, the employing one matters — ask which entity is on the
contract before relying on a hit.

## What a hit does and does not mean

A listing means the company **can** sponsor, not that it **will** for a given role.
The salary thresholds still govern:

- **UK Skilled Worker**: £41,700 or the occupation going rate, whichever is higher;
  new-entrant rate 70% of the going rate with a £33,400 floor (criteria apply).
- **NL Highly Skilled Migrant**: the reduced graduate threshold applies after the
  orientation year (zoekjaar); check the current IND figure.

**UK HPI** is a separate route needing no sponsor: a degree from a listed
university awarded within the last 5 years. Kris's JHU MA (2018) is outside that
window and ESSEC/CentraleSupélec is not listed, so HPI is not currently available
— UK roles therefore depend on Skilled Worker sponsorship.

## Working from another branch

These scripts live on `main`. From a variant branch, run them without switching:

```bash
python3 <(git show main:reference/check_sponsor.py) lendable
```

The data files are untracked, so they stay in place across checkouts.
