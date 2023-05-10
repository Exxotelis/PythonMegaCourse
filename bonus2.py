# password = input("Enter password: ")
#
# while password != "pass123":
#     password = input("Enter password: ")
#
# print("Password was successful")


# waiting_list = ["sen", "ben", "john"]
#
# waiting_list.sort()
# for index, item in enumerate(waiting_list):

#     row = f"{ index + 1}.{item.capitalize()}"
#     print(row)

# menu = ["pasta", "pizza", "salad"]
#
# for i, j in enumerate(menu):
#     print(f"{i}.{j}")
while True:
    password = input("Enter new password: ")
    result = {"length": False, "digit": False, "uppercase": False}

    if len(password) >= 8:
        result["length"] = True
    else:
        result["length"] = False

    digit = False
    for i in password:
        if i.isdigit():
            digit = True

    result["digit"] = digit

    uppercase = False
    for i in password:
        if i.isupper():
            uppercase = True

    result["upper-case"] = uppercase

    print(result)

    if all(result.values()):
        print("Strong password")
    else:
        print("Please try again")


# print(result)



