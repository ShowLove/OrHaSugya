def build_sefaria_link(
    tractate_name: str,
    daf_input: str
) -> str:
    """
    Build a Sefaria URL.
    """

    return (
        f"https://www.sefaria.org/"
        f"{tractate_name}.{daf_input.lower()}"
    )