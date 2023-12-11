import typer

cmd_new = typer.Typer()


@cmd_new.command()
def new():
    """
    New
    """
    typer.echo("New a mojo project")
