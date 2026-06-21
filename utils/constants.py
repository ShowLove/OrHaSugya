from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]

DATA_DIR = ROOT_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"

DEFAULT_TRACTATE = "Berakhot"

# BACKWARD COMPATIBILITY
TRACTATE_BERAKHOT = DEFAULT_TRACTATE

# NEW LOCATION
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