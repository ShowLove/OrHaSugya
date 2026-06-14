from link_getter.link_service import generate_link


DATA_FILE = "data/berakhot.json"


def display_menu() -> None:
    print("=== Half-Daf Link Generator ===\n")
    print("Option:")
    print("1. Generate Sefaria link\n")


def main() -> None:

    display_menu()

    option = input(
        "Select option: "
    ).strip()

    if option != "1":
        print("\nInvalid option.")
        return

    daf_input = input(
        "\nInput daf portion "
        "(e.g. 2a, 10b): "
    ).strip()

    try:

        link = generate_link(
            daf_input,
            DATA_FILE
        )

        print("\nGenerated Link:")
        print(link)

    except ValueError as error:

        print("\nError:")
        print(error)


if __name__ == "__main__":
    main()