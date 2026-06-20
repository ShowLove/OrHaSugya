import requests


BASE_URL = "https://www.sefaria.org/api/texts"


def fetch_daf_data(daf: str) -> dict:
    """
    Fetch clean Sefaria daf data.
    """

    ref = f"Berakhot.{daf}"

    url = f"{BASE_URL}/{ref}"

    params = {
        "context": 0,
        "commentary": 0,
        "pad": 0
    }

    try:
        print(f"[API] Fetching: {url}")

        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        # HARD DEBUG SAFETY
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