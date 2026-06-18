def build_sefaria_link(tractate_name: str, daf_input: str) -> str:
    return (
        f"https://www.sefaria.org/"
        f"{tractate_name}.{daf_input.lower()}"
    )


def build_sefaria_api_link(tractate_name: str, daf_input: str) -> str:
    return (
        f"https://www.sefaria.org/api/texts/"
        f"{tractate_name}.{daf_input.lower()}"
    )