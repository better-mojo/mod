import os
import tomlkit
from loguru import logger

from mod_cli.core.dir import validate_project_dir, find_project_dir


def pretty_print(kv: dict = None):
    kv = kv or {}
    if not isinstance(kv, dict):
        logger.info(kv)
        return

    for k, v in kv.items():
        if isinstance(v, dict):
            logger.info(f"{k}:")
            for kk, vv in v.items():
                logger.info(f"  {kk}: {vv}")
                if isinstance(vv, dict):
                    for kkk, vvv in vv.items():
                        logger.info(f"    {kkk}: {vvv}")
                else:
                    logger.info(f"  {kk}: {vv}")
        else:
            logger.info(f"{k}: {v}")


class ModFile(object):

    def __init__(self, project_dir: str = None):
        self.project_dir = project_dir if validate_project_dir(project_dir) else find_project_dir()
        self.mod_toml = os.path.join(self.project_dir, "mod.toml")
        self.mod_lock = os.path.join(self.project_dir, "mod.lock")
        self.pyproject_toml = os.path.join(self.project_dir, "pyproject.toml")

        self.data = {}
        self.pyproject_data = {}

    def read(self):
        if not os.path.exists(self.mod_toml):
            logger.error(f"mod.toml not found: {self.mod_toml}")
            return

        with open(self.mod_toml, "r") as f:
            self.data = tomlkit.load(f)
            logger.info(f"read mod.toml: {self.data}")

    def read_pyproject(self):
        if not os.path.exists(self.pyproject_toml):
            logger.error(f"pyproject.toml not found: {self.pyproject_toml}")
            return

        with open(self.pyproject_toml, "r") as f:
            self.pyproject_data = tomlkit.load(f)
            pretty_print(self.pyproject_data)

    def add_package(self):
        pass


def test():
    mod = ModFile()
    mod.read_pyproject()
