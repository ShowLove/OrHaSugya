import json


def load_tractate_metadata(file_path: str) -> dict:
    """
    Load tractate metadata from JSON.
    """

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)