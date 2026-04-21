# CLI Expense Tracker

A lightweight command-line expense tracker written in Python. Expenses are stored locally in a CSV file and managed entirely from the terminal.

---

## Concepts used

* CLI subcommands via argparse
* CSV file I/O
* Modular Python project structure
* Date parsing and validation
* Command dispatch pattern

---

## Features

* Add, update, and delete expenses
* List all recorded expenses
* Generate expense summaries (total or by month)
* Automatic ID assignment
* Persistent storage using a local CSV file
* Date support with validation (MM/DD/YYYY)

---

## Project Structure

```
expense-tracker.py   # Main CLI entry point
cli.py               # Argument parsing and validation
handlers.py          # Command dispatcher
file_io.py           # CSV operations and core logic
expenses.csv         # Auto-created data storage file
```

---

## Requirements

* Python 3.7+
* Standard library only (no external dependencies)

---

## Installation

1. Clone or download the project:

```
git clone https://github.com/tfowl95/expense-tracker.git
cd expense-tracker
```

2. Ensure Python is installed:

```
python3 --version
```

3. Run directly:

```
python3 expense-tracker.py --help
```

---

## Usage

### Add an Expense

```
python3 expense-tracker.py add "groceries" --amount 25.50 --date 04/20/2026
```
If --date is omitted, today's date is used.

---

### Update an Expense

At least one field must be provided.
```
python3 expense-tracker.py update <id> [--description TEXT] [--amount VALUE] [--date MM/DD/YYYY]
```

Example:

```
python3 expense-tracker.py update 1 --amount 30.00
```

---

### Delete an Expense

```
python3 expense-tracker.py delete <id>
```

Example:

```
python3 expense-tracker.py delete 2
```

---

### List Expenses

```
python3 expense-tracker.py list
```

Output includes ID, amount, date, and description.

---

### View Summary

Total summary (all time)

```
python3 expense-tracker.py summary
```

Monthly summary

```
python3 expense-tracker.py summary --month <1-12>
```

Example:

```
python3 expense-tracker.py summary --month 4
```

---

## Data Storage

Expenses are stored in expenses.csv in the same directory as the script.

File format:

```
ID, Description, Amount, Date
```

Notes
* File is automatically created if missing
* IDs are unique and auto-generated
* Amounts are stored as floats with 2 decimal precision
* Dates are stored as MM/DD/YYYY

---

## Example Output

List command:

```
ID  Amount      Date          Description
1   $25.50      04/20/2026    groceries
2   $10.00      04/19/2026    coffee
```

Summary command:

```
Total expenses for April: $35.50
```

---

## Error Handling

The CLI validates:

* Missing required arguments
* Invalid command names
* Invalid date format (MM/DD/YYYY)
* Non-numeric IDs
* Update command requiring at least one field
* File read/write consistency

Common errors include:

* Invalid command
* Missing amount for add
* Invalid date format
* Expense ID not found (silent skip in update/delete logic)

---

## Notes

* Expense IDs are auto-incremented using the lowest available integer
* Update operations overwrite only specified fields
* CSV header is preserved on every write operation
* Summary can be global or month-specific

---

## License

No license specified.
