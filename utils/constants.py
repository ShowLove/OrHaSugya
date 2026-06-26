from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]

DATA_DIR = ROOT_DIR / "data"

DEFAULT_TRACTATE = "Berakhot"

# ==================================================
# METADATA
# ==================================================

TRACTATE_METADATA_DIR = (
    DATA_DIR / "tractate_metadata"
)


def normalize_tractate_name(
    tractate: str
) -> str:
    return (
        tractate
        .lower()
        .replace(" ", "_")
    )


def display_tractate_name(
    filename: str
) -> str:
    return (
        filename
        .replace("_", " ")
        .title()
    )


# ==================================================
# TRADITIONAL SHAS ORDER
# ==================================================

TRACTATE_ORDER = [

    "Berakhot",
    "Shabbat",
    "Eruvin",
    "Pesachim",
    "Shekalim",
    "Yoma",
    "Sukkah",
    "Beitzah",
    "Rosh Hashanah",
    "Taanit",
    "Megillah",
    "Moed Katan",
    "Chagigah",

    "Yevamot",
    "Ketubot",
    "Nedarim",
    "Nazir",
    "Sotah",
    "Gittin",
    "Kiddushin",

    "Bava Kamma",
    "Bava Metzia",
    "Bava Batra",
    "Sanhedrin",
    "Makkot",
    "Shevuot",
    "Avodah Zarah",
    "Horayot",

    "Zevachim",
    "Menachot",
    "Chullin",
    "Bekhorot",
    "Arakhin",
    "Temurah",
    "Keritot",
    "Meilah",
    "Kinnim",
    "Tamid",
    "Middot",

    "Niddah"
]


def get_available_tractates():
    """
    Returns tractates in the traditional
    order of Shas. If metadata exists for
    additional tractates in the future,
    they are appended alphabetically.
    """

    metadata = {
        display_tractate_name(
            f.stem
        )
        for f in TRACTATE_METADATA_DIR.glob(
            "*.json"
        )
    }

    ordered = [
        tractate
        for tractate in TRACTATE_ORDER
        if tractate in metadata
    ]

    remaining = sorted(
        metadata - set(ordered)
    )

    return ordered + remaining


def get_tractate_metadata_file(
    tractate: str = DEFAULT_TRACTATE
):
    return (
        TRACTATE_METADATA_DIR /
        f"{normalize_tractate_name(tractate)}.json"
    )


# ==================================================
# TRACTATE DATA
# ==================================================

TRACTATE_DIR = (
    DATA_DIR / "tractate"
)


def get_tractate_dir(
    tractate: str = DEFAULT_TRACTATE
):
    return (
        TRACTATE_DIR /
        normalize_tractate_name(
            tractate
        )
    )


def get_raw_dir(
    tractate: str = DEFAULT_TRACTATE
):
    return (
        get_tractate_dir(
            tractate
        )
        / "raw"
    )


def get_processed_dir(
    tractate: str = DEFAULT_TRACTATE
):
    return (
        get_tractate_dir(
            tractate
        )
        / "processed"
    )


# --------------------------------------------------
# Backward compatibility
# --------------------------------------------------

TRACTATE_BERAKHOT = DEFAULT_TRACTATE

DATA_FILE_BERAKHOT = (
    get_tractate_metadata_file(
        DEFAULT_TRACTATE
    )
)

RAW_DIR = get_raw_dir()
PROCESSED_DIR = get_processed_dir()


# ==================================================
# EXPORT BUNDLES
# ==================================================

TRACTATE_EXPORT_BUNDLES_DIR = (
    DATA_DIR /
    "tractate_export_bundles"
)


def get_bundle_output_file(
    tractate: str = DEFAULT_TRACTATE
):
    return (
        TRACTATE_EXPORT_BUNDLES_DIR /
        f"{normalize_tractate_name(tractate)}_bundle.jsonl"
    )


ALL_TRACTATES_BUNDLE_FILE = (
    TRACTATE_EXPORT_BUNDLES_DIR /
    "all_tractates_bundle.jsonl"
)


# --------------------------------------------------
# Backward compatibility
# --------------------------------------------------

BUNDLE_OUTPUT_FILE = (
    get_bundle_output_file(
        DEFAULT_TRACTATE
    )
)


# ==================================================
# CODE EXPORT
# ==================================================

CODEBASE_OUTPUT_FILE = (
    DATA_DIR /
    "code_data.txt"
)


# ==================================================
# API
# ==================================================

SEFARIA_BASE_URL = (
    "https://www.sefaria.org/api/texts"
)

API_TIMEOUT = 10

DEFAULT_DELAY = 0.5

RANGE_DELAY = 0.75


# ==================================================
# FILE SUFFIXES
# ==================================================

RAW_FILE_PREFIX = "berakhot_"

RAW_FILE_SUFFIX = "_raw.json"

PROCESSED_FILE_PREFIX = "berakhot_"

PROCESSED_FILE_SUFFIX = "_processed.json"