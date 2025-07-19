import os
import sys


def get_path(path: str) -> str:
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return os.path.join(getattr(sys, "_MEIPASS"), os.path.normpath(path))
    else:
        return os.path.normpath(path)
