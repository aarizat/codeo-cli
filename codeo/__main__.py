import time

import mechanicalsoup as ms

from .cli import get_args
from .codeo import CodeoBrowser
from .utils import get_enviroment_vars, show_results


def main():
    args = get_args()

    with ms.StatefulBrowser() as browser:
        cb = CodeoBrowser(browser)
        username, password = get_enviroment_vars()
        cb.login(username, password)
        result = cb.submit_problem(args.url, args.file)
        time.sleep(1.5)
        show_results(result)


if __name__ == "__main__":
    main()
