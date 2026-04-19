#!/usr/bin/env python3

from cli import cli_arg_parse
from storage import set_output_path, create_file_if_missing

args = cli_arg_parse()
output_file = set_output_path()
create_file_if_missing(output_file)