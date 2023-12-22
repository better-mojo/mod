import typer
from loguru import logger

cmd_new = typer.Typer()


@cmd_new.command("new")
def new(project_name: str):
    """
    New
    """
    typer.echo("New a mojo project")
    logger.info(f"project_name: {project_name}")
