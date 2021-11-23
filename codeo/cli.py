import argparse


def get_args():
    parser = argparse.ArgumentParser(
        description="Submit code to codeo.app website",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    required_args = parser.add_argument_group("required arguments")
    required_args.add_argument(
        "-u",
        "--url",
        action="store",
        help="Url of the problem to submit",
        required=True,
    )
    required_args.add_argument(
        "-f",
        "--file",
        action="store",
        help="File with the code",
        required=True,
    )
    return parser.parse_args()
