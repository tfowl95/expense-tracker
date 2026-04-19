#!/usr/bin/env python3

from cli import arg_parse
from pathlib import Path

args = arg_parse()

script_dir = Path(__file__).resolve().parent
output_file = script_dir / "expenses.csv"

