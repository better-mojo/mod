
from typing import Annotated

import typer

cmd_add = typer.Typer(
    help="Add a package", no_args_is_help=True, invoke_without_command=True
)


@cmd_add.callback()
def cb(
    package: Annotated[
        list[str],
        typer.Argument(
            metavar="PACKAGE",
            help="Add a package to dependencies",
        ),
    ],
    dev: Annotated[
        bool,
        typer.Option(
            "--dev",
            "-d",
            help="Add a development package to dependencies",
        ),
    ] = False,
):
    """
    Add
    """

    if dev:
        typer.echo(f"Add {package} to development dependencies")
    else:
        typer.echo(f"Add {package} to dependencies")
