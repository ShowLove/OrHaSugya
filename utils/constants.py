# utils/constants.py

from pathlib import Path

# ----------------------------
# PROJECT ROOT / DATA
# ----------------------------

ROOT_DIR = Path(__file__).resolve().parents[1]

DATA_DIR = ROOT_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"

DATA_FILE_BERAKHOT = DATA_DIR / "berakhot.json"


# ----------------------------
# TRACTATE CONFIG
# ----------------------------

TRACTATE_BERAKHOT = "Berakhot"


# ----------------------------
# SEFARIA API
# ----------------------------

SEFARIA_BASE_URL = "https://www.sefaria.org/api/texts"


# ----------------------------
# FILE NAMING
# ----------------------------

RAW_FILE_PREFIX = "berakhot_"
RAW_FILE_SUFFIX = "_raw.json"

PROCESSED_FILE_PREFIX = "berakhot_"
PROCESSED_FILE_SUFFIX = "_processed.json"

BUNDLE_OUTPUT_FILE = DATA_DIR / "berakhot_bundle.jsonl"

CODEBASE_OUTPUT_FILE = DATA_DIR / "code_data.txt"


# ----------------------------
# PROCESSING SPEED / LIMITS
# ----------------------------

DEFAULT_DELAY = 0.5
RANGE_DELAY = 0.75
API_TIMEOUT = 10


# ----------------------------
# CODEBASE BUNDLER IGNORES
# ----------------------------

IGNORE_DIRS = {
    "__pycache__",
    ".git",
    ".idea",
    ".vscode",
    "venv",
    ".venv",
    "node_modules",
    "data"
}

IGNORE_FILES = {
    "code_data.txt"
}

IGNORE_SUFFIXES = {
    ".pyc",
    ".DS_Store"
}