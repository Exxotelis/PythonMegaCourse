def get_todos(todos_args, filepath="files/todos.txt"):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        write_todos(todos_args)
    return todos_local


def write_todos(todos_args, filepath="files/todos.txt"):
    with open(filepath, 'w') as file:
        file.writelines(todos_args)


# if __name__ == "__main__":
#     print("Hello from Functions")
#     print(get_todos())
