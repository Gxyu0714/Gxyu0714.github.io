#!/usr/bin/env python3
"""Detect newly listed publications and create bilingual News posts.

Primary source: ORCID public API (stable).
Optional secondary: Google Scholar citations page (best-effort; often blocked).

Bootstrap behavior:
  - If _data/known_publications.yml is missing/empty, record current works and exit
    without creating news (avoids dumping your full history on first run).
  - Later runs only create news for titles not already recorded.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KNOWN_PATH = ROOT / "_data" / "known_publications.yml"
NEWS_DIR = ROOT / "_news"
CONFIG_PATH = ROOT / "_config.yml"

ORCID_ID = os.environ.get("ORCID_ID", "").strip()
SCHOLAR_USER = os.environ.get("SCHOLAR_USERID", "").strip()
USER_AGENT = os.environ.get(
    "SYNC_USER_AGENT",
    "Gxyu0714-site-sync/1.0 (mailto:guoxinyu00714@gmail.com)",
)


def load_ids_from_config() -> tuple[str, str]:
    orcid = ORCID_ID
    scholar = SCHOLAR_USER
    if CONFIG_PATH.exists():
        text = CONFIG_PATH.read_text(encoding="utf-8")
        if not orcid:
            m = re.search(r"^orcid_id:\s*([^\s#]+)", text, re.M)
            if m:
                orcid = m.group(1).strip()
        if not scholar:
            m = re.search(r"^scholar_userid:\s*([^\s#]+)", text, re.M)
            if m:
                scholar = m.group(1).strip()
    return orcid, scholar


def normalize_title(title: str) -> str:
    t = title.casefold()
    t = re.sub(r"\s+", " ", t)
    t = re.sub(r"[^\w\s]", "", t)
    return t.strip()


def slugify(title: str, limit: int = 60) -> str:
    s = title.casefold()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = s.strip("-")[:limit].strip("-")
    return s or "publication"


def http_get_json(url: str, headers: dict | None = None):
    req_headers = {"User-Agent": USER_AGENT, "Accept": "application/json"}
    if headers:
        req_headers.update(headers)
    req = urllib.request.Request(url, headers=req_headers)
    with urllib.request.urlopen(req, timeout=45) as resp:
        return json.load(resp)


def http_get_text(url: str) -> str:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (compatible; Gxyu0714Bot/1.0; "
                "+https://gxyu0714.github.io)"
            ),
            "Accept-Language": "en-US,en;q=0.9",
        },
    )
    with urllib.request.urlopen(req, timeout=45) as resp:
        return resp.read().decode("utf-8", errors="replace")


def fetch_orcid_works(orcid: str) -> list[dict]:
    if not orcid:
        return []
    url = f"https://pub.orcid.org/v3.0/{orcid}/works"
    data = http_get_json(url)
    works = []
    for group in data.get("group", []):
        summaries = group.get("work-summary") or []
        if not summaries:
            continue
        s = summaries[0]
        title = ((s.get("title") or {}).get("title") or {}).get("value")
        if not title:
            continue
        year = ((s.get("publication-date") or {}).get("year") or {}).get("value")
        put_code = s.get("put-code")
        ext_ids = ((s.get("external-ids") or {}).get("external-id")) or []
        doi = None
        for ext in ext_ids:
            if (ext.get("external-id-type") or "").lower() == "doi":
                doi = ext.get("external-id-value")
                break
        works.append(
            {
                "id": f"orcid:{put_code}" if put_code else f"title:{normalize_title(title)}",
                "title": title.strip(),
                "year": str(year) if year else None,
                "doi": doi,
                "source": "orcid",
            }
        )
    return works


def fetch_scholar_works(scholar_id: str) -> list[dict]:
    """Best-effort scrape. Returns [] if Google blocks the request."""
    if not scholar_id:
        return []
    url = (
        "https://scholar.google.com/citations?"
        + urllib.parse.urlencode({"user": scholar_id, "hl": "en", "pagesize": "100"})
    )
    try:
        html = http_get_text(url)
    except Exception as exc:  # noqa: BLE001
        print(f"[warn] Google Scholar fetch failed: {exc}", file=sys.stderr)
        return []

    # Citation rows: <a class="gsc_a_at" ...>Title</a>
    titles = re.findall(
        r'<a[^>]*class="gsc_a_at"[^>]*>(.*?)</a>',
        html,
        flags=re.I | re.S,
    )
    years = re.findall(r'<span class="gsc_a_h gsc_a_hc gs_ibl">(\d{4})</span>', html)
    cleaned = []
    for i, raw in enumerate(titles):
        title = re.sub(r"<[^>]+>", "", raw)
        title = re.sub(r"\s+", " ", title).strip()
        if not title:
            continue
        year = years[i] if i < len(years) else None
        cleaned.append(
            {
                "id": f"scholar:{hashlib.sha1(normalize_title(title).encode()).hexdigest()[:12]}",
                "title": title,
                "year": year,
                "doi": None,
                "source": "google_scholar",
            }
        )
    if not cleaned:
        print("[warn] Google Scholar returned no titles (likely blocked).", file=sys.stderr)
    return cleaned


def load_known() -> dict:
    if not KNOWN_PATH.exists():
        return {"updated_at": None, "publications": []}
    text = KNOWN_PATH.read_text(encoding="utf-8")
    # Minimal YAML subset parser for our file shape.
    pubs = []
    current = None
    updated_at = None
    for line in text.splitlines():
        if line.startswith("updated_at:"):
            updated_at = line.split(":", 1)[1].strip().strip("'\"") or None
        elif line.strip().startswith("- id:"):
            if current:
                pubs.append(current)
            current = {"id": line.split(":", 1)[1].strip().strip("'\"")}
        elif current is not None and line.strip().startswith("title:"):
            val = line.split(":", 1)[1].strip()
            if val.startswith("'") or val.startswith('"'):
                val = val[1:-1]
            current["title"] = val
            current["key"] = normalize_title(val)
        elif current is not None and line.strip().startswith("key:"):
            current["key"] = line.split(":", 1)[1].strip().strip("'\"")
        elif current is not None and line.strip().startswith("source:"):
            current["source"] = line.split(":", 1)[1].strip().strip("'\"")
        elif current is not None and line.strip().startswith("year:"):
            y = line.split(":", 1)[1].strip().strip("'\"")
            current["year"] = y if y and y != "null" else None
    if current:
        pubs.append(current)
    return {"updated_at": updated_at, "publications": pubs}


def dump_known(pubs: list[dict]) -> None:
    lines = [
        f"updated_at: '{datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}'",
        "publications:",
    ]
    # Stable sort for cleaner diffs
    for p in sorted(pubs, key=lambda x: (x.get("year") or "", normalize_title(x.get("title") or ""))):
        title = (p.get("title") or "").replace("'", "''")
        lines.append(f"  - id: '{p.get('id')}'")
        lines.append(f"    title: '{title}'")
        lines.append(f"    key: '{normalize_title(p.get('title') or '')}'")
        lines.append(f"    source: '{p.get('source') or 'unknown'}'")
        year = p.get("year")
        lines.append(f"    year: '{year}'" if year else "    year: null")
    KNOWN_PATH.parent.mkdir(parents=True, exist_ok=True)
    KNOWN_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def merge_works(*groups: list[dict]) -> list[dict]:
    by_key: dict[str, dict] = {}
    for group in groups:
        for w in group:
            key = normalize_title(w["title"])
            if not key:
                continue
            if key not in by_key:
                by_key[key] = dict(w)
                by_key[key]["key"] = key
            else:
                # Prefer ORCID metadata when available
                if by_key[key].get("source") != "orcid" and w.get("source") == "orcid":
                    by_key[key].update(w)
                    by_key[key]["key"] = key
                elif not by_key[key].get("year") and w.get("year"):
                    by_key[key]["year"] = w["year"]
                if not by_key[key].get("doi") and w.get("doi"):
                    by_key[key]["doi"] = w["doi"]
    return list(by_key.values())


def write_news(work: dict) -> Path:
    NEWS_DIR.mkdir(parents=True, exist_ok=True)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    slug = slugify(work["title"])
    path = NEWS_DIR / f"{today}-{slug}.md"
    n = 2
    while path.exists():
        path = NEWS_DIR / f"{today}-{slug}-{n}.md"
        n += 1

    title = work["title"].strip()
    year = work.get("year") or "recently"
    doi = work.get("doi")
    link = f"https://doi.org/{doi}" if doi else None

    en_link = f' <a href="{link}">paper</a>' if link else ""
    zh_link = f' <a href="{link}">论文链接</a>' if link else ""

    content = f"""---
layout: post
date: {today} 12:00:00 +0800
inline: true
related_posts: false
---

<span class="lang-en">New publication ({year}): <em>{title}</em>.{en_link}</span>
<span class="lang-zh">新发表论文（{year}）：<em>{title}</em>。{zh_link}</span>
"""
    path.write_text(content, encoding="utf-8")
    return path


def main() -> int:
    orcid, scholar = load_ids_from_config()
    print(f"[info] ORCID={orcid or '(none)'} Scholar={scholar or '(none)'}")

    orcid_works = []
    scholar_works = []
    try:
        orcid_works = fetch_orcid_works(orcid)
        print(f"[info] ORCID works: {len(orcid_works)}")
    except Exception as exc:  # noqa: BLE001
        print(f"[error] ORCID fetch failed: {exc}", file=sys.stderr)

    try:
        scholar_works = fetch_scholar_works(scholar)
        print(f"[info] Scholar works: {len(scholar_works)}")
    except Exception as exc:  # noqa: BLE001
        print(f"[warn] Scholar fetch error: {exc}", file=sys.stderr)

    works = merge_works(orcid_works, scholar_works)
    if not works:
        print("[error] No publications fetched from any source.", file=sys.stderr)
        return 1

    known = load_known()
    known_pubs = known.get("publications") or []
    known_keys = {p.get("key") or normalize_title(p.get("title") or "") for p in known_pubs}
    known_keys.discard("")

    # Bootstrap: record everything, create no news.
    if not known_keys:
        dump_known(works)
        print(f"[info] Bootstrapped {len(works)} publications into {KNOWN_PATH}")
        print("[info] No news created on first run.")
        return 0

    new_works = [w for w in works if normalize_title(w["title"]) not in known_keys]
    created = []
    for w in sorted(new_works, key=lambda x: (x.get("year") or "", x["title"])):
        path = write_news(w)
        created.append(path)
        print(f"[info] Created news: {path.relative_to(ROOT)}")

    # Refresh known set to full current catalog
    dump_known(works)

    if created:
        print(f"[info] Added {len(created)} news item(s).")
    else:
        print("[info] No new publications.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
