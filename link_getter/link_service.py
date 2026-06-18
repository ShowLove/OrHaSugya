from link_getter.json_reader import load_tractate_data
from link_getter.validator import validate_daf_input
from link_getter.link_builder import (
    build_sefaria_link,
    build_sefaria_api_link
)


def generate_link(
    daf_input: str,
    json_path: str,
    api: bool = False
) -> str:

    tractate_data = load_tractate_data(json_path)

    title = tractate_data["title"]
    start_daf = tractate_data["daf_range"]["start"]
    end_daf = tractate_data["daf_range"]["end"]

    if not validate_daf_input(daf_input, start_daf, end_daf):
        raise ValueError(
            f"Invalid input '{daf_input}'. "
            f"Expected between {start_daf}a and {end_daf}b."
        )

    if api:
        return build_sefaria_api_link(title, daf_input)

    return build_sefaria_link(title, daf_input)