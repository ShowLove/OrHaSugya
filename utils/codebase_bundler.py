import os
from pathlib import Path
from datetime import datetime

from utils.constants import CODEBASE_OUTPUT_FILE


# ----------------------------
# CLEAN LLM EXPORT RULES
# ----------------------------

ALLOWED_SUFFIXES = {
    ".py",
    ".md"
}

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

IGNORE_SUFFIXES = {
    ".pyc",
    ".DS_Store",
    ".json",   # IMPORTANT: removes large datasets from context noise
    ".log",
    ".sqlite",
    ".db"
}


# ----------------------------
# FILTER LOGIC
# ----------------------------

def _should_ignore(path: Path) -> bool:
    if any(part in IGNORE_DIRS for part in path.parts):
        return True

    if path.name in IGNORE_FILES:
        return True

    if path.suffix in IGNORE_SUFFIXES:
        return True

    if path.suffix not in ALLOWED_SUFFIXES:
        return True

    return False


# ----------------------------
# TREE BUILDER
# ----------------------------

def _build_tree(root: Path) -> str:
    lines = []

    for dirpath, dirnames, filenames in os.walk(root):
        dirpath = Path(dirpath)

        dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS]

        level = len(dirpath.relative_to(root).parts)
        indent = "    " * level

        lines.append(f"{indent}{dirpath.name}/")

        for f in filenames:
            file_path = dirpath / f
            if not _should_ignore(file_path):
                lines.append(f"{indent}    {f}")

    return "\n".join(lines)


# ----------------------------
# FILE COLLECTOR
# ----------------------------

def _collect_files(root: Path):
    for dirpath, dirnames, filenames in os.walk(root):
        dirpath = Path(dirpath)

        dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS]

        for file in filenames:
            file_path = dirpath / file
            if not _should_ignore(file_path):
                yield file_path


# ----------------------------
# EXPORT
# ----------------------------

def export_codebase_bundle(root_path: str | None = None) -> str:

    root = Path(__file__).resolve().parents[1] if root_path is None else Path(root_path).resolve()

    output_path = CODEBASE_OUTPUT_FILE
    output_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"\n[INFO] Exporting CLEAN codebase from: {root}")

    tree = _build_tree(root)
    files = list(_collect_files(root))

    with open(output_path, "w", encoding="utf-8") as out:

        out.write("=== CLEAN CODEBASE FOR LLM ===\n\n")
        out.write(tree)
        out.write("\n\n")
        out.write("=" * 80 + "\n\n")

        out.write(f"Generated: {datetime.now()}\n")
        out.write(f"Root: {root}\n")
        out.write("Mode: LLM-clean export (no data/json/cache files)\n\n")
        out.write("=" * 80 + "\n\n")

        for file_path in files:
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

    print(f"[OK] Clean codebase exported to: {output_path}")
    return str(output_path)