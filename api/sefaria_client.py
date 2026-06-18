import requests


BASE_URL = "https://www.sefaria.org/api/texts/"


def fetch_daf_data(ref: str) -> dict:
    url = f"{BASE_URL}{ref}"

    response = requests.get(url)

    if response.status_code != 200:
        raise ValueError(f"Sefaria error: {response.status_code}")

    return response.json()