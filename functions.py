FILEPATH = "files\\todos.txt"


def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_args, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_args)


# if __name__ == "__main__":
#     print("Hello from Functions")
#     print(get_todos())
print(get_todos())