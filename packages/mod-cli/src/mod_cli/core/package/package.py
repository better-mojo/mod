import os
import subprocess
import unittest
from pathlib import Path

import tomlkit
from loguru import logger


class PackageHelper:
    GLOBAL_CACHE_DIR = Path.home().joinpath(".mod", "cache", "github.com")
    MOD_FILE = "mod.toml"
    DEV_DEPENDENCIES = "dev-dependencies"
    DEPENDENCIES = "dependencies"

    def __init__(self):
        self.mod_toml = self.parse_mod_toml()
        self.packages = self.mod_toml.get(self.DEPENDENCIES, {})
        self.dev_packages = self.mod_toml.get(self.DEV_DEPENDENCIES, {})

        logger.debug(f"mod.toml: {self.mod_toml}")
        logger.debug(f"packages: {self.packages}")
        logger.debug(f"dev_packages: {self.dev_packages}")

        if not self.GLOBAL_CACHE_DIR.exists():
            self.GLOBAL_CACHE_DIR.mkdir(parents=True)

    def parse_mod_toml(self):
        f_mod = Path(os.getcwd()) / self.MOD_FILE

        if not f_mod.exists():
            logger.error(f"mod.toml not found: {f_mod}")
            print("mod.toml not found in current directory")
            return None

        with open(f_mod, "r") as f:
            return tomlkit.load(f)

    def add_many(
        self,
        packages: list[str],
        package_name: str = None,
        is_dev: bool = False,
        version: str = None,
        branch: str = None,
    ):
        if not packages:
            return

        if len(packages) == 1:
            self.add_one(
                packages[0],
                package_name,
                is_dev,
                version,
                branch,
            )
            return

        for pkg in packages:
            self.add_one(pkg)

    def add_to_mod_toml(
        self,
        package_name: str,
        url: str = None,  # git pkg
        is_dev: bool = False,
        version: str = None,
        branch: str = None,
        path: str = None,  # local pkg
    ):
        where = self.packages if is_dev else self.packages

        if package_name in where.keys():
            if url == where["git"]:
                return
            else:
                logger.error("duplicate package name in mod.toml")

        item = {
            "git": url,
        }
        if is_dev:
            item["dev"] = True
        if version:
            item["version"] = version
        if branch:
            item["branch"] = branch
        if path:
            item["path"] = path

        where[package_name] = item
        return item

    def save_mod_toml(self):
        f_mod = Path(os.getcwd()) / self.MOD_FILE
        with open(f_mod, "w") as f:
            tomlkit.dump(self.mod_toml, f)

    def add_one(
        self,
        package_path: str | list,
        package_name: str = None,
        is_dev: bool = False,
        version: str = None,
        branch: str = None,  # git remote branch
    ):
        """
        todo:
            1. validate
            2. add package to mod.toml
            3. git clone pkg to ~/.mod/cache/
        """
        owner, repo, local_pkg_path = None, None, None

        if "github.com" in package_path.lower():
            owner, repo = package_path.split("github.com/")[1].split("/")
        elif "gh" in package_path.lower():
            owner, repo = package_path.lstrip("gh://").split("/")
        else:  # local package
            local_pkg_path = package_path

        logger.debug(f"owner: {owner}, repo: {repo}, local_pkg_path: {local_pkg_path}")
        if not owner and not repo and not local_pkg_path:
            logger.error(f"Invalid package: {package_path}")
            return
        url = f"https://github.com/{owner}/{repo}"
        cached_path = self.GLOBAL_CACHE_DIR.joinpath(owner, repo)

        # save to mod.toml
        self.add_to_mod_toml(
            package_name if package_name else repo,
            url=url if not local_pkg_path else None,
            is_dev=is_dev,
            version=version,
            branch=branch,
            path=local_pkg_path,
        )

        # check if cached
        self.git_clone(url, cached_path)

        # save to mod.toml
        self.save_mod_toml()

    def git_clone(self, url: str, cached_path: Path):
        # check if cached
        if cached_path.exists():
            logger.info(f"{cached_path} already exists")
            return

        # not exists
        cached_path.mkdir(parents=True, exist_ok=True)

        try:
            # git clone to ~/.mod/cache/github.com
            ret = subprocess.run(
                ["git", "clone", url, cached_path],
                check=True,
                capture_output=True,
            )
            if ret.stdout:
                print(ret.stdout)
            if ret.stderr:
                print(ret.stderr)
        except subprocess.CalledProcessError as e:
            logger.error(e.stderr)
        except Exception as e:
            logger.error(e)

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
