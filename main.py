from test.test_menu import run_test_menu

from utils.export_bundle import (
    export_processed_to_jsonl
)

from utils.codebase_bundler import (
    export_codebase_bundle
)


def display_menu():
    print("\n=== Half-Daf System ===\n")

    print("1. Development Tools")
    print("2. Export processed tractate as JSONL")
    print("3. Export FULL codebase (for ChatGPT)")


def main():

    while True:

        display_menu()

        option = input(
            "\nSelect option: "
        ).strip()

        if option == "1":

            run_test_menu()

        elif option == "2":

            print(
                "\n[INFO] Exporting processed tractate as JSONL..."
            )

            path = export_processed_to_jsonl()

            print(
                f"[OK] Export complete: {path}"
            )

        elif option == "3":

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