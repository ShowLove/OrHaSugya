import os
import json
from utils.constants import PROCESSED_DIR, BUNDLE_OUTPUT_FILE


def export_processed_to_jsonl(output_file=None):
    """
    Combine all processed files into a single JSONL file.
    """

    output_file = output_file or BUNDLE_OUTPUT_FILE

    files = sorted(os.listdir(PROCESSED_DIR))

    with open(output_file, "w", encoding="utf-8") as out:

        for file in files:
            if not file.endswith("_processed.json"):
                continue

            path = os.path.join(PROCESSED_DIR, file)

            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)

                daf = file.replace("berakhot_", "").replace("_processed.json", "")

                record = {
                    "daf": daf,
                    "ref": data.get("ref"),
                    "heRef": data.get("heRef"),
                    "english": data.get("english", []),
                    "hebrew": data.get("hebrew", [])
                }

                out.write(json.dumps(record, ensure_ascii=False) + "\n")

    return str(output_file)