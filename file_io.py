from pathlib import Path
import csv
from datetime import datetime

def get_file_path():
    script_dir = Path(__file__).resolve().parent
    return script_dir / "expenses.csv"

def create_file_if_missing(output_file):
    headers = ("ID", "Description", "Amount", "Date")
    if not Path(output_file).exists():
        with open(output_file, "w") as file:
            writer=csv.writer(file)
            writer.writerow(headers)

def get_csv_contents(file_path):
    with open(file_path, "r") as file:
        return list(csv.reader(file))
    
def get_unique_id(file_path):
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        next(reader)

        #populate existing_ids with what is found in the .csv file
        existing_ids = []
        for row in reader:
            existing_ids.append(int(row[0]))
        
        # find and return a unique id
        id_found = False
        new_id = 1
        while not id_found:
            if new_id in existing_ids:
                new_id += 1
            else:
                id_found = True
        return new_id

    
def add_expense(args, file_path):
    new_id = get_unique_id(file_path)
    with open(file_path, "a") as file:
        writer = csv.writer(file)
        writer.writerow((new_id, args.description, f"{args.amount:.2f}", args.date.strftime("%m/%d/%Y")))
    print(f"Expense added successfully (ID: {new_id})")

def update_expense(args, file_path):
    new_csv = []

    with open(file_path, "r") as file:
        reader = csv.reader(file)
        new_csv.append(next(reader))
        for row in reader:
            if row and int(row[0]) == args.id:
                if args.description:
                    row[1] = args.description
                if args.amount:
                    row[2] = args.amount
                if args.date:
                    row[3] = args.date.strftime("%m/%d/%Y")
            new_csv.append(row)
    
    with open(file_path, "w") as file:
        writer = csv.writer(file)
        writer.writerows(new_csv)
    
    print(f"Expense updated successfully.")

def list_expenses(args, file_path):
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        print(f"{header[0]:4}{header[2]:12}{header[3]:14}{header[1]:10}")

        for row in reader:
            print(f"{row[0]:4}${row[2]:11}{row[3]:14}{row[1]:10}")

def delete_expense(args, file_path):
    new_csv = []
    
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        new_csv.append(next(reader))
        for row in reader:
            if row and int(row[0]) != args.id:
                new_csv.append(row)
    
    with open(file_path, "w") as file:
        writer = csv.writer(file)
        writer.writerows(new_csv)

    print(f"Expense updated successfully.")

def summary_expense(args, file_path):
    if args.month:

        months = {
            1: "January",
            2: "February",
            3: "March",
            4: "April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September",
            10: "October",
            11: "November",
            12: "December"
        }

        with open(file_path, "r") as file:
            reader = csv.reader(file)
            next(reader)
            sum = 0
            for row in reader:
                row_date = datetime.strptime(row[3], "%m/%d/%Y").date()
                row_month = row_date.month
                if args.month == row_month:
                    sum += float(row[2])
        print(f"Total expenses for {months[args.month]}: ${sum:.2f}")
    else:
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            next(reader)
            sum = 0
            for row in reader:
                sum += float(row[2])
        print(f"Total expenses: ${sum:.2f}")