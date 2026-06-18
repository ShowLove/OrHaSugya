import json
from pathlib import Path


DATA_FOLDER = Path("data")
RAW_FOLDER = DATA_FOLDER / "raw"
PROCESSED_FOLDER = DATA_FOLDER / "processed"


def ensure_data_directories() -> None:
    RAW_FOLDER.mkdir(parents=True, exist_ok=True)
    PROCESSED_FOLDER.mkdir(parents=True, exist_ok=True)


def build_raw_filename(tractate_name: str, daf_input: str) -> str:
    tractate = tractate_name.lower().replace(" ", "_")
    return f"{tractate}_{daf_input.lower()}_raw.json"


def save_raw_response(response_data: dict, tractate_name: str, daf_input: str) -> str:

    ensure_data_directories()

    filename = build_raw_filename(tractate_name, daf_input)
    file_path = RAW_FOLDER / filename

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(response_data, f, ensure_ascii=False, indent=4)

    return str(file_path)