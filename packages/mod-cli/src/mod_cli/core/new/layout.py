from jinja2 import Environment
from jinja2.loaders import FileSystemLoader
from loguru import logger


class ProjectLayout:
    SOURCE_DIR = "src"
    MOD_FILE = "mod.toml"
    MOD_LOCK_FILE = "mod.lock"
    LIB_FILE = "lib.mojo"
    BIN_FILE = "main.mojo"
    INIT_FILE = "__init__.mojo"
    README_FILE = "README.md"
    TASK_FILE = "Taskfile.yml"
    IGNORE_FILE = ".gitignore"

    def __init__(self, search_path: str = "../../templates"):
        self.env = Environment(loader=FileSystemLoader("../../templates"))

    def render_mod_file(
        self,
        project_name,
        author_name="your_name",
        author_email="you@email.com",
    ):
        f = self.env.get_template(self.MOD_FILE).render(
            project_name=project_name,
            author_name=author_name,
            author_email=author_email,
        )
        logger.info(f"mod.toml: {f}")

    def render_bin_file(self):
        f = self.env.get_template(self.BIN_FILE).render()
        logger.info(f"bin.mojo: {f}")

    def render_lib_file(self):
        f = self.env.get_template(self.LIB_FILE).render()
        logger.info(f"lib.mojo: {f}")

    def render_readme_file(self, project_name, project_type="bin"):
        f = self.env.get_template(self.README_FILE).render(
            project_name=project_name,
            project_type="binary application" if project_type == "bin" else "library",
        )
        logger.info(f"README.md: {f}")

    def render_init_file(self):
        f = self.env.get_template(self.INIT_FILE).render()
        logger.info(f"__init__.mojo: {f}")

    def render_task_file(self):
        f = self.env.get_or_select_template(self.TASK_FILE).render()
        logger.info(f"Taskfile.yml: {f}")

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
    # read_template()

    pl = ProjectLayout()
    pl.render_mod_file("demo")
    pl.render_lib_file()
    pl.render_bin_file()
    pl.render_readme_file("demo-bin", "bin")
    pl.render_readme_file("demo-lib", "lib")
    pl.render_init_file()
    pl.render_task_file()
