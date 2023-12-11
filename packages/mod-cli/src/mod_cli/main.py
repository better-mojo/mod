import typer
from typing_extensions import Annotated

app = typer.Typer()


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
