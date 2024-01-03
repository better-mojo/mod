import os
import shutil
import unittest
from pathlib import Path

from jinja2 import Environment
from jinja2.loaders import FileSystemLoader
from loguru import logger


class PackageCacheHelper:
    """Package Global Cache:
    like:
        - cargo: `.cargo/registry`
        - dart: `.pub-cache`
    """

    MOD_ROOT = os.path.expanduser("~/.mod")  # mod global cache root dir
    MOD_TEMPLATE_DIR = "mod"
    MOD_CONFIG_FILE = "config.toml"

    def __init__(self, mod_root: Path | str = None):
        self.mod_root = Path(mod_root) if mod_root else Path(self.MOD_ROOT)
        self.bin_dir = self.mod_root / "bin"
        self.cache_dir = self.mod_root / "cache/github.com"
        self.f_config = self.mod_root / "config.toml"

        # template loader:
        self.env = Environment(
            loader=FileSystemLoader(
                [
                    self.get_template_dir(),
                    "templates",
                ]
            )
        )

        logger.debug(f"mod root: {self.mod_root}, type: {type(self.mod_root)}")
        logger.debug(f"bin dir: {self.bin_dir}, type: {type(self.bin_dir)}")

        # auto init
        self.init()

    def init(self):
        """
        1. 获取用户目录
        2. 判断用户目录下, 是否存在 `.mod/` 文件夹
        3. 如果不存在, 自动创建
        4. 如果存在, 跳过.
        """
        if self.mod_root.exists():
            return

        self.create_mod_dir()
        self.write_mod_config()

    def get_template_dir(self):
        from mod_cli.utils.path import get_templates_dir

        tpl_root = get_templates_dir()
        return tpl_root / self.MOD_TEMPLATE_DIR

    def create_mod_dir(self):
        os.makedirs(self.mod_root, exist_ok=True)
        os.makedirs(self.bin_dir, exist_ok=True)
        os.makedirs(self.cache_dir, exist_ok=True)

    def write_mod_config(self):
        with open(self.f_config, "w") as f:
            f.write(self.env.get_or_select_template(self.MOD_CONFIG_FILE).render())
        logger.info(f"save config file: {self.f_config}, ")

    def clean(self):
        if os.path.exists(self.mod_root):
            shutil.rmtree(self.mod_root)
            print(f"clean .mod dir: {self.mod_root}")

    def reset(self):
        self.clean()
        self.init()
        print(f"reset .mod dir: {self.mod_root}")


class _TestIt(unittest.TestCase):
    def setUp(self) -> None:
        self.it = PackageCacheHelper()
        pass

    def tearDown(self) -> None:
        pass

    def test_init(self):
        self.it.init()

    def test_clean(self):
        self.it.clean()

    def test_reset(self):
        self.it.reset()
