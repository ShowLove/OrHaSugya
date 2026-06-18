from link_getter.link_service import (
    generate_link,
    fetch_and_store_daf
)

DATA_FILE = "data/berakhot.json"


def display_menu() -> None:
    print("=== Half-Daf Link Generator ===\n")
    print("1. Generate Sefaria API link")
    print("2. Generate Sefaria link")
    print("3. Fetch daf data from Sefaria API\n")


def main() -> None:

    display_menu()

    option = input("Select option: ").strip()

    if option not in ("1", "2", "3"):
        print("Invalid option")
        return

    daf_input = input("Input daf (e.g. 3a): ").strip()

    try:

        if option == "3":
            path = fetch_and_store_daf(daf_input, DATA_FILE)
            print("\nSaved to:")
            print(path)
            return

        link = generate_link(
            daf_input,
            DATA_FILE,
            api=(option == "1")
        )

        print("\nResult:")
        print(link)

    except Exception as e:
        print("\nError:")
        print(e)


if __name__ == "__main__":
    main()