import argparse
from datetime import datetime

def parse_date(input):
    try:
        return datetime.strptime(input, "%m/%d/%Y").date()
    except ValueError:
        raise argparse.ArgumentTypeError("Use MM/DD/YYYY format")

def cli_arg_parse():
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest="command")

    # add command
    add_parser = subparser.add_parser("add")
    add_parser.add_argument("--description", type = str, required = True)
    add_parser.add_argument("--amount", type = float, required = True)
    add_parser.add_argument("--date", type = parse_date)

    return parser.parse_args()