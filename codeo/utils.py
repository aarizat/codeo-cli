import os
import sys

from rich import print as rprint
from rich.table import Table


def get_enviroment_vars():
    """Read user credentials to login codeo.app website from enviroment
    variables
    """
    USERNAME = os.environ.get("USER_NAME")
    PASSWORD = os.environ.get("PASSWORD")
    if not all((USERNAME, PASSWORD)):
        rprint(
            "[bold]Make sure to set the following enviroment variables:[bold] :crying_cat_face: \
            \n [bold blue]* USER_NAME\n * PASSWORD\n"
        )
        sys.exit()
    return USERNAME, PASSWORD


def create_table_header() -> Table:
    """Table header to display in stdout and show results scraped from
    codeo.app
    """
    table = Table(show_header=True, header_style="bold")
    table.add_column("Case", justify="center", style="red")
    table.add_column("Result", justify="left")
    table.add_column("Time", justify="center")
    table.add_column("Memory", justify="center")
    return table