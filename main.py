from link_getter.link_service import generate_link
from utils.berakhot_processor import process_single_daf
from utils.range_processor import (
    process_daf_range,
    process_full_book
)

DATA_FILE = "data/berakhot.json"


def display_menu():
    print("\n=== Half-Daf System ===\n")
    print("1. Generate Sefaria API link")
    print("2. Generate Sefaria link")
    print("3. Process single daf")
    print("4. Process daf range (Berakhot)")
    print("5. Get full Berakhot data")


def main():

    display_menu()
    option = input("\nSelect option: ").strip()

    if option in ("1", "2"):
        daf_input = input("Enter daf (e.g. 3a): ").strip()

        link = generate_link(
            daf_input,
            DATA_FILE,
            api=(option == "1")
        )

        print("\nGenerated:")
        print(link)

    elif option == "3":
        daf = input("Enter daf: ").strip()
        process_single_daf(daf)

    elif option == "4":
        start = input("Start daf (e.g. 4a): ").strip()
        end = input("End daf (e.g. 10a): ").strip()
        process_daf_range(start, end)

    elif option == "5":
        process_full_book()

    else:
        print("Invalid option")


if __name__ == "__main__":
    main()