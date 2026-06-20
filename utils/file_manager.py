import json
import os
from utils.constants import (
    RAW_DIR,
    PROCESSED_DIR,
    RAW_FILE_PREFIX,
    RAW_FILE_SUFFIX,
    PROCESSED_FILE_SUFFIX
)


def ensure_dirs() -> None:
    os.makedirs(RAW_DIR, exist_ok=True)
    os.makedirs(PROCESSED_DIR, exist_ok=True)


def save_raw_response(daf: str, data: dict) -> str:
    ensure_dirs()

    filename = f"{RAW_FILE_PREFIX}{daf.lower()}{RAW_FILE_SUFFIX}"
    path = os.path.join(RAW_DIR, filename)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return path


def load_raw_response(daf: str) -> dict:
    ensure_dirs()

    path = os.path.join(
        RAW_DIR,
        f"{RAW_FILE_PREFIX}{daf.lower()}{RAW_FILE_SUFFIX}"
    )

    if not os.path.exists(path):
        return None

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_processed(daf: str, data: dict) -> str:
    ensure_dirs()

    path = os.path.join(
        PROCESSED_DIR,
        f"{RAW_FILE_PREFIX}{daf.lower()}{PROCESSED_FILE_SUFFIX}"
    )

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return path