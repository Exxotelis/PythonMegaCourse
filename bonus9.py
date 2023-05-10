while True:
    password = input("Enter new password: ")
    result = {"length": False, "digit": False, "uppercase": False}

    if len(password) >= 8:
        result["length"] = True

    digit = False
    for i in password:
        if i.isdigit():
            digit = True
    result["digit"] = digit

    uppercase = False
    for i in password:
        if i.isupper():
            uppercase = True
    result["uppercase"] = uppercase

    if all(result.values()):
        print("Strong password")
        break
    else:
        print("Weak password. Please try again.")
        for key, value in result.items():
            if not value:
                print(f"Password should have {key}.")
