from loguru import logger
from jinja2 import Environment
from jinja2.loaders import FileSystemLoader


class ProjectLayout:
    pass

    def __init__(self):
        self.f_mod = None
        self.f_readme = None
        self.f_lib = None
        self.f_bin = None

    def load_template(self):
        pass

    def write(self):
        pass


def read_template():
    # 支持相对路径:
    env = Environment(loader=FileSystemLoader("../../templates"))

    tmpl = env.get_template("mod.toml.jinja2")

    logger.info(f"{tmpl.render()}")
    logger.info(f"{env.get_template('layout_bin/src/main.mojo').render()}")


def test():
    read_template()
