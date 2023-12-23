import typer

cmd_add = typer.Typer(help="Add a package")


@cmd_add.command()
def add():
    """
    Add
    """
    typer.echo("Add a package")
