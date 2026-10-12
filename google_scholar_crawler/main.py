"""Fetch public Google Scholar citation totals without third-party packages."""

import argparse
from datetime import datetime, timezone
from html import unescape
import json
import os
from pathlib import Path
import re
import time
from urllib.parse import urlencode
from urllib.request import Request, urlopen


def parse_citation_count(document):
    table = re.search(
        r'<table\b[^>]*\bid=["\']gsc_rsb_st["\'][^>]*>(.*?)</table>',
        document, re.IGNORECASE | re.DOTALL,
    )
    if not table:
        raise ValueError("Google Scholar statistics table not found; cached data is retained")
    cells = re.findall(
        r'<td\b[^>]*\bclass=["\'][^"\']*\bgsc_rsb_std\b[^"\']*["\'][^>]*>(.*?)</td>',
        table.group(1), re.IGNORECASE | re.DOTALL,
    )
    if not cells:
        raise ValueError("Google Scholar citation total not found")
    value = unescape(re.sub(r"<[^>]+>", "", cells[0])).strip()
    if not re.fullmatch(r"[0-9][0-9,\s]*", value):
        raise ValueError("Invalid Google Scholar citation total")
    return int(re.sub(r"[,\s]", "", value))


def fetch_stats(author_id):
    if not re.fullmatch(r"[A-Za-z0-9_-]+", author_id):
        raise ValueError("Invalid Google Scholar author ID")
    url = "https://scholar.google.com/citations?" + urlencode({"user": author_id, "hl": "en"})
    request = Request(url, headers={"User-Agent": "Mozilla/5.0", "Accept-Language": "en-US,en;q=0.9"})
    for attempt in range(2):
        try:
            with urlopen(request, timeout=20) as response:
                document = response.read().decode("utf-8")
            count = parse_citation_count(document)
            return {
                "scholar_id": author_id,
                "citedby": count,
                "updated": datetime.now(timezone.utc).isoformat(),
                "publications": {},
            }
        except (OSError, ValueError):
            if attempt:
                raise
            time.sleep(3)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=Path("results"))
    args = parser.parse_args()
    stats = fetch_stats(os.environ.get("GOOGLE_SCHOLAR_ID", "ehxjrc8AAAAJ"))
    args.output_dir.mkdir(parents=True, exist_ok=True)
    outputs = {
        "gs_data.json": stats,
        "gs_data_shieldsio.json": {
            "schemaVersion": 1, "label": "citations", "message": str(stats["citedby"]),
        },
    }
    for name, data in outputs.items():
        target = args.output_dir / name
        temporary = target.with_suffix(".tmp")
        temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        temporary.replace(target)
    print(f"Google Scholar citation total: {stats['citedby']}")


if __name__ == "__main__":
    main()
