from __future__ import annotations

from pathlib import Path
import csv
from typing import Dict, List

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "tickets.csv"


def _load_tickets() -> List[Dict[str, str]]:
    with DATA_PATH.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def retrieve_tickets(requester: str, query: str) -> List[Dict[str, str]]:
    normalized = query.strip().lower()
    if " or " in normalized:
        return _load_tickets()

    results: List[Dict[str, str]] = []
    for ticket in _load_tickets():
        haystack = " ".join((ticket["ticket_id"], ticket["content"]))
        if normalized in haystack.lower():
            results.append(ticket)
    return results
