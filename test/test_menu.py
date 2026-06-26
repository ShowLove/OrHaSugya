from link_getter.link_service import (
    generate_link
)

from utils.berakhot_processor import (
    process_single_daf
)

from utils.range_processor import (
    process_daf_range,
    process_full_book
)

from utils.app_state import (
    get_current_tractate,
    set_current_tractate
)

from utils.constants import (
    get_available_tractates,
    get_tractate_metadata_file
)


def display_test_menu():

    current_tractate = get_current_tractate()

    print("\n=== Development Tools ===\n")
    print(f"Current tractate: {current_tractate}\n")

    print("1. Change tractate")
    print("2. Generate Sefaria API link")
    print("3. Generate Sefaria link")
    print("4. Process single daf")
    print("5. Process daf range")
    print("6. Get full tractate data")
    print("0. Back")


def select_tractate():

    tractates = get_available_tractates()

    if not tractates:
        print("[ERROR] No tractate metadata files found.")
        return

    print("\n=== Available Tractates ===\n")

    for i, tractate in enumerate(
        tractates,
        start=1
    ):
        print(f"{i}. {tractate}")

    selection = input(
        "\nSelect tractate: "
    ).strip()

    try:
        selection = int(selection)

    except ValueError:
        print("Invalid selection")
        return

    if selection < 1 or selection > len(tractates):
        print("Invalid selection")
        return

    selected_tractate = tractates[
        selection - 1
    ]

    set_current_tractate(
        selected_tractate
    )

    print(
        f"\n[OK] Current tractate: {selected_tractate}"
    )


def run_test_menu():

    while True:

        display_test_menu()

        option = input(
            "\nSelect option: "
        ).strip()

        current_tractate = get_current_tractate()

        if option == "1":

            select_tractate()

        elif option in ("2", "3"):

            daf_input = input(
                "Enter daf (e.g. 3a): "
            ).strip()

            link = generate_link(
                daf_input,
                str(
                    get_tractate_metadata_file(
                        current_tractate
                    )
                ),
                api=(option == "2"),
                tractate=current_tractate
            )

            print("\nGenerated:")
            print(link)

        elif option == "4":

            daf = input(
                "Enter daf: "
            ).strip()

            process_single_daf(
                daf,
                current_tractate
            )

        elif option == "5":

            start = input(
                "Start daf (e.g. 4a): "
            ).strip()

            end = input(
                "End daf (e.g. 10a): "
            ).strip()

            process_daf_range(
                start,
                end,
                current_tractate
            )

        elif option == "6":

            process_full_book(
                current_tractate
            )

        elif option == "0":

            return

        else:

            print("Invalid option")

        input(
            "\nPress Enter to continue..."
        )