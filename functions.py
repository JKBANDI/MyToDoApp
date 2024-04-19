FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file:
        todos_ret = file.readlines()
    return todos_ret


def write_todo(todos_arg, filepath=FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)