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
# LOGGING HELPERS
# ----------------------------

def log_info(msg: str) -> None:
    print(f"[INFO] {msg}")


def log_success(msg: str) -> None:
    print(f"[SUCCESS] {msg}")


def log_error(msg: str) -> None:
    print(f"[ERROR] {msg}")


# ----------------------------
# RAW HANDLING
# ----------------------------

def get_or_create_raw(tractate: str, daf: str) -> dict:

    name = f"{tractate.lower()}_{daf}"
    path = raw_path(name)

    if file_exists(path):
        log_info(f"Loading cached raw {tractate} {daf}")
        return read_json(path)

    log_info(f"Fetching from Sefaria: {tractate} {daf}")

    ref = f"{tractate}.{daf}"
    data = fetch_daf_data(ref)

    write_json(path, data)

    log_success(f"Saved raw {tractate} {daf}")

    return data


# ----------------------------
# PROCESSING
# ----------------------------

def process_raw_to_processed(raw: dict) -> dict:

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

    try:
        log_info(f"Processing {tractate} {daf}")

        raw = get_or_create_raw(tractate, daf)
        processed = process_raw_to_processed(raw)

        save_processed(tractate, daf, processed)

        log_success(f"Saved processed {tractate} {daf}")

        return processed

    except Exception as e:
        log_error(f"{tractate} {daf} failed: {e}")
        raise


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

    total = (end_num - start_num + 1) * 2
    done = 0

    for num in range(start_num, end_num + 1):

        for suffix in ("a", "b"):
            daf = f"{num}{suffix}"

            log_info(f"[{done+1}/{total}] Processing {tractate} {daf}")

            try:
                result = process_single_daf(tractate, daf)
                results.append(result)

                log_success(f"Completed {tractate} {daf}")

            except Exception as e:
                log_error(f"{tractate} {daf} error: {e}")

            done += 1
            time.sleep(delay)

    return results