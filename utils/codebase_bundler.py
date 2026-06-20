import os
from pathlib import Path
from datetime import datetime


IGNORE_DIRS = {
    "__pycache__",
    ".git",
    ".idea",
    ".vscode",
    "venv",
    ".venv",
    "node_modules",
    "data"
}

IGNORE_FILES = {
    "code_data.txt"
}


def _should_ignore(path: Path) -> bool:
    parts = set(path.parts)
    if parts & IGNORE_DIRS:
        return True
    if path.name in IGNORE_FILES:
        return True
    if path.suffix in {".pyc", ".DS_Store"}:
        return True
    return False


def _build_tree(root: Path) -> str:
    lines = []

    for dirpath, dirnames, filenames in os.walk(root):
        dirpath = Path(dirpath)

        # filter ignored dirs in-place
        dirnames[:] = [
            d for d in dirnames
            if d not in IGNORE_DIRS
        ]

        level = len(dirpath.relative_to(root).parts)
        indent = "    " * level

        lines.append(f"{indent}{dirpath.name}/")

        for f in filenames:
            file_path = dirpath / f
            if not _should_ignore(file_path):
                lines.append(f"{indent}    {f}")

    return "\n".join(lines)


def _collect_files(root: Path):
    for dirpath, dirnames, filenames in os.walk(root):
        dirpath = Path(dirpath)

        dirnames[:] = [
            d for d in dirnames
            if d not in IGNORE_DIRS
        ]

        for file in filenames:
            file_path = dirpath / file
            if not _should_ignore(file_path):
                yield file_path


def export_codebase_bundle(root_path: str | None = None) -> str:
    """
    Creates a single bundled file containing:
    - directory tree
    - all project source files

    Output: data/code_data.txt
    """

    if root_path is None:
        root = Path(__file__).resolve().parents[1]
    else:
        root = Path(root_path).resolve()

    output_path = root / "data" / "code_data.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"\n[INFO] Bundling codebase from: {root}")

    tree = _build_tree(root)

    all_files = list(_collect_files(root))

    with open(output_path, "w", encoding="utf-8") as out:

        out.write("=== CODEBASE STRUCTURE ===\n\n")
        out.write(tree)
        out.write("\n\n")
        out.write("=" * 80 + "\n\n")

        out.write(f"Generated: {datetime.now()}\n")
        out.write(f"Root: {root}\n\n")
        out.write("=" * 80 + "\n\n")

        for file_path in all_files:
            try:
                relative = file_path.relative_to(root)

                out.write("\n\n")
                out.write("=" * 80 + "\n")
                out.write(f"FILE: {relative}\n")
                out.write("=" * 80 + "\n\n")

                content = file_path.read_text(encoding="utf-8", errors="ignore")
                out.write(content)

            except Exception as e:
                out.write(f"\n[ERROR READING FILE: {file_path}] {e}\n")

    print(f"[OK] Codebase exported to: {output_path}")

    return str(output_path)