#!/usr/bin/env python3
"""List volatile facts whose last_verified date is older than N days (default 60).

Usage: scripts/check-volatile.py [--days 60]
Exit code 1 if anything is stale, so it can be used in cron/CI.
"""
import argparse
import datetime as dt
import pathlib
import re
import sys

FILE = pathlib.Path(__file__).resolve().parent.parent / "knowledge" / "_meta" / "volatile-facts.md"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=60)
    args = ap.parse_args()

    today = dt.date.today()
    stale, ok = [], 0
    for line in FILE.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|") or line.startswith("|---") or "last_verified" in line:
            continue
        cols = [c.strip() for c in line.strip("|").split("|")]
        if len(cols) < 5:
            continue
        key, value, last = cols[0], cols[1], cols[4]
        m = re.match(r"(\d{4}-\d{2}-\d{2})", last)
        if not m:
            stale.append((key, value, "never verified"))
            continue
        age = (today - dt.date.fromisoformat(m.group(1))).days
        if age > args.days:
            stale.append((key, value, f"{age} days old"))
        else:
            ok += 1

    print(f"✅ {ok} fresh · ⚠️ {len(stale)} stale (threshold {args.days} days)")
    for key, value, why in stale:
        print(f"  ⚠️  {key:<22} {value:<35} {why}")
    return 1 if stale else 0


if __name__ == "__main__":
    sys.exit(main())
