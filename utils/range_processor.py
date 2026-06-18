import time
from link_getter.json_reader import load_tractate_data
from utils.berakhot_processor import process_daf_if_missing


def parse_daf(daf: str) -> int:
    return int(daf[:-1])


def get_all_dafs():
    data = load_tractate_data("data/berakhot.json")
    return list(range(data["daf_range"]["start"], data["daf_range"]["end"] + 1))


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

    results = []

    for n in range(start_num, end_num + 1):
        daf = f"{n}a"

        print(f"[INFO] Starting daf {daf}")

        result = process_daf_if_missing(daf)

        results.append({
            "daf": daf,
            "data": result
        })

        time.sleep(0.75)  # avoid hammering API

    return results


def process_full_book():
    """
    Process entire Berakhot.
    """

    data = load_tractate_data("data/berakhot.json")
    start = data["daf_range"]["start"]
    end = data["daf_range"]["end"]

    return process_daf_range(f"{start}a", f"{end}a")