from link_getter.link_service import generate_link
from utils.processor import process_single_daf, process_range

import json

DATA_FILE = "data/berakhot.json"


def display_menu() -> None:
    print("\n=== Half-Daf Link Generator ===\n")
    print("1. Generate Sefaria API link")
    print("2. Generate Sefaria link")
    print("3. Process single daf")
    print("4. Process range\n")


def main() -> None:

    display_menu()
    option = input("Select option: ").strip()

    if option in ("1", "2", "3"):
        daf = input("Input daf (e.g. 3a): ").strip()

    if option == "1":
        print(generate_link(daf, DATA_FILE, api=True))

    elif option == "2":
        print(generate_link(daf, DATA_FILE, api=False))

    elif option == "3":
        result = process_single_daf("Berakhot", daf)
        print("Processed:", result["ref"])

    elif option == "4":

        start = input("Start daf: ").strip()
        end = input("End daf: ").strip()

        data = json.load(open(DATA_FILE))

        results = process_range(
            "Berakhot",
            start,
            end,
            data["daf_range"]["start"],
            data["daf_range"]["end"]
        )

        print(f"\nProcessed {len(results)} dapim")

    else:
        print("Invalid option")


if __name__ == "__main__":
    main()