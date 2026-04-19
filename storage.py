from pathlib import Path

def set_output_path():
    script_dir = Path(__file__).resolve().parent
    return script_dir / "expenses.csv"

def create_file_if_missing(output_file):
    if not Path(output_file).exists():
        with open(output_file, "w") as file:
            file.close()