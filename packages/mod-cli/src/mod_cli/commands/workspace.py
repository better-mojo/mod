import typer


cmd_workspace = typer.Typer(help="Mojo Workspace Manger", no_args_is_help=True)


@cmd_workspace.command("init")
def init_workspace():
    typer.echo("Init mojo workspace")


@cmd_workspace.command("add")
def add_to_workspace():
    typer.echo("add a mojo project to workspace")


@cmd_workspace.command("remove")
def remove_from_workspace():
    typer.echo("remove a mojo project from workspace")


@cmd_workspace.command("list")
def list_workspace():
    typer.echo("list all mojo projects in workspace")
