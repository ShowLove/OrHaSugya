import re


def validate_daf_input(
    daf_input: str,
    start_daf: int,
    end_daf: int
) -> bool:
    """
    Validate input such as:
    2a
    10b
    64a
    """

    match = re.fullmatch(
        r"(\d+)([ab])",
        daf_input.lower()
    )

    if not match:
        return False

    daf_number = int(match.group(1))

    return start_daf <= daf_number <= end_daf