from pathlib import Path
import csv

def get_file_path():
    script_dir = Path(__file__).resolve().parent
    return script_dir / "expenses.csv"

def create_file_if_missing(output_file):
    if not Path(output_file).exists():
        with open(output_file, "w") as file:
            file.close()

def get_csv_contents(file_path):
    with open(file_path, "r") as file:
        return list(csv.reader(file))