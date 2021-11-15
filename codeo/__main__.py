import mechanicalsoup as ms

from .codeo import CodeoBrowser
from .cli import get_args
from .utils import get_enviroment_vars, show_results


def main():

    username, password = get_enviroment_vars()
    args = get_args()

    with ms.StatefulBrowser() as browser:
        if args.file:
            cb = CodeoBrowser(browser)
            cb.login(username, password)
            cb.submit_problem(args.url, args.file)
        else:
            show_results(args.result)


if __name__ == "__main__":
    main()
