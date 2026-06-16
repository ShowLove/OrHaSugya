def build_sefaria_link(
    tractate_name: str,
    daf_input: str
) -> str:
    """
    Build a standard Sefaria reader URL.
    """

    return (
        f"https://www.sefaria.org/"
        f"{tractate_name}.{daf_input.lower()}"
    )


def build_sefaria_api_link(
    tractate_name: str,
    daf_input: str
) -> str:
    """
    Build a Sefaria API URL.
    """

    return (
        f"https://www.sefaria.org/api/texts/"
        f"{tractate_name}.{daf_input.lower()}"
    )