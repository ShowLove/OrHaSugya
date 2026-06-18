import time
from utils.file_manager import (
    save_raw_response,
    load_raw_response,
    save_processed,
)

from api.sefaria_client import fetch_daf_data


def process_single_daf(daf: str) -> dict:
    """
    Fetch + save + process a single daf.
    """

    print(f"[INFO] Processing daf: {daf}")

    try:
        raw = fetch_daf_data(daf)
        save_raw_response(daf, raw)
        print(f"[OK] Raw saved for {daf}")

        processed = process_raw_to_structured(raw)
        save_processed(daf, processed)

        print(f"[OK] Processed saved for {daf}")

        time.sleep(0.5)  # gentle pacing for Sefaria etiquette

        return processed

    except Exception as e:
        print(f"[ERROR] Failed processing {daf}: {e}")
        return None


def process_raw_to_structured(raw: dict) -> dict:
    """
    Convert raw Sefaria response into structured format.
    (currently pass-through but ready for expansion)
    """

    return {
        "ref": raw.get("ref"),
        "heRef": raw.get("heRef"),
        "english": raw.get("text", []),
        "hebrew": raw.get("he", []),
    }


def process_daf_if_missing(daf: str) -> dict:
    """
    If raw exists → reuse
    If not → fetch it
    Then process
    """

    existing = load_raw_response(daf)

    if existing:
        print(f"[INFO] Raw exists for {daf}, using cached file")
        return process_raw_to_structured(existing)

    print(f"[INFO] Raw missing for {daf}, fetching...")
    return process_single_daf(daf)