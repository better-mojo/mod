import typer


cmd_workspace = typer.Typer(help="Hack Mojo Std Library", no_args_is_help=True)


@cmd_workspace.command()
def init():
    typer.echo("Init mojo workspace")


@cmd_workspace.command()
def add():
    typer.echo("add ")
    typer.echo("Cleaning the 3rd Package to mojopkg")


@cmd_workspace.command()
def add():
    typer.echo("Adding 3rd Package(mojopkg) to Mojo Std Library Directory")


@cmd_workspace.command()
def remove():
    typer.echo("Removing 3rd Package(mojopkg) from Mojo Std Library Directory")


@cmd_workspace.command()
def auto():
    typer.echo("Auto Build & Add 3rd Package(mojopkg) to Mojo Std Library Directory")


@cmd_workspace.command()
def edit():
    typer.echo("Edit the 3rd Package(mojopkg)")
