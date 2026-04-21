import argparse
from datetime import datetime

def parse_date(input):
    try:
        return datetime.strptime(input, "%m/%d/%Y").date()
    except ValueError:
        raise argparse.ArgumentTypeError("Use MM/DD/YYYY format")

def cli_arg_parse():
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest="command", required = True)

    # add command
    add_parser = subparser.add_parser("add")
    add_parser.add_argument("--description", type = str, required = True)
    add_parser.add_argument("--amount", type = float, required = True)
    add_parser.add_argument("--date", type = parse_date, default = datetime.today().date())

    # update command
    update_parser = subparser.add_parser("update")
    update_parser.add_argument("id", type = int)
    update_parser.add_argument("--description", type = str)
    update_parser.add_argument("--amount", type = float)
    update_parser.add_argument("--date", type = parse_date)

    # list command
    update_parser = subparser.add_parser("list")
    

    args = parser.parse_args()

    # additional validation check for update command
    if args.command == "update" and args.description == None and args.amount == None and args.date == None:
        parser.error("'update' command requires at least one optional argument to update: --description --amount --date")

    return args