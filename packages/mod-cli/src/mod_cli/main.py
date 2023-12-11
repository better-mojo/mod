import typer

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


def main(name: str = typer.Option("World", "-n", "--name")):
    print(f"Hello {name}")


if __name__ == "__main__":
    typer.run(main)
