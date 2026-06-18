import time
from typing import List

from utils.file_manager import (
    raw_path,
    processed_path,
    file_exists,
    read_json,
    write_json
)

from api.sefaria_client import fetch_daf_data


# ----------------------------
# RAW HANDLING
# ----------------------------

def get_or_create_raw(tractate: str, daf: str) -> dict:
    """
    Ensure raw exists.
    If not → fetch from Sefaria → save.
    """

    name = f"{tractate.lower()}_{daf}"
    path = raw_path(name)

    if file_exists(path):
        return read_json(path)

    ref = f"{tractate}.{daf}"
    data = fetch_daf_data(ref)

    write_json(path, data)
    return data


# ----------------------------
# PROCESSING
# ----------------------------

def process_raw_to_processed(raw: dict) -> dict:
    """
    Minimal clean structure (expand later easily)
    """

    return {
        "ref": raw.get("ref"),
        "heRef": raw.get("heRef"),
        "title": raw.get("title"),
        "heTitle": raw.get("heTitle"),
        "text": raw.get("text", []),
        "he": raw.get("he", []),
        "versions": raw.get("versions", [])
    }


def save_processed(tractate: str, daf: str, processed: dict) -> None:
    name = f"{tractate.lower()}_{daf}"
    path = processed_path(name)
    write_json(path, processed)


def process_single_daf(tractate: str, daf: str) -> dict:
    raw = get_or_create_raw(tractate, daf)
    processed = process_raw_to_processed(raw)
    save_processed(tractate, daf, processed)
    return processed


# ----------------------------
# RANGE PROCESSING
# ----------------------------

def daf_to_int(daf: str) -> int:
    return int(daf[:-1])


def process_range(
    tractate: str,
    start: str,
    end: str,
    start_int: int,
    end_int: int,
    delay: float = 0.5
) -> List[dict]:

    start_num = daf_to_int(start)
    end_num = daf_to_int(end)

    if start_num < start_int:
        raise ValueError("Start daf out of bounds")

    if end_num > end_int:
        raise ValueError("End daf out of bounds")

    results = []

    for num in range(start_num, end_num + 1):

        for suffix in ("a", "b"):
            daf = f"{num}{suffix}"

            try:
                result = process_single_daf(tractate, daf)
                results.append(result)
                time.sleep(delay)

            except Exception as e:
                print(f"Skipping {daf}: {e}")

    return results