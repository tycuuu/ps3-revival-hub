"""Sync the published primary-DNS sheet into a small JSON file for the site."""

from __future__ import annotations

import csv
import json
import re
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "data" / "main-dns.json"
CSV_URL = (
    "https://docs.google.com/spreadsheets/d/e/2PACX-1vRtl-fj4jqAcie8rGQ0iI7HMg5C3JnzaUFZYbP9twG4YYK93OlqeVNOYjfswwhx0g"
    "/pub?gid=1640242559&single=true&output=csv"
)
USER_AGENT = "PS3-Revival-Hub/1.0 (primary DNS catalogue sync)"


def normalize(value: str) -> str:
    value = value.casefold().replace("ł", "l")
    value = unicodedata.normalize("NFKD", value)
    value = "".join(char for char in value if not unicodedata.combining(char))
    return re.sub(r"[^a-z0-9]+", " ", value).strip()


def main() -> None:
    request = Request(CSV_URL, headers={"User-Agent": USER_AGENT})
    with urlopen(request, timeout=30) as response:
        content = response.read().decode("utf-8-sig", errors="replace")

    rows = list(csv.reader(content.splitlines()))
    if not rows:
        raise RuntimeError("The published DNS CSV is empty")

    title_names = {"gra", "game", "title", "game title", "game name", "name", "nazwa gry"}
    dns_names = {
        "dns", "glowny dns", "dns glowny", "main dns", "primary dns", "dns address",
        "main dns address", "adres dns", "adres dns glowny", "ps3 dns",
    }
    header_index = next(
        (
            i for i, row in enumerate(rows)
            if any(normalize(cell) in title_names for cell in row)
            and any(normalize(cell) in dns_names for cell in row)
        ),
        0,
    )
    headers = [normalize(cell) for cell in rows[header_index]]
    title_index = next((i for i, value in enumerate(headers) if value in title_names), 0)
    dns_index = next((i for i, value in enumerate(headers) if value in dns_names), 1 if title_index == 0 else 0)

    games: dict[str, str] = {}
    for row in rows[header_index + 1 :]:
        title = row[title_index].strip() if title_index < len(row) else ""
        dns = row[dns_index].strip() if dns_index < len(row) else ""
        if title and dns:
            games[normalize(title)] = dns

    if not games:
        raise RuntimeError(
            "No game/DNS rows were recognized. Check the published CSV headers and sharing settings."
        )

    snapshot = {
        "updatedAt": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
        "games": games,
    }
    OUTPUT.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote primary DNS for {len(games)} games")


if __name__ == "__main__":
    main()
