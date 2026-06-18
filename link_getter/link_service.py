from .json_reader import load_tractate_metadata
from .validator import is_valid_daf_reference
from .link_builder import (
    build_reader_url,
    build_api_url
)


def generate_sefaria_link(
    daf_reference: str,
    metadata_path: str,
    api: bool = False
) -> str:

    tractate_metadata = load_tractate_metadata(
        metadata_path
    )

    tractate_title = tractate_metadata["title"]

    first_daf = (
        tractate_metadata["daf_range"]["start"]
    )

    last_daf = (
        tractate_metadata["daf_range"]["end"]
    )

    if not is_valid_daf_reference(
        daf_reference,
        first_daf,
        last_daf
    ):
        raise ValueError(
            f"Invalid input '{daf_reference}'. "
            f"Expected a daf between "
            f"{first_daf}a and {last_daf}b."
        )

    if api:
        return build_api_url(
            tractate_title,
            daf_reference
        )

    return build_reader_url(
        tractate_title,
        daf_reference
    )