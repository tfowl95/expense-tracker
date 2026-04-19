import argparse

def cli_arg_parse():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")

# add command
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("--description", type=str, required=True)
    add_parser.add_argument("--amount", type=float, required=True)

    return parser.parse_args()