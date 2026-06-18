import json
from pathlib import Path


BASE_DATA = Path("data")
RAW_DIR = BASE_DATA / "raw"
PROCESSED_DIR = BASE_DATA / "processed"


def ensure_structure() -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def raw_path(name: str) -> Path:
    return RAW_DIR / f"{name}_raw.json"


def processed_path(name: str) -> Path:
    return PROCESSED_DIR / f"{name}_processed.json"


def file_exists(path: Path) -> bool:
    return path.exists()


def read_json(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path: Path, data: dict) -> None:
    ensure_structure()
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)