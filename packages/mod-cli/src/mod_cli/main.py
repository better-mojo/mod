import typer
from typing_extensions import Annotated

from .commands import cmd_add, cmd_new

app = typer.Typer()
app.add_typer(cmd_new, name="new", help="Create a new project")
app.add_typer(cmd_add, name="add", help="Add a package")


@app.callback()
def callback():
    """
    Awesome Portal Gun
    """


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
    typer.run(main)
