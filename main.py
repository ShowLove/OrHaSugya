from link_getter.link_service import generate_link
from utils.processor import process_raw_folder

DATA_FILE = "data/berakhot.json"


def display_menu() -> None:
    print("=== Half-Daf Link Generator ===\n")
    print("Option:")
    print("1. Generate Sefaria API link")
    print("2. Generate Sefaria link")
    print("3. Process raw Sefaria files\n")


def main() -> None:

    display_menu()

    option = input("Select option: ").strip()

    # NEW OPTION: PROCESS RAW DATA
    if option == "3":
        process_raw_folder()
        return

    if option not in ("1", "2"):
        print("\nInvalid option.")
        return

    daf_input = input(
        "\nInput daf portion (e.g. 2a, 10b): "
    ).strip()

    try:
        link = generate_link(
            daf_input,
            DATA_FILE,
            api=(option == "1")
        )

        print("\nGenerated Link:")
        print(link)

    except ValueError as error:
        print("\nError:")
        print(error)


if __name__ == "__main__":
    main()