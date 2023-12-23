import os
from enum import Enum
from pathlib import Path
from typing import Optional

import typer
from loguru import logger
from typing_extensions import Annotated

from mod_cli.commands.add import cmd_add
from mod_cli.commands.hack import cmd_hack

__version__ = "0.1.1"

app = typer.Typer(
    help="Awesome Mojo Package Manager",
    no_args_is_help=True,
)

# app.add_typer(cmd_new, help="Create a new project")
app.add_typer(cmd_add, name="add")
app.add_typer(cmd_hack, name="hack")


def init_app():
    # app.add_typer(cmd_new, help="Create a new project")
    app.add_typer(cmd_add, help="Add a package")
    app.add_typer(cmd_hack)
    return app


def version_callback(value: bool):
    if value:
        print(f"Mod(Mojo Dep) CLI Version: {__version__}")
        raise typer.Exit()


# todo x: add global --options
@app.callback(short_help="-h")
def main(
    version: Annotated[
        Optional[bool],
        typer.Option(
            "--version", "-v", callback=version_callback, help="Show the version"
        ),
    ] = None,
):
    """
    Awesome Mojo Package Manager
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


@app.command("new", help="Create a new project: [--bin, --lib]")
def new_project(
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


@app.command("install", help="Install dependencies")
def install_deps():
    """
    Install dependencies
    """
    typer.echo(f"Install dependencies")


@app.command()
def build():
    """
    Build the project
    """
    typer.echo("Building the project")


@app.command("init")
def init_project():
    """
    Init the old project
    """
    typer.echo("init the old project")


@app.command("env", help="Environment information")
def env_info():
    typer.echo("Environment information")


@app.command(help="Doctor")
def doctor():
    typer.echo("fix env")


@app.command(help="Mojo workspace(monorepo)")
def workspace():
    typer.echo("Mojo workspace(monorepo)")


@app.command(help="Doctor")
def doctor():
    typer.echo("fix env")


@app.command(help="Doctor")
def doctor():
    typer.echo("fix env")
