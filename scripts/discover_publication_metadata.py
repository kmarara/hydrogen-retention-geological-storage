#!/usr/bin/env python3
"""Retrieve publication metadata from Crossref and OpenAlex by DOI.

This discovers and records scholarly metadata; it does NOT retrieve or create
experimental IFT measurements. Supplementary data must be downloaded from the
publisher/repository and independently checked.
"""
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

USER_AGENT = "HydrogenBrineIFTBenchmark/0.1 (research metadata discovery)"


def get_json(url: str, timeout: int = 30) -> dict:
    request = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    with urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def retrieve_crossref(doi: str, mailto: str | None) -> dict:
    url = "https://api.crossref.org/works/" + quote(doi, safe="")
    if mailto:
        url += "?mailto=" + quote(mailto, safe="")
    try:
        payload = get_json(url)
        message = payload.get("message", {})
        return {
            "status": "ok",
            "source": "Crossref",
            "doi": message.get("DOI"),
            "title": message.get("title", []),
            "container_title": message.get("container-title", []),
            "published": message.get("published"),
            "author": message.get("author", []),
            "URL": message.get("URL"),
            "link": message.get("link", []),
        }
    except (HTTPError, URLError, TimeoutError, ValueError) as exc:
        return {"status": "error", "source": "Crossref", "error": str(exc)}


def retrieve_openalex(doi: str) -> dict:
    # OpenAlex accepts a DOI URL as the Works identifier.
    url = "https://api.openalex.org/works/https://doi.org/" + quote(doi, safe="/")
    try:
        payload = get_json(url)
        locations = payload.get("locations", [])
        return {
            "status": "ok",
            "source": "OpenAlex",
            "id": payload.get("id"),
            "doi": payload.get("doi"),
            "title": payload.get("title"),
            "publication_year": payload.get("publication_year"),
            "open_access": payload.get("open_access"),
            "best_oa_location": payload.get("best_oa_location"),
            "locations": locations,
            "primary_location": payload.get("primary_location"),
        }
    except (HTTPError, URLError, TimeoutError, ValueError) as exc:
        return {"status": "error", "source": "OpenAlex", "error": str(exc)}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("dois", nargs="+", help="One or more publication DOIs")
    parser.add_argument("--mailto", help="Contact email for Crossref polite-pool requests")
    parser.add_argument("--out", type=Path, default=Path("data/metadata/publication_metadata.json"))
    args = parser.parse_args()

    records = []
    for doi in args.dois:
        doi = doi.strip().removeprefix("https://doi.org/").removeprefix("http://doi.org/")
        if not doi or "/" not in doi:
            raise SystemExit(f"Not a plausible DOI: {doi!r}")
        crossref = retrieve_crossref(doi, args.mailto)
        time.sleep(0.2)
        openalex = retrieve_openalex(doi)
        records.append({
            "requested_doi": doi,
            "retrieved_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "crossref": crossref,
            "openalex": openalex,
            "scope_note": "Bibliographic metadata only; not experimental IFT observations.",
        })

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(records, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.out), "records": len(records)}, indent=2))


if __name__ == "__main__":
    main()
