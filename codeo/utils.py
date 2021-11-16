import os
import sys
import time

import requests
from bs4 import BeautifulSoup
from rich import print as rprint
from rich.console import Console
from rich.table import Table


def get_enviroment_vars():
    """Read user credentials to login codeo.app website from enviroment
    variables
    """
    USERNAME = os.environ.get("USER_NAME")
    PASSWORD = os.environ.get("PASSWORD")
    if not all((USERNAME, PASSWORD)):
        rprint(
            "[bold]Make sure to set the following enviroment variables:[bold]"
            " :crying_cat_face:\n"
            "[bold blue] * USER_NAME=...\n * PASSWORD=...\n"
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


def show_results(url):
    """Scrape results from codeo.app website and append them to row table."""
    console = Console()
    table = create_table_header()
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    tbody = soup.find("tbody")

    with console.status("[bold green] Working on test cases..."):
        time.sleep(1.5)
        for tr in tbody.find_all("tr"):
            case = tr.th.a
            result, time_, memory = tr.find_all("td")
            table.add_row(
                case.text.strip(),
                result.div.text.strip(),
                time_.text.strip(),
                memory.text.strip(),
            )
    problem = soup.find("h2").a.text
    author, date = soup.find("ul", class_="mb-4").find_all("li")
    console.print("Problem:", f"[bold red]{problem}[bold red]")
    console.print("* [bold]Author:[bold]", f"[red]{author.text[7:]}[red]")
    console.print("* [bold]Date:[bold]", f"{date.text[7:]}")
    console.print(table)
    score = soup.find("span", class_="font-weight-bold").text
    console.print("Total Score:", f"[bold]{score}[bold]")
