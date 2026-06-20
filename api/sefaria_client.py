import requests
from utils.constants import (
    SEFARIA_BASE_URL,
    TRACTATE_BERAKHOT,
    API_TIMEOUT
)


def fetch_daf_data(daf: str) -> dict:
    """
    Fetch clean Sefaria daf data.
    """

    ref = f"{TRACTATE_BERAKHOT}.{daf}"
    url = f"{SEFARIA_BASE_URL}/{ref}"

    params = {
        "context": 0,
        "commentary": 0,
        "pad": 0
    }

    try:
        print(f"[API] Fetching: {url}")

        response = requests.get(url, params=params, timeout=API_TIMEOUT)
        data = response.json()

        if "error" in data:
            print(f"[API ERROR] {data['error']}")

        return data

    except Exception as e:
        print(f"[API FAIL] {e}")
        return {
            "ref": None,
            "heRef": None,
            "text": [],
            "he": [],
            "error": str(e)
        }