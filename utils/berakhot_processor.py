import time
from utils.file_manager import (
    save_raw_response,
    load_raw_response,
    save_processed,
)

from api.sefaria_client import fetch_daf_data


def process_single_daf(daf: str) -> dict:
    """
    Full pipeline: fetch → save raw → process → save processed
    """

    print(f"\n[PROCESS] Starting daf {daf}")

    raw = fetch_daf_data(daf)

    # IMPORTANT DEBUG CHECK
    if not raw or (raw.get("text") == [] and raw.get("he") == []):
        print(f"[WARNING] Empty or invalid data returned for {daf}")
        print(f"[DEBUG KEYS] {list(raw.keys())}")
        save_raw_response(daf, raw)
        return None

    save_raw_response(daf, raw)
    print(f"[OK] Raw saved: {daf}")

    processed = process_raw_to_structured(raw)

    save_processed(daf, processed)
    print(f"[OK] Processed saved: {daf}")

    time.sleep(0.5)

    return processed


def process_raw_to_structured(raw: dict) -> dict:
    """
    Normalize Sefaria output across possible formats.
    """

    return {
        "ref": raw.get("ref"),
        "heRef": raw.get("heRef"),

        # robust extraction (Sefaria is inconsistent)
        "english": extract_english(raw),
        "hebrew": extract_hebrew(raw),

        "debug_keys": list(raw.keys()) if isinstance(raw, dict) else []
    }


def extract_english(raw: dict):
    """
    Try multiple possible Sefaria formats.
    """

    if not isinstance(raw, dict):
        return []

    return (
        raw.get("text")
        or raw.get("texts")
        or raw.get("english")
        or []
    )


def extract_hebrew(raw: dict):
    """
    Try multiple possible Hebrew formats.
    """

    if not isinstance(raw, dict):
        return []

    return (
        raw.get("he")
        or raw.get("heText")
        or raw.get("hebrew")
        or []
    )


def process_daf_if_missing(daf: str) -> dict:
    """
    Use cached raw if available, otherwise fetch.
    """

    existing = load_raw_response(daf)

    if existing:
        print(f"[CACHE] Using existing raw for {daf}")
        return process_raw_to_structured(existing)

    print(f"[FETCH] No cache for {daf}")
    return process_single_daf(daf)