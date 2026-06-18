import re


def is_valid_daf_reference(
    daf_reference: str,
    first_daf: int,
    last_daf: int
) -> bool:
    """
    Validate input such as:
    2a
    10b
    64a
    """

    daf_reference = (
        daf_reference
        .strip()
        .lower()
    )

    match = re.fullmatch(
        r"(\d+)([ab])",
        daf_reference
    )

    if not match:
        return False

    daf_number = int(match.group(1))

    return (
        first_daf
        <= daf_number
        <= last_daf
    )