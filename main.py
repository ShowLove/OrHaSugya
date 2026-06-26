from test.test_menu import run_test_menu

from utils.app_state import (
    get_current_tractate
)

from utils.export_bundle import (
    export_processed_to_jsonl,
    export_all_processed_to_jsonl
)

from utils.codebase_bundler import (
    export_codebase_bundle
)


def display_menu():

    current_tractate = get_current_tractate()

    print("\n=== Half-Daf System ===\n")
    print(f"Current tractate: {current_tractate}\n")

    print("1. Development Tools")
    print("2. Export current tractate processed data as JSONL")
    print("3. Export ALL tractates processed data as JSONL")
    print("4. Export FULL codebase (for ChatGPT)")


def main():

    while True:

        display_menu()

        option = input(
            "\nSelect option: "
        ).strip()

        if option == "1":

            run_test_menu()

        elif option == "2":

            current_tractate = get_current_tractate()

            print(
                f"\n[INFO] Exporting processed {current_tractate} data as JSONL..."
            )

            path = export_processed_to_jsonl()

            print(
                f"[OK] Export complete: {path}"
            )

        elif option == "3":

            confirm = input(
                "\nThis will export processed data for ALL tractates. Continue? (y/n): "
            ).strip().lower()

            if confirm == "y":

                paths = export_all_processed_to_jsonl()

                print(
                    f"\n[OK] Exported {len(paths)} tractate bundle(s)."
                )

            else:

                print(
                    "[CANCELLED] Did not export all tractates."
                )

        elif option == "4":

            print(
                "\n[INFO] Exporting CLEAN codebase bundle (LLM-ready)..."
            )

            path = export_codebase_bundle()

            print(
                f"[OK] Clean codebase exported: {path}"
            )

        else:

            print("Invalid option")

        print()


if __name__ == "__main__":
    main()