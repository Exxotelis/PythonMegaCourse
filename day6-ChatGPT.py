while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ").strip()

            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo + "\n")

            file = open('files/todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show' | 'display':  # same result
            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                # item = item.title()  # capitalize the first letter of any words you type in
                row = f"{index + 1}: {item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: ")) - 1

            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            new_todo = input("Enter new todo: ").strip()
            todos[number] = new_todo + "\n"

            file = open('files/todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'complete':
            number = int(input("Number of the todo to complete: ")) - 1

            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.pop(number)

            file = open('files/todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'exit':
            break
        case _:
            print("Hey, you entered an unknown command")

print("Bye!!")
