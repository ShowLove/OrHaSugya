import json


def load_tractate_data(file_path: str) -> dict:
    """
    Load tractate metadata from JSON.
    """

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)