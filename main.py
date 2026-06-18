from link_getter.link_service import generate_sefaria_link

DATA_FILE = "data/berakhot.json"


def display_main_menu() -> None:
    print("=== Half-Daf Link Generator ===\n")
    print("Option:")
    print("1. Generate Sefaria API link")
    print("2. Generate Sefaria link\n")


def main() -> None:

    display_main_menu()

    option = input(
        "Select option: "
    ).strip()

    if option not in ("1", "2"):
        print("\nInvalid option.")
        return

    daf_reference = input(
        "\nInput daf portion "
        "(e.g. 2a, 10b): "
    ).strip()

    try:

        link = generate_sefaria_link(
            daf_reference,
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