from file_io import add_expense, update_expense, list_expenses, delete_expense, summary_expense

def dispatch(args, file_path):
    handlers = {
        "add": handle_add,
        "update": handle_update,
        "list": handle_list,
        "summary": handle_summary,
        "delete": handle_delete,
    }
    handlers[args.command](args, file_path)

def handle_add(args, file_path):
    add_expense(args, file_path)

def handle_update(args, file_path):
    update_expense(args, file_path)

def handle_list(args, file_path):
    list_expenses(args, file_path)

def handle_delete(args, file_path):
    delete_expense(args, file_path)

def handle_summary(args, file_path):
    summary_expense(args, file_path)