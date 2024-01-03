import os
import unittest

from loguru import logger


class PackageHelper:
    def __init__(self):
        self.packages = []
        self.dev_packages = []

        os.getcwd()
        current_dir = os.getcwd()
        logger.debug(f"current_dir: {current_dir}")

    def add(
        self,
        package: str | list,
        is_dev: bool = False,
        version: str = None,
        branch: str = None,  # git remote branch
        path: str = None,  # local package
    ):
        logger.debug(
            f"adding package: {package}, is_dev: {is_dev}, version: {version}, branch: {branch}, path: {path}"
        )

        pass

    def _parse_package_name(self, package: str):
        if not package:
            return

        if "git" in package:
            print(f"{package} is not supported")
            pass
        if "gh" in package:
            print(f"{package} is not supported")
            pass

        pass

    def remove(self):
        pass

    def update(self):
        pass

    def list(self):
        pass


class _TestIt(unittest.TestCase):
    def setUp(self) -> None:
        self.it = PackageHelper()
        pass

    def tearDown(self) -> None:
        pass

    def test_add(self):
        self.it.add(package="github.com/owner/repo")
