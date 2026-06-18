import os
import json


PROCESSED_DIR = "data/processed"


def export_processed_to_jsonl(output_file="data/berakhot_bundle.jsonl"):
    """
    Combine all processed files into a single JSONL file.
    """

    files = sorted(os.listdir(PROCESSED_DIR))

    with open(output_file, "w", encoding="utf-8") as out:

        for file in files:
            if not file.endswith("_processed.json"):
                continue

            path = os.path.join(PROCESSED_DIR, file)

            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)

                # normalize daf from filename
                daf = file.replace("berakhot_", "").replace("_processed.json", "")

                record = {
                    "daf": daf,
                    "ref": data.get("ref"),
                    "heRef": data.get("heRef"),
                    "english": data.get("english", []),
                    "hebrew": data.get("hebrew", [])
                }

                out.write(json.dumps(record, ensure_ascii=False) + "\n")

    return output_file