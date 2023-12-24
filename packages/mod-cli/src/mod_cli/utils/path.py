import os
from pathlib import Path


def get_templates_dir(relative_path="../templates") -> Path | str:
    where = Path(os.path.dirname(__file__))

    tpl_dir = Path(where / relative_path)
    return tpl_dir


def test():
    p = get_templates_dir()
    print(f"dir: {p}, is exists: {p.exists()}")
