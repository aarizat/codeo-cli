import os
import sys

from rich import print as rprint


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
