#!/usr/bin/env python3

from cli import cli_arg_parse
from storage import get_file_path, create_file_if_missing, get_csv_contents

args = cli_arg_parse()
print(args.date)
file_path = get_file_path()
create_file_if_missing(file_path)

expenses = get_csv_contents(file_path)