def build_reader_url(
    tractate_title: str,
    daf_reference: str
) -> str:
    """
    Build a standard Sefaria reader URL.
    """

    return (
        f"https://www.sefaria.org/"
        f"{tractate_title}.{daf_reference.lower()}"
    )


def build_api_url(
    tractate_title: str,
    daf_reference: str
) -> str:
    """
    Build a Sefaria API URL.
    """

    return (
        f"https://www.sefaria.org/api/texts/"
        f"{tractate_title}.{daf_reference.lower()}"
    )