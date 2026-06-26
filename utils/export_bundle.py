import os
import json

from utils.app_state import (
    get_current_tractate
)

from utils.constants import (
    get_processed_dir,
    get_bundle_output_file
)


def export_processed_to_jsonl(
    tractate: str | None = None,
    output_file=None
):
    """
    Combine all processed files for the selected tractate
    into a single JSONL file.
    """

    if tractate is None:
        tractate = get_current_tractate()

    processed_dir = get_processed_dir(
        tractate
    )

    output_file = (
        output_file or
        get_bundle_output_file(tractate)
    )

    if not processed_dir.exists():
        raise FileNotFoundError(
            f"Processed directory does not exist: {processed_dir}"
        )

    files = sorted(
        os.listdir(processed_dir)
    )

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as out:

        for file in files:

            if not file.endswith("_processed.json"):
                continue

            path = processed_dir / file

            with open(
                path,
                "r",
                encoding="utf-8"
            ) as f:
                data = json.load(f)

            daf = file.replace(
                "_processed.json",
                ""
            )

            record = {
                "tractate": tractate,
                "daf": daf,
                "ref": data.get("ref"),
                "heRef": data.get("heRef"),
                "english": data.get("english", []),
                "hebrew": data.get("hebrew", [])
            }

            out.write(
                json.dumps(
                    record,
                    ensure_ascii=False
                ) + "\n"
            )

    return str(output_file)