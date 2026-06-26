# =========================
# FILE: utils/app_state.py
# =========================

from utils.constants import DEFAULT_TRACTATE


_current_tractate = DEFAULT_TRACTATE


def get_current_tractate() -> str:
    return _current_tractate


def set_current_tractate(tractate: str) -> None:
    global _current_tractate
    _current_tractate = tractate


def reset_current_tractate() -> None:
    global _current_tractate
    _current_tractate = DEFAULT_TRACTATE