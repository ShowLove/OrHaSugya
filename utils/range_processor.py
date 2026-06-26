# =========================
# FILE: utils/range_processor.py
# =========================

import time

from link_getter.json_reader import load_tractate_data

from utils.berakhot_processor import (
    process_daf_if_missing
)

from utils.app_state import (
    get_current_tractate
)

from utils.constants import (
    get_tractate_metadata_file
)


def parse_daf(daf: str) -> int:
    return int(daf[:-1])


def build_daf_list(start: int, end: int) -> list:
    dafs = []

    for n in range(start, end + 1):
        dafs.append(f"{n}a")
        dafs.append(f"{n}b")

    return dafs


def process_daf_range(
    start: str,
    end: str,
    tractate: str | None = None
) -> list:

    if tractate is None:
        tractate = get_current_tractate()

    start_num = parse_daf(start)
    end_num = parse_daf(end)

    data = load_tractate_data(
        str(
            get_tractate_metadata_file(
                tractate
            )
        )
    )

    min_daf = data["daf_range"]["start"]
    max_daf = data["daf_range"]["end"]

    if start_num < min_daf or end_num > max_daf:
        print("[ERROR] Range out of bounds")
        return []

    dafs = build_daf_list(
        start_num,
        end_num
    )

    results = []

    for i, daf in enumerate(
        dafs,
        start=1
    ):
        print(
            f"[INFO] ({i}/{len(dafs)}) "
            f"Processing {tractate} {daf}"
        )

        try:
            result = process_daf_if_missing(
                daf,
                tractate
            )

            results.append({
                "daf": daf,
                "data": result
            })

        except Exception as e:
            print(f"[ERROR] Failed {daf}: {e}")

        time.sleep(0.75)

    return results


def process_full_book(
    tractate: str | None = None
):

    if tractate is None:
        tractate = get_current_tractate()

    data = load_tractate_data(
        str(
            get_tractate_metadata_file(
                tractate
            )
        )
    )

    start = data["daf_range"]["start"]
    end = data["daf_range"]["end"]

    print(
        f"[INFO] Processing full {tractate}: "
        f"{start} → {end}"
    )

    return process_daf_range(
        f"{start}a",
        f"{end}a",
        tractate
    )