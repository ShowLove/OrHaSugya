# =========================
# FILE: utils/file_manager.py
# =========================

import json
import os
from utils.constants import (
    RAW_DIR,
    PROCESSED_DIR,
    RAW_FILE_PREFIX,
    RAW_FILE_SUFFIX,
    PROCESSED_FILE_SUFFIX,
    DEFAULT_TRACTATE
)


def ensure_dirs():
    os.makedirs(RAW_DIR, exist_ok=True)
    os.makedirs(PROCESSED_DIR, exist_ok=True)


def _prefix(tractate: str) -> str:
    return f"{tractate.lower()}_" if tractate else RAW_FILE_PREFIX


def save_raw_response(daf: str, data: dict, tractate: str = DEFAULT_TRACTATE) -> str:
    ensure_dirs()

    filename = f"{_prefix(tractate)}{daf.lower()}{RAW_FILE_SUFFIX}"
    path = os.path.join(RAW_DIR, filename)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return path


def load_raw_response(daf: str, tractate: str = DEFAULT_TRACTATE) -> dict:
    ensure_dirs()

    path = os.path.join(
        RAW_DIR,
        f"{_prefix(tractate)}{daf.lower()}{RAW_FILE_SUFFIX}"
    )

    if not os.path.exists(path):
        return None

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_processed(daf: str, data: dict, tractate: str = DEFAULT_TRACTATE) -> str:
    ensure_dirs()

    path = os.path.join(
        PROCESSED_DIR,
        f"{_prefix(tractate)}{daf.lower()}{PROCESSED_FILE_SUFFIX}"
    )

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return path