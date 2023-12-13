from loguru import logger
from jinja2 import Environment
from jinja2.loaders import FileSystemLoader


def read_template():
    # 支持相对路径:
    env = Environment(loader=FileSystemLoader("../../templates"))

    tmpl = env.get_template("mod.toml.jinja2")

    logger.info(f"{tmpl.render()}")


def test():
    read_template()
