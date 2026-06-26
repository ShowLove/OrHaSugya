import os
import json

from utils.app_state import (
    get_current_tractate
)

from utils.constants import (
    get_available_tractates,
    get_processed_dir,
    get_bundle_output_file,
    TRACTATE_EXPORT_BUNDLES_DIR,
    ALL_TRACTATES_BUNDLE_FILE
)


def export_processed_to_jsonl(
    tractate: str | None = None,
    output_file=None
):
    """
    Combine all processed files for one tractate
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

    TRACTATE_EXPORT_BUNDLES_DIR.mkdir(
        parents=True,
        exist_ok=True
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


def combine_tractate_bundles():
    """
    Combine individual tractate bundle files
    into one all_tractates_bundle.jsonl file.
    Uses the order returned by get_available_tractates(),
    which follows traditional Shas order.
    """

    tractates = get_available_tractates()

    TRACTATE_EXPORT_BUNDLES_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    combined_count = 0
    missing_files = []

    with open(
        ALL_TRACTATES_BUNDLE_FILE,
        "w",
        encoding="utf-8"
    ) as out:

        for tractate in tractates:

            bundle_path = get_bundle_output_file(
                tractate
            )

            if not bundle_path.exists():

                missing_files.append(
                    str(bundle_path)
                )

                continue

            with open(
                bundle_path,
                "r",
                encoding="utf-8"
            ) as f:

                for line in f:

                    if not line.strip():
                        continue

                    out.write(line)

                    combined_count += 1

    print(
        f"\n[OK] Combined bundle created: {ALL_TRACTATES_BUNDLE_FILE}"
    )

    print(
        f"[OK] Combined records: {combined_count}"
    )

    if missing_files:

        print("\n[WARNING] Missing bundle files skipped:")

        for path in missing_files:
            print(f"- {path}")

    return str(ALL_TRACTATES_BUNDLE_FILE)


def export_all_processed_to_jsonl():
    """
    Export processed data for all available tractates.
    Creates one JSONL bundle per tractate.
    Then creates one combined all_tractates_bundle.jsonl file.
    """

    tractates = get_available_tractates()

    if not tractates:
        print("[ERROR] No tractate metadata files found.")
        return []

    exported_files = []

    TRACTATE_EXPORT_BUNDLES_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    print("\n=== Exporting ALL Tractates to JSONL ===\n")

    for i, tractate in enumerate(
        tractates,
        start=1
    ):

        print(
            f"[INFO] ({i}/{len(tractates)}) "
            f"Exporting {tractate}..."
        )

        try:
            path = export_processed_to_jsonl(
                tractate
            )

            exported_files.append(path)

            print(
                f"[OK] Exported: {path}"
            )

        except FileNotFoundError as e:
            print(
                f"[SKIP] {tractate}: {e}"
            )

        except Exception as e:
            print(
                f"[ERROR] Failed {tractate}: {e}"
            )

    combined_path = combine_tractate_bundles()

    exported_files.append(
        combined_path
    )

    print(
        f"\n[OK] Finished exporting {len(exported_files)} bundle file(s)."
    )

    return exported_files