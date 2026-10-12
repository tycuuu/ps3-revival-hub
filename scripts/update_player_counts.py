"""Fetch PS3-only live counts for the static GitHub Pages catalogue."""

from __future__ import annotations

import csv
import json
import re
import sys
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
SHEET_CSV = "https://docs.google.com/spreadsheets/d/1Oj3D-jTXuEPmC4b21FQ1I-K8JTJYQRkKkK4cBhTaHxs/export?format=csv"
OUTPUT = ROOT / "data" / "live-counts.json"
USER_AGENT = "PS3-Revival-Hub/1.0 (community game count display)"
BFBC2_SERVERS = {
    "Conquest · Panama Canal": "https://psrestored.online/bfbc2?server=conquest",
    "Conquest · Arica Harbor": "https://psrestored.online/bfbc2?server=s4",
    "Rush · Valparaiso": "https://psrestored.online/bfbc2?server=s3",
    "Squad Rush · Panama Canal": "https://psrestored.online/bfbc2?server=s5",
    "Squad Deathmatch · Panama Canal": "https://psrestored.online/bfbc2?server=s6",
    "Rush · Arica Harbor": "https://psrestored.online/bfbc2?server=rush",
    "Vietnam Conquest · Hill 137": "https://psrestored.online/bfbc2?server=s8&game=vietnam",
    "Vietnam Rush · Hill 137": "https://psrestored.online/bfbc2?server=s7&game=vietnam",
}


class PageText(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.text: list[str] = []
        self.descriptions: list[str] = []
        self.psn_links: set[str] = set()
        self.panel_found = False
        self._stack: list[tuple[str, bool]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "meta" and values.get("name", "").casefold() in {"description", "og:description"}:
            self.descriptions.append(values.get("content", "") or "")
        parent_inside = self._stack[-1][1] if self._stack else False
        inside = parent_inside or values.get("id") == "server-panel"
        if values.get("id") == "server-panel":
            self.panel_found = True
        if tag == "a" and inside and "/bfbc2/players/psn/" in (values.get("href") or ""):
            self.psn_links.add((values.get("href") or "").split("?", 1)[0].rstrip("/").casefold())
        if tag not in {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}:
            self._stack.append((tag, inside))

    def handle_endtag(self, tag: str) -> None:
        for index in range(len(self._stack) - 1, -1, -1):
            if self._stack[index][0] == tag:
                del self._stack[index:]
                break

    def handle_data(self, data: str) -> None:
        value = " ".join(data.split())
        if value:
            self.text.append(value)


def fetch(url: str) -> tuple[str, PageText]:
    request = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(request, timeout=25) as response:
        html = response.read().decode("utf-8", errors="replace")
    parser = PageText()
    parser.feed(html)
    return html, parser


def stamp() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def count_tduworld() -> int | None:
    _, page = fetch("https://www.tduworld.com/")
    text = " ".join(page.text)
    match = re.search(r"PS3\s+Online\s*:?\s*(\d+)\s+Players\s+Online", text, re.I)
    return int(match.group(1)) if match else None


def count_buzz_ps3() -> int | None:
    _, page = fetch("https://www.buzz-revival.online/")
    text = " ".join(page.text)
    match = re.search(r"players\s+online\s+PS3\s+(\d+)\s*[·•]\s*RPCS3\s+\d+", text, re.I)
    return int(match.group(1)) if match else None


def count_psrestored(url: str) -> int:
    _, page = fetch(url)
    if not page.panel_found:
        raise RuntimeError("Nie znaleziono profili PSN w panelu serwera")
    return len(page.psn_links)


def read_sheet() -> tuple[list[dict[str, str]], set[str]]:
    request = Request(SHEET_CSV, headers={"User-Agent": USER_AGENT})
    with urlopen(request, timeout=25) as response:
        content = response.read().decode("utf-8-sig", errors="replace")
    rows = list(csv.reader(content.splitlines()))
    section = ""
    projects: list[dict[str, str]] = []
    titles: set[str] = set()
    for row in rows:
        first = (row[0] if row else "").strip()
        if first == "PS3 Online Multiplayer Games":
            section = "projects"
            continue
        if first == "Gra":
            section = "games"
            continue
        if section == "games" and first:
            titles.add(first.casefold())
            continue
        if section != "projects" or len(row) < 4 or not first:
            continue
        cells = [(row[i] if i < len(row) else "").strip() for i in range(9)]
        titles.add(cells[0].casefold())
        projects.append({"title": cells[0], "project": cells[1], "url": cells[2], "status_url": cells[3]})
    return projects, titles


def load_previous() -> dict:
    try:
        return json.loads(OUTPUT.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {"checkedAt": None, "games": {}}


def main() -> None:
    previous = load_previous().get("games", {})
    results: dict[str, dict] = {}
    now = stamp()
    rows, titles = read_sheet()
    has_bfbc2 = any("bad company 2" in title for title in titles)
    has_tdu = any("test drive unlimited 2" in title for title in titles)
    buzz_title = next((title for title in titles if "buzz" in title), None)
    def save_count(key: str, players: int, source: str, *, servers: list[dict] | None = None) -> None:
        payload = {"players": players, "source": source, "checkedAt": now}
        if servers is not None:
            payload["servers"] = servers
        results[key] = payload

    if has_tdu:
        try:
            count = count_tduworld()
            if count is None:
                raise RuntimeError("Strona nie udostępniła licznika PS3")
            save_count("test drive unlimited 2", count, "TDU World · PS3")
        except Exception as exc:
            print(f"SKIP TDU World: {exc}")

    if buzz_title:
        try:
            count = count_buzz_ps3()
            if count is None:
                raise RuntimeError("Strona nie udostępniła osobnej liczby PS3")
            save_count(buzz_title, count, "Buzz! Revival · PS3")
        except Exception as exc:
            print(f"SKIP Buzz! Revival: {exc}")

    if has_bfbc2:
        servers: list[dict] = []
        for name, url in BFBC2_SERVERS.items():
            try:
                servers.append({"name": name, "players": count_psrestored(url)})
            except Exception as exc:
                print(f"SKIP PS Restored {name}: {exc}")
        if servers:
            save_count("battlefield: bad company 2", sum(s["players"] for s in servers), "PS Restored · PSN / PS3", servers=servers)

    # Keep a last successful reading for up to 12 hours if a source is temporarily unavailable.
    for key, old in previous.items():
        if key in results or not isinstance(old, dict):
            continue
        try:
            age = (datetime.now(timezone.utc) - datetime.fromisoformat(old["checkedAt"].replace("Z", "+00:00"))).total_seconds()
        except (KeyError, ValueError, TypeError):
            continue
        if age < 12 * 60 * 60:
            results[key] = {**old, "stale": True}

    OUTPUT.write_text(json.dumps({"checkedAt": now, "games": results}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(results)} supported counts")


if __name__ == "__main__":
    try:
        main()
    except (URLError, TimeoutError, RuntimeError) as error:
        print(f"Count refresh failed: {error}", file=sys.stderr)
        raise
