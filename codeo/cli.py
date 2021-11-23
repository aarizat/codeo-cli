import argparse


def get_args():
    parser = argparse.ArgumentParser(
        description="Submit code to codeo.app website",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-u",
        "--url",
        action="store",
        help="Url of the problem to submit",
        required=True,
    )
    parser.add_argument(
        "-f",
        "--file",
        action="store",
        help="File with the code",
        required=True,
    )
    return parser.parse_args()
