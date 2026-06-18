import json
import os


RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"


def ensure_dirs() -> None:
    os.makedirs(RAW_DIR, exist_ok=True)
    os.makedirs(PROCESSED_DIR, exist_ok=True)


def save_raw_response(daf: str, data: dict) -> str:
    """
    Save raw Sefaria response.
    """
    ensure_dirs()

    filename = f"berakhot_{daf.lower()}_raw.json"
    path = os.path.join(RAW_DIR, filename)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return path


def load_raw_response(daf: str) -> dict:
    ensure_dirs()

    path = os.path.join(RAW_DIR, f"berakhot_{daf.lower()}_raw.json")

    if not os.path.exists(path):
        return None

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_processed(daf: str, data: dict) -> str:
    ensure_dirs()

    path = os.path.join(PROCESSED_DIR, f"berakhot_{daf.lower()}_processed.json")

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return path