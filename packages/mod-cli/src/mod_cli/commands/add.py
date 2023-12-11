import typer

cmd_add = typer.Typer()


@cmd_add.command()
def add():
    """
    Add
    """
    typer.echo("Add a package")
