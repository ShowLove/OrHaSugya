import os
import json


def ensure_folder(path: str) -> None:
    """
    Create folder if it doesn't exist.
    """
    os.makedirs(path, exist_ok=True)


def load_json(file_path: str) -> dict:
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(file_path: str, data: dict) -> None:
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)