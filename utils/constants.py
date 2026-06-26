from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]

DATA_DIR = ROOT_DIR / "data"

DEFAULT_TRACTATE = "Berakhot"

# ==================================================
# METADATA
# ==================================================

TRACTATE_METADATA_DIR = DATA_DIR / "tractate_metadata"


def normalize_tractate_name(tractate: str) -> str:
    return tractate.lower().replace(" ", "_")


def display_tractate_name(filename: str) -> str:
    return filename.replace("_", " ").title()


def get_available_tractates() -> list[str]:
    files = sorted(
        TRACTATE_METADATA_DIR.glob("*.json")
    )

    return [
        display_tractate_name(f.stem)
        for f in files
    ]


def get_tractate_metadata_file(
    tractate: str = DEFAULT_TRACTATE
):
    return (
        TRACTATE_METADATA_DIR /
        f"{normalize_tractate_name(tractate)}.json"
    )


# backward compatibility
TRACTATE_BERAKHOT = DEFAULT_TRACTATE

DATA_FILE_BERAKHOT = get_tractate_metadata_file(
    DEFAULT_TRACTATE
)

# ==================================================
# TRACTATE DATA FOLDERS
# ==================================================

TRACTATE_DIR = DATA_DIR / "tractate"


def get_tractate_dir(
    tractate: str = DEFAULT_TRACTATE
):
    return (
        TRACTATE_DIR /
        normalize_tractate_name(tractate)
    )


def get_raw_dir(
    tractate: str = DEFAULT_TRACTATE
):
    return get_tractate_dir(tractate) / "raw"


def get_processed_dir(
    tractate: str = DEFAULT_TRACTATE
):
    return get_tractate_dir(tractate) / "processed"


# backward compatibility
RAW_DIR = get_raw_dir()
PROCESSED_DIR = get_processed_dir()

SEFARIA_BASE_URL = "https://www.sefaria.org/api/texts"

RAW_FILE_PREFIX = "berakhot_"
RAW_FILE_SUFFIX = "_raw.json"

PROCESSED_FILE_PREFIX = "berakhot_"
PROCESSED_FILE_SUFFIX = "_processed.json"


def get_bundle_output_file(
    tractate: str = DEFAULT_TRACTATE
):
    return (
        DATA_DIR /
        f"{normalize_tractate_name(tractate)}_bundle.jsonl"
    )


BUNDLE_OUTPUT_FILE = get_bundle_output_file(
    DEFAULT_TRACTATE
)

CODEBASE_OUTPUT_FILE = DATA_DIR / "code_data.txt"

DEFAULT_DELAY = 0.5
RANGE_DELAY = 0.75
API_TIMEOUT = 10