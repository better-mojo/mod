import os
from pathlib import Path

import typer
from mod_cli.core.new.layout import ProjectLayout
from mod_cli.utils.validate import validate_project_name


class ProjectHelper:
    def __init__(self):
        self.layout = ProjectLayout(search_path="templates/")

    def new(
        self,
        project_name: Path | str,
        project_type: str = "bin",
        **kwargs,
    ):
        p = Path(project_name)
        if not validate_project_name(project_name):
            print(f"{project_name} is not a directory")
            raise typer.Abort(f"{project_name} is not a directory")

        if p.exists():
            typer.confirm(
                f"❗️{project_name} already exists, do you want to overwrite it?",
                abort=True,
            )
            print(f"\n❗️Overwriting {project_name}")

        try:
            os.makedirs(p, exist_ok=True)  # allow to overwrite
        except Exception as e:
            print(e)
            # raise typer.Exit(1)
            raise typer.Abort(e)

        # create files
        self.render_templates(
            path=p.absolute(),
            project_type=project_type,
        )

    def render_templates(self, path: Path, project_type: str = "bin"):
        self.layout.write(
            path=path,
            project_name=path.name,
            project_type=project_type,
        )


def new_project(
    project_name: str, project_type: str = "lib", project_dir: str = None, **kwargs
):
    if project_type == "lib":
        new_lib(project_name=project_name, project_dir=project_dir)
    else:
        new_bin(project_name=project_name, project_dir=project_dir)


def new_lib(project_name: str, project_dir: str = None):
    """mojo new lib
    like cargo new --lib
    """
    if not project_dir:
        project_dir = "./"

    p = Path("./src/lib.rs")
    if p.exists():
        print("lib already exists")
        return

    pass


def new_bin(project_name: str, project_dir: str = None):
    """mojo new binary app
    like cargo new --bin
    """
    pass
