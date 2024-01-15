import subprocess
from enum import Enum
from pathlib import Path
from typing import (
    Annotated,
    Optional,
)

import typer

from mod_cli.commands.add import cmd_add
from mod_cli.commands.hack import cmd_hack
from mod_cli.commands.workspace import cmd_workspace
from mod_cli.core.new import ProjectHelper
from mod_cli.core.package.package import PackageHelper

__version__ = "0.1.2"  # todo x: sync with pyproject.toml version


class AppPanelType(str, Enum):
    cmds = "🔥 Commands"
    project = "Management Commands"
    development = "Development Commands"
    environment = "Environment Commands"
    proxy = "Proxy Commands"


def version_callback(value: bool):
    if value:
        print(f"Mod(Mojo Dep) CLI Version: {__version__}")
        raise typer.Exit()


app = typer.Typer(
    help=f"Mod({__version__}) - Awesome Mojo Package Manager",
    no_args_is_help=True,
    name="Mod",
)

# app.add_typer(cmd_new, help="Create a new project")
app.add_typer(cmd_add, name="add2", rich_help_panel=AppPanelType.development)
app.add_typer(cmd_hack, name="hack", rich_help_panel=AppPanelType.development)
app.add_typer(cmd_workspace, name="workspace", rich_help_panel=AppPanelType.project)


# todo x: add global --options
@app.callback(invoke_without_command=True)
def main(
    h: Annotated[
        Optional[bool],  # fix
        typer.Option(
            "--help",
            "-h",
            help="Show this help message",
        ),
    ] = False,
    version: Annotated[
        Optional[bool],  # fix
        typer.Option(
            "--version",
            "-v",
            # callback=version_callback,
            help="Show the version",
        ),
    ] = False,
):
    """
    Awesome Mojo Package Manager
    """
    from mod_cli.core.cache import PackageCacheHelper

    ph = PackageCacheHelper()
    ph.init()

    # -v option
    if version:
        print(f"🔥 Mod: {__version__}")
        raise typer.Exit()

    # -h option
    if h:
        import subprocess

        subprocess.run(["mod"])
        print("🔥 Mod: %s" % __version__)
        raise typer.Exit()


class NewType(str, Enum):
    bin = "bin"
    lib = "lib"


def is_valid_directory(path):
    import re

    if isinstance(path, Path):
        path = str(path)

    pattern = r"^([\w.-]+)+/?$"
    return re.match(pattern, path) is not None


@app.command(
    "new",
    help="Create a new project: [--bin, --lib]",
    rich_help_panel=AppPanelType.project,
)
def new_project(
    project_name: Annotated[
        Path,
        typer.Argument(metavar="path", help="The path to create the project at."),
    ],
    is_bin: Annotated[
        bool,
        typer.Option("--bin", help="Use a binary (application) template [default]"),
    ] = False,
    is_lib: Annotated[
        bool,
        typer.Option("--lib", help="Use a library template"),
    ] = False,
    # typ: Annotated[NewType, typer.Option("--type", help="The type of project")] = NewType.bin,
):
    typ = NewType.bin
    if is_lib:
        typ = NewType.lib
    if is_bin:
        typ = NewType.bin

    h = ProjectHelper()
    h.new(project_name=project_name, project_type=typ)

    if is_lib:
        typer.echo(f"Created library `{project_name}` package")
    else:
        typer.echo(f"Created binary (application) `{project_name}` package")


@app.command(
    "install",
    help="Install dependencies",
    rich_help_panel=AppPanelType.development,
)
def install_deps():
    """
    Install dependencies
    """
    typer.echo("Install dependencies")


@app.command(
    rich_help_panel=AppPanelType.development,
)
def build():
    """
    Build the project
    """
    typer.echo("Building the project")


@app.command(
    "init",
    rich_help_panel=AppPanelType.project,
)
def init_project():
    """
    Init the old project
    """
    typer.echo("init the old project")


@app.command(
    "add",
    help="Add dependencies",
    rich_help_panel=AppPanelType.development,
    no_args_is_help=True,
)
def add_dep(
    package_path: Annotated[
        list[str],
        typer.Argument(
            metavar="PACKAGE_PATH",
            help="Add a package to dependencies",
        ),
    ] = None,
    package_name: Annotated[
        Optional[str],
        typer.Option(
            metavar="PACKAGE_NAME",
            help="the name of the package to add",
        ),
    ] = None,
    is_dev: Annotated[
        Optional[bool],
        typer.Option(
            "--dev",
            "-d",
            help="BOOL: Add a development package to dependencies",
        ),
    ] = False,
    version: Annotated[
        Optional[str],  # todo x: fix this
        typer.Option(
            "--version",
            help="The version of the package to add",
        ),
    ] = None,
    branch: Annotated[
        Optional[str],  # fix
        typer.Option(
            "--branch",
            help="The branch of the package to add",
        ),
    ] = None,
):
    typer.echo(
        f"input args: {package_path}, name: {package_name}, dev: {is_dev}, v: {version}, branch: {branch}"
    )
    if is_dev:
        typer.echo(f"Add {package_path} to development dependencies")
    else:
        typer.echo(f"Add {package_path} to dependencies")

    h = PackageHelper()
    if not h.is_mod_file_exists():
        typer.echo("mod.toml not found in current directory")
        raise typer.Abort()
    h.add_many(
        packages=package_path,
        package_name=package_name,
        is_dev=is_dev,
        version=version,
        branch=branch,
    )


@app.command(
    "remove",
    help="Remove dependencies",
    rich_help_panel=AppPanelType.development,
    no_args_is_help=True,
)
def remove_dep(
    package: Annotated[
        list[str],
        typer.Argument(
            metavar="PACKAGE",
            help="Remove a package from dependencies",
        ),
    ],
    dev: Annotated[
        bool,
        typer.Option(
            "--dev",
            "-d",
            help="Remove a development package from dependencies",
        ),
    ] = False,
):
    h = PackageHelper()
    h.remove_many(packages=package, is_dev=dev)


@app.command("env", help="Environment information")
def env_info():
    typer.echo("Environment information")


@app.command(help="Doctor")
def doctor():
    typer.echo("fix env")


@app.command(
    "mojo",
    help="Run mojo command",
    rich_help_panel=AppPanelType.proxy,
)
def mojo_exec(
    args: Annotated[
        list[str],
        typer.Argument(
            metavar="COMMAND",
            help="Run mojo command",
        ),
    ] = None,
):
    proxy_exec(["mojo", *args])


@app.command(
    "poetry",
    help="Run Poetry(Python) command",
    rich_help_panel=AppPanelType.proxy,
)
def poetry_exec(
    args: Annotated[
        list[str],
        typer.Argument(
            metavar="COMMAND",
            help="Run poetry command",
        ),
    ] = None,
):
    proxy_exec(["poetry", *args])


@app.command(
    "pdm",
    help="Run PDM(Python) command",
    rich_help_panel=AppPanelType.proxy,
)
def pdm_exec(
    args: Annotated[
        list[str],
        typer.Argument(
            metavar="COMMAND",
            help="Run pdm command",
        ),
    ] = None,
):
    proxy_exec(["pdm", *args])


def proxy_exec(cmds: list):
    print(f"Exec Command: {cmds}")
    try:
        ret = subprocess.run(
            cmds,
            # shell=True,
            check=True,
            # stdout=subprocess.PIPE,
            # stderr=subprocess.PIPE,
            encoding="utf-8",
            capture_output=True,
            text=True,
        )

        if ret.stdout:
            print(ret.stdout)
        if ret.stderr:
            print(ret.stderr)
    except subprocess.CalledProcessError as e:
        print(f"{e.stderr}")  # todo x: print exec exception error
    except subprocess.SubprocessError as e:
        print(f"{e}")
    except Exception as e:
        print(f"{e}")
