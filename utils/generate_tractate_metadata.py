import json
import os


TRACTATES = [
    ("Berakhot", "ברכות", 64),
    ("Shabbat", "שבת", 157),
    ("Eruvin", "עירובין", 105),
    ("Pesachim", "פסחים", 121),
    ("Shekalim", "שקלים", 22),
    ("Yoma", "יומא", 88),
    ("Sukkah", "סוכה", 56),
    ("Beitzah", "ביצה", 40),
    ("Rosh_Hashanah", "ראש השנה", 35),
    ("Taanit", "תענית", 31),
    ("Megillah", "מגילה", 32),
    ("Moed_Katan", "מועד קטן", 29),
    ("Chagigah", "חגיגה", 27),
    ("Yevamot", "יבמות", 122),
    ("Ketubot", "כתובות", 112),
    ("Nedarim", "נדרים", 91),
    ("Nazir", "נזיר", 66),
    ("Sotah", "סוטה", 49),
    ("Gittin", "גיטין", 90),
    ("Kiddushin", "קידושין", 82),
    ("Bava_Kamma", "בבא קמא", 119),
    ("Bava_Metzia", "בבא מציעא", 119),
    ("Bava_Batra", "בבא בתרא", 176),
    ("Sanhedrin", "סנהדרין", 113),
    ("Makkot", "מכות", 24),
    ("Shevuot", "שבועות", 49),
    ("Avodah_Zarah", "עבודה זרה", 76),
    ("Horayot", "הוריות", 14),
    ("Zevachim", "זבחים", 120),
    ("Menachot", "מנחות", 110),
    ("Chullin", "חולין", 142),
    ("Bekhorot", "בכורות", 61),
    ("Arakhin", "ערכין", 34),
    ("Temurah", "תמורה", 34),
    ("Keritot", "כריתות", 28),
    ("Meilah", "מעילה", 22),
    ("Kinnim", "קינים", 3),
    ("Tamid", "תמיד", 10),
    ("Middot", "מידות", 4),
    ("Niddah", "נדה", 73),
]

METADATA_DIR = "data/tractate_metadata"


def ensure_metadata_dir():
    os.makedirs(METADATA_DIR, exist_ok=True)


def generate_metadata_file(title, he_title, end_daf):
    ensure_metadata_dir()

    data = {
        "title": title.replace("_", " "),
        "heTitle": he_title,
        "daf_range": {
            "start": 2,
            "end": end_daf
        }
    }

    filename = f"{title.lower()}.json"
    path = os.path.join(METADATA_DIR, filename)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=2
        )

    return path


def generate_all_metadata():
    generated = []

    print("\n[INFO] Generating metadata for ALL tractates...\n")

    for title, he_title, end_daf in TRACTATES:

        path = generate_metadata_file(
            title,
            he_title,
            end_daf
        )

        generated.append(path)

        print(f"[OK] {title}")

    print(
        f"\n[SUCCESS] Generated {len(generated)} metadata files."
    )

    return generated


def generate_single_metadata(index):
    title, he_title, end_daf = TRACTATES[index]

    path = generate_metadata_file(
        title,
        he_title,
        end_daf
    )

    print(f"\n[SUCCESS] Generated:")
    print(path)

    return path


def metadata_menu():

    print("\n=== Generate Tractate Metadata ===\n")

    print("0. ALL TRACTATES")

    for i, (title, _, _) in enumerate(
        TRACTATES,
        start=1
    ):
        print(
            f"{i}. {title.replace('_', ' ')}"
        )

    selection = input(
        "\nSelect option: "
    ).strip()

    try:
        selection = int(selection)

    except ValueError:
        print("[ERROR] Invalid selection")
        return

    if selection == 0:
        return generate_all_metadata()

    if selection < 1 or selection > len(TRACTATES):
        print("[ERROR] Invalid selection")
        return

    return generate_single_metadata(
        selection - 1
    )