# =========================
# FILE: utils/file_manager.py
# =========================

import json
import os

from utils.constants import (
    DEFAULT_TRACTATE,
    RAW_FILE_SUFFIX,
    PROCESSED_FILE_SUFFIX,
    get_raw_dir,
    get_processed_dir
)


def ensure_dirs(
    tractate: str = DEFAULT_TRACTATE
):
    os.makedirs(
        get_raw_dir(tractate),
        exist_ok=True
    )

    os.makedirs(
        get_processed_dir(tractate),
        exist_ok=True
    )


def save_raw_response(
    daf: str,
    data: dict,
    tractate: str = DEFAULT_TRACTATE
) -> str:

    ensure_dirs(tractate)

    raw_dir = get_raw_dir(tractate)

    path = os.path.join(
        raw_dir,
        f"{daf.lower()}{RAW_FILE_SUFFIX}"
    )

    with open(path, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=2
        )

    return path


def load_raw_response(
    daf: str,
    tractate: str = DEFAULT_TRACTATE
) -> dict:

    ensure_dirs(tractate)

    raw_dir = get_raw_dir(tractate)

    path = os.path.join(
        raw_dir,
        f"{daf.lower()}{RAW_FILE_SUFFIX}"
    )

    if not os.path.exists(path):
        return None

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_processed(
    daf: str,
    data: dict,
    tractate: str = DEFAULT_TRACTATE
) -> str:

    ensure_dirs(tractate)

    processed_dir = get_processed_dir(
        tractate
    )

    path = os.path.join(
        processed_dir,
        f"{daf.lower()}{PROCESSED_FILE_SUFFIX}"
    )

    with open(path, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=2
        )

    return path