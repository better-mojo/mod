import os
from enum import Enum
from pathlib import Path

import typer
from loguru import logger
from typing_extensions import Annotated

from mod_cli.commands import cmd_add

app = typer.Typer()

# app.add_typer(cmd_new, help="Create a new project")
app.add_typer(cmd_add, help="Add a package")


@app.callback()
def callback():
    """
    Awesome Portal Gun
    """


class NewType(str, Enum):
    bin = "bin"
    lib = "lib"


def is_valid_directory(path):
    import re

    if isinstance(path, Path):
        path = str(path)

    pattern = r"^([\w.-]+)+/?$"
    return re.match(pattern, path) is not None


@app.command(help="Create a new project: [--bin, --lib]")
def new(
    project_name: Annotated[
        Path, typer.Argument(metavar="path", help="The path to create the project at.")
    ],
    is_bin: Annotated[
        bool, typer.Option("--bin", help="Create a binary project")
    ] = False,
    is_lib: Annotated[
        bool, typer.Option("--lib", help="Create a library project")
    ] = False,
    # typ: Annotated[NewType, typer.Option("--type", help="The type of project")] = NewType.bin,
):
    """
    New
    """
    typer.echo("New a mojo project")
    logger.info(f"project name: {project_name}")
    logger.info(f"project type: is_bin: {is_bin}, is_lib: {is_lib}")

    if is_valid_directory(project_name):
        print(f"{project_name} is not a directory")
        # raise typer.Exit(1)
        raise typer.Abort(f"{project_name} is not a directory")

    if os.path.exists(project_name):
        typer.confirm(
            f"❗️{project_name} already exists, do you want to overwrite it?", abort=True
        )
        print(f"\n❗️Overwriting {project_name}")

    try:
        os.makedirs(project_name, exist_ok=True)  # allow to overwrite
    except Exception as e:
        print(e)
        # raise typer.Exit(1)
        raise typer.Abort(e)

    # 创建路径

    # 判断 project_name 是不是路径(相对路径和绝对路径)


@app.command()
def shoot():
    """
    Shoot the portal gun
    """
    typer.echo("Shooting portal gun")


@app.command()
def load():
    """
    Load the portal gun
    """
    typer.echo("Loading portal gun")
