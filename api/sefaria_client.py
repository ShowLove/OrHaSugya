import requests


def fetch_daf_data(tractate_name: str, daf_input: str) -> dict:

    url = (
        "https://www.sefaria.org/api/texts/"
        f"{tractate_name}.{daf_input.lower()}"
    )

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    return response.json()