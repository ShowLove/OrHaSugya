import time
import json
import os

from utils.file_utils import ensure_folder, load_json, save_json


RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"
INDEX_FILE = "data/berakhot.json"


# ---------------------------
# Helpers
# ---------------------------

def _parse_daf(daf: str):
    """
    Converts '4a' -> (4, 'a')
    """
    daf = daf.strip().lower()
    num = int("".join([c for c in daf if c.isdigit()]))
    side = "".join([c for c in daf if c.isalpha()])
    return num, side


def _daf_to_str(num: int, side: str) -> str:
    return f"{num}{side}"


def _in_range(current, start, end) -> bool:
    cur_n, cur_s = _parse_daf(current)
    start_n, start_s = _parse_daf(start)
    end_n, end_s = _parse_daf(end)

    # simple linear comparison (good enough for daf system)
    if cur_n < start_n or cur_n > end_n:
        return False

    if cur_n == start_n and cur_s < start_s:
        return False

    if cur_n == end_n and cur_s > end_s:
        return False

    return True


def _get_index_bounds():
    """
    Reads berakhot.json to get allowed range
    """
    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    start = data["daf_range"]["start"]
    end = data["daf_range"]["end"]

    return f"{start}a", f"{end}b"


# ---------------------------
# Core processor for one daf
# ---------------------------

def _process_single_daf(daf_ref: str):
    """
    Fetch raw file (if exists), process it, store processed version.
    """

    raw_path = os.path.join(RAW_DIR, f"{daf_ref}_raw.json")
    processed_path = os.path.join(PROCESSED_DIR, f"{daf_ref}_raw.json")

    if not os.path.exists(raw_path):
        print(f"[SKIP] Missing raw file: {daf_ref}")
        return

    raw_data = load_json(raw_path)

    processed = {
        "ref": raw_data.get("ref"),
        "heRef": raw_data.get("heRef"),
        "english": [],
        "hebrew_aramaic": []
    }

    for i, t in enumerate(raw_data.get("text", [])):
        processed["english"].append({"id": i, "text": t})

    for i, t in enumerate(raw_data.get("he", [])):
        processed["hebrew_aramaic"].append({"id": i, "text": t})

    save_json(processed_path, processed)

    print(f"[OK] Processed {daf_ref}")


# ---------------------------
# PUBLIC ENTRY FUNCTION
# ---------------------------

def process_range(start_daf: str, end_daf: str):
    """
    MAIN FUNCTION (called from main.py)

    - validates bounds
    - loops range safely
    - throttles requests
    """

    ensure_folder(PROCESSED_DIR)

    min_bound, max_bound = _get_index_bounds()

    # validate user request
    if not _in_range(start_daf, min_bound, max_bound):
        print(f"Start {start_daf} is out of bounds ({min_bound} - {max_bound})")
        return

    if not _in_range(end_daf, min_bound, max_bound):
        print(f"End {end_daf} is out of bounds ({min_bound} - {max_bound})")
        return

    start_n, start_s = _parse_daf(start_daf)
    end_n, end_s = _parse_daf(end_daf)

    print(f"Processing range: {start_daf} → {end_daf}")

    # iterate safely
    current_n = start_n

    while current_n <= end_n:
        for side in ["a", "b"]:
            current = _daf_to_str(current_n, side)

            if not _in_range(current, start_daf, end_daf):
                continue

            _process_single_daf(current)

            # polite throttling (important for Sefaria / API safety)
            time.sleep(0.4)

        current_n += 1

    print("Done processing range.")