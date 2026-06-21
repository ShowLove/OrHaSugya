from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]

DATA_DIR = ROOT_DIR / "data"

DEFAULT_TRACTATE = "Berakhot"

# backward compatibility
TRACTATE_BERAKHOT = DEFAULT_TRACTATE

# metadata
TRACTATE_METADATA_DIR = DATA_DIR / "tractate_metadata"

DATA_FILE_BERAKHOT = (
    TRACTATE_METADATA_DIR / "berakhot.json"
)


def get_tractate_metadata_file(
    tractate: str = DEFAULT_TRACTATE
):
    return (
        TRACTATE_METADATA_DIR /
        f"{tractate.lower().replace(' ', '_')}.json"
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
        tractate.lower().replace(" ", "_")
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

BUNDLE_OUTPUT_FILE = DATA_DIR / "berakhot_bundle.jsonl"
CODEBASE_OUTPUT_FILE = DATA_DIR / "code_data.txt"

DEFAULT_DELAY = 0.5
RANGE_DELAY = 0.75
API_TIMEOUT = 10