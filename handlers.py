def dispatch(args):
    handlers = {
        "add": handle_add,
        "list": handle_list,
        "summary": handle_summary,
        "delete": handle_delete,
    }
    handlers[args.command](args)

def handle_add(args):
    pass



def handle_list(args):
    pass

def handle_summary(args):
    pass

def handle_delete(args):
    pass