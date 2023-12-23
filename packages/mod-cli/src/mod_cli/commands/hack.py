import typer


cmd_hack = typer.Typer(help="Hack Mojo Std Library")


@cmd_hack.command()
def build():
    typer.echo("Building the 3rd Package to mojopkg")


@cmd_hack.command()
def clean():
    typer.echo("Cleaning the 3rd Package to mojopkg")


@cmd_hack.command()
def add():
    typer.echo("Adding 3rd Package(mojopkg) to Mojo Std Library Directory")


@cmd_hack.command()
def remove():
    typer.echo("Removing 3rd Package(mojopkg) from Mojo Std Library Directory")


@cmd_hack.command()
def auto():
    typer.echo("Auto Build & Add 3rd Package(mojopkg) to Mojo Std Library Directory")


@cmd_hack.command()
def edit():
    typer.echo("Edit the 3rd Package(mojopkg)")
