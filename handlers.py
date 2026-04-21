from file_io import add_expense

def dispatch(args, file_path):
    handlers = {
        "add": handle_add,
        "list": handle_list,
        "summary": handle_summary,
        "delete": handle_delete,
    }
    handlers[args.command](args, file_path)

def handle_add(args, file_path):
    add_expense(args, file_path)

def handle_list(args, file_path):
    pass

def handle_summary(args, file_path):
    pass

def handle_delete(args, file_path):
    pass