import argparse


def get_args():
    parser = argparse.ArgumentParser(
        description="Submit code to codeo website",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-u",
        "--url",
        action="store",
        help="Url of the problem to submit",
    )
    parser.add_argument(
        "-f",
        "--file",
        action="store",
        help="File with the code",
    )
    parser.add_argument(
        "-r",
        "--result",
        action="store",
        help="Show results",
    )
    return parser.parse_args()
