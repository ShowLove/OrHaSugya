# =========================
# FILE: utils/berakhot_processor.py
# =========================

import time

from utils.file_manager import (
    save_raw_response,
    load_raw_response,
    save_processed,
)

from api.sefaria_client import (
    fetch_daf_data
)

from utils.app_state import (
    get_current_tractate
)


def process_single_daf(
    daf: str,
    tractate: str | None = None
) -> dict:
    """
    Full pipeline: fetch → save raw → process → save processed.
    Defaults to the currently selected tractate.
    """

    if tractate is None:
        tractate = get_current_tractate()

    print(f"\n[PROCESS] Starting {tractate} {daf}")

    raw = fetch_daf_data(
        daf,
        tractate
    )

    if not raw or (
        raw.get("text") == [] and
        raw.get("he") == []
    ):
        print(
            f"[WARNING] Empty or invalid data returned for {daf}"
        )

        print(
            f"[DEBUG KEYS] {list(raw.keys())}"
        )

        save_raw_response(
            daf,
            raw,
            tractate
        )

        return None

    save_raw_response(
        daf,
        raw,
        tractate
    )

    print(f"[OK] Raw saved: {daf}")

    processed = process_raw_to_structured(
        raw
    )

    save_processed(
        daf,
        processed,
        tractate
    )

    print(f"[OK] Processed saved: {daf}")

    time.sleep(0.5)

    return processed


def process_raw_to_structured(raw: dict) -> dict:
    return {
        "ref": raw.get("ref"),
        "heRef": raw.get("heRef"),
        "english": extract_english(raw),
        "hebrew": extract_hebrew(raw),
        "debug_keys": list(raw.keys()) if isinstance(raw, dict) else []
    }


def extract_english(raw: dict):
    if not isinstance(raw, dict):
        return []

    return (
        raw.get("text") or
        raw.get("texts") or
        raw.get("english") or
        []
    )


def extract_hebrew(raw: dict):
    if not isinstance(raw, dict):
        return []

    return (
        raw.get("he") or
        raw.get("heText") or
        raw.get("hebrew") or
        []
    )


def process_daf_if_missing(
    daf: str,
    tractate: str | None = None
) -> dict:
    """
    Use cached raw if available, otherwise fetch.
    Defaults to the currently selected tractate.
    """

    if tractate is None:
        tractate = get_current_tractate()

    existing = load_raw_response(
        daf,
        tractate
    )

    if existing:
        print(
            f"[CACHE] Using existing raw for {tractate} {daf}"
        )

        return process_raw_to_structured(
            existing
        )

    print(f"[FETCH] No cache for {tractate} {daf}")

    return process_single_daf(
        daf,
        tractate
    )