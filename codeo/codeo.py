import argparse
import os
import sys

from mechanicalsoup import LinkNotFoundError
from rich import print as rprint

AVAILABLE_LANGUAGES = {
    ".js": "JavaScript",
    ".py": "Python 3",
    ".java": "Java",
    ".cpp": "C++",
    ".rb": "Ruby",
    ".go": "Go",
    ".cs": "C#",
    ".c": "C",
}


class CodeoBrowser:
    def __init__(self, browser):
        self.browser = browser

    def login(self, username: str, password: str) -> None:
        """Log in to codeo.app"""
        self.browser.open("http://127.0.0.1:3000/usuarios/login")
        form = self.browser.select_form()
        form.set_input({"user[username]": username})
        form.set_input({"user[password]": password})
        form.choose_submit("commit")
        self.browser.submit_selected()
        if self.browser.url == "http://127.0.0.1:3000/usuarios/login":
            rprint(
                ":eyes: [bold]Please check your login credentials[bold] :eyes:"
            )
            sys.exit()

    def submit_problem(self, problem_url: str, filename: str) -> None:
        """Submit source code to codeo.app to be verified."""
        self.browser.open(problem_url)
        try:
            form = self.browser.select_form()
        except LinkNotFoundError:
            rprint(
                ":no_entry_sign: [bold]Please check url problem is"
                "correct[bold] :no_entry_sign:"
            )
            sys.exit()
        form.set_select({"submission[language]": self.get_language(filename)})
        form.set_textarea(
            {"submission[source_code]": self.read_source_code(filename)}
        )
        form.choose_submit("commit")
        self.browser.submit_selected()
        return self.browser.url

    def close(self) -> None:
        """Close browser session"""
        self.browser.close()

    @staticmethod
    def read_source_code(filename: str) -> str:
        """Rread source code from file."""
        if not os.path.isfile(filename):
            raise argparse.ArgumentTypeError(f"No such file: {filename}")

        with open(os.path.abspath(filename), mode="rt") as fp:
            return fp.read()

    @staticmethod
    def get_language(filename: str) -> str:
        """Get the programming language to use in codeo.app from the file
        extension
        """
        _, extension = os.path.splitext(filename)
        if extension not in AVAILABLE_LANGUAGES:
            rprint(
                "[bold]Programming language not available yet.[bold] "
                ":see_no_evil:"
            )
            sys.exit()
        return AVAILABLE_LANGUAGES.get(extension)
