import typer
from loguru import logger
import os


def init_mod_config():
    # app_dir = typer.get_app_dir(".")
    user_root = os.path.expanduser("~")

    # mod config:
    cfg_dir = os.path.join(user_root, ".config", "mod-cli")
    cfg_file = os.path.join(cfg_dir, "mod.toml")

    if not os.path.exists(cfg_dir):
        logger.info(f"create app_dir: {cfg_dir}")
        os.makedirs(cfg_dir)

    # 检查 ~/.config/mod-cli/mod.toml 是否存在? 如果不存在, 创建一个
    if not os.path.exists(cfg_file):
        logger.info(f"create mod global config file: {cfg_file}")
        with open(cfg_file, "w") as f:
            f.write("#TODO: global config file")


def clean_mod_config():
    # app_dir = typer.get_app_dir(".")
    user_root = os.path.expanduser("~")

    # mod config:
    cfg_dir = os.path.join(user_root, ".config", "mod-cli")
    cfg_file = os.path.join(cfg_dir, "mod.toml")

    if os.path.exists(cfg_file):
        logger.info(f"remove mod global config file: {cfg_file}")
        os.remove(cfg_file)


def reset_mod_config():
    clean_mod_config()
    init_mod_config()


def test():
    init_mod_config()
    clean_mod_config()
