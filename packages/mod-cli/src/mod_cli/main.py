import typer
from typing_extensions import Annotated
from loguru import logger

from enum import Enum

from mod_cli.commands import cmd_add, cmd_new

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


@app.command(help="Create a new project: --bin, --lib, --app")
def new(
    project_name: str,
    typ: Annotated[NewType, typer.Option("--type", help="The type of project")] = NewType.bin,
):
    """
    New
    """
    typer.echo("New a mojo project")
    logger.info(f"project_name: {project_name}, project_type: {typ}")


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


def main(name: Annotated[str, typer.Option("-n", "--name")] = "World"):
    print(f"Hello {name}")


if __name__ == "__main__":
    # typer.run(main)
    app()
