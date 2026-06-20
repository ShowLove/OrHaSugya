import time
from link_getter.json_reader import load_tractate_data
from utils.berakhot_processor import process_daf_if_missing


def parse_daf(daf: str) -> int:
    """
    Convert '10a' -> 10
    """
    return int(daf[:-1])


def build_daf_list(start: int, end: int) -> list:
    """
    Build full daf list including a + b pages.
    Example:
        4 → 4a, 4b
        5 → 5a, 5b
    """
    dafs = []
    for n in range(start, end + 1):
        dafs.append(f"{n}a")
        dafs.append(f"{n}b")
    return dafs


def process_daf_range(start: str, end: str) -> list:
    """
    Process range like 4a → 10a safely.
    """
    start_num = parse_daf(start)
    end_num = parse_daf(end)

    data = load_tractate_data("data/berakhot.json")

    min_daf = data["daf_range"]["start"]
    max_daf = data["daf_range"]["end"]

    if start_num < min_daf or end_num > max_daf:
        print("[ERROR] Range out of bounds")
        return []

    dafs = build_daf_list(start_num, end_num)

    results = []

    for i, daf in enumerate(dafs, start=1):

        print(f"[INFO] ({i}/{len(dafs)}) Processing {daf}")

        try:
            result = process_daf_if_missing(daf)

            results.append({
                "daf": daf,
                "data": result
            })

        except Exception as e:
            print(f"[ERROR] Failed {daf}: {e}")

        time.sleep(0.75)

    return results


def process_full_book():
    """
    Process entire Berakhot using the same pipeline as range processing.
    """
    data = load_tractate_data("data/berakhot.json")

    start = data["daf_range"]["start"]
    end = data["daf_range"]["end"]

    print(f"[INFO] Processing full Berakhot: {start} → {end}")

    return process_daf_range(f"{start}a", f"{end}a")