#!/usr/bin/env python3
"""Look up an employer in the UK and NL sponsor registers.

    python3 reference/check_sponsor.py lendable
    python3 reference/check_sponsor.py "booking holdings" --uk
    python3 reference/check_sponsor.py marktlink --nl

Registers list the legal entity, not the brand ("Lendable Operations Ltd",
"Booking.com B.V."), so matching is done on a normalised name with legal
suffixes stripped, plus a token-overlap fallback. Always read the printed
download date: a stale file answers confidently and wrongly.
"""

import csv
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SUFFIXES = {
    "bv", "nv", "ltd", "limited", "plc", "llp", "llc", "inc", "sa", "sas", "sarl",
    "gmbh", "ag", "holding", "holdings", "group", "groep", "operations", "services",
    "international", "nederland", "netherlands", "uk", "europe", "emea", "the", "and",
}


def normalise(name: str) -> str:
    n = name.lower().replace("&", " and ")
    n = re.sub(r"[^a-z0-9 ]+", " ", n)
    return re.sub(r"\s+", " ", n).strip()


def tokens(name: str) -> list[str]:
    return [t for t in normalise(name).split() if t not in SUFFIXES and len(t) > 1]


def load(path: Path):
    if not path.exists():
        return None, None
    meta_path = path.with_suffix(".meta.json")
    meta = json.loads(meta_path.read_text()) if meta_path.exists() else {}
    with path.open(newline="") as fh:
        rows = list(csv.DictReader(fh))
    return rows, meta


def search(rows, query: str, name_key: str):
    q_norm, q_tokens = normalise(query), tokens(query)
    exact, partial = [], []
    for row in rows:
        name = (row.get(name_key) or "").strip()
        if not name:
            continue
        n_norm = normalise(name)
        if q_norm and q_norm in n_norm:
            exact.append(row)
        elif q_tokens and all(t in n_norm.split() for t in q_tokens):
            partial.append(row)
    return exact, partial


def report(label: str, path: Path, query: str, name_key: str, cols: list[str]) -> None:
    rows, meta = load(path)
    print(f"\n=== {label} ===")
    if rows is None:
        print(f"  no data file ({path.name}) -- run: python3 reference/fetch_registers.py")
        return
    print(f"  {len(rows):,} entries, downloaded {meta.get('downloaded', '?')}")
    exact, partial = search(rows, query, name_key)
    hits = exact or partial
    if not hits:
        print(f"  NOT FOUND: '{query}'")
        return
    if not exact:
        print("  no direct match; closest by tokens:")
    for row in hits[:12]:
        print("  - " + " | ".join(str(row.get(c, "")).strip() for c in cols if row.get(c)))
    if len(hits) > 12:
        print(f"  ... and {len(hits) - 12} more")
    if meta.get("note"):
        print(f"  note: {meta['note']}")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = {a for a in sys.argv[1:] if a.startswith("--")}
    if not args:
        sys.exit(__doc__)
    query = " ".join(args)
    both = not (flags & {"--uk", "--nl"})
    if both or "--uk" in flags:
        report("UK licensed sponsors (Skilled Worker)", HERE / "uk-licensed-sponsors.csv",
               query, "Organisation Name", ["Organisation Name", "Town/City", "Type & Rating", "Route"])
    if both or "--nl" in flags:
        report("NL recognised sponsors (IND, labour/HSM)", HERE / "nl-recognised-sponsors.csv",
               query, "Organisation Name", ["Organisation Name", "KVK number"])
    print()
