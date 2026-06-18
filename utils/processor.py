import os

from .file_utils import (
    ensure_folder,
    load_json,
    save_json
)


RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"


def _transform_sefaria_raw(raw: dict) -> dict:
    """
    Converts raw Sefaria response into clean LLM-friendly format.
    """

    english = raw.get("text", [])
    hebrew = raw.get("he", [])

    processed = {
        "ref": raw.get("ref"),
        "heRef": raw.get("heRef"),

        "english": [],
        "hebrew_aramaic": []
    }

    for i, txt in enumerate(english):
        processed["english"].append({
            "id": i,
            "text": txt
        })

    for i, txt in enumerate(hebrew):
        processed["hebrew_aramaic"].append({
            "id": i,
            "text": txt
        })

    processed["alignment"] = {
        "type": "parallel",
        "length": max(len(english), len(hebrew))
    }

    return processed


def process_raw_folder() -> None:
    """
    MAIN ENTRY POINT

    - Reads all files in data/raw
    - Converts them
    - Writes to data/processed
    - Overwrites existing processed files
    """

    ensure_folder(PROCESSED_DIR)

    files = [
        f for f in os.listdir(RAW_DIR)
        if f.endswith(".json")
    ]

    if not files:
        print("No raw files found.")
        return

    for file_name in files:
        raw_path = os.path.join(RAW_DIR, file_name)
        processed_path = os.path.join(PROCESSED_DIR, file_name)

        try:
            raw_data = load_json(raw_path)
            cleaned = _transform_sefaria_raw(raw_data)

            save_json(processed_path, cleaned)

            print(f"Processed: {file_name}")

        except Exception as e:
            print(f"Failed on {file_name}: {e}")