# password = input("Please enter your password: ")
#
# if len(password) >= 7:
#     print("Great job")
# else:
#     print("Week password mate")

#
# length = float(input("Enter length: "))
# width = float(input("Enter width: "))
#
# perimeter = (length + width) * 2
# area = length * width
#
# print("Perimeter is", perimeter)
# print("Area is", area)
#
# if perimeter < 14 or area > 10:
#     print("OK")
# else:
#     print("NOT OK")
#     try:
#         width = float(input("Enter the rectangle width: "))
#         length = float(input("Enter the rectangle length: "))
#         if width == length:
#             exit("This looks like square.")
#     area = width * length
#     print(area)
# except ValueError:
#     print("Please enter a number.")


total_value = input("ENTER TOTAL VALUE: ")
value = input("ENTER VALUE: ")

if not (total_value.isdigit() and value.isdigit()):
    print("Invalid input. Please enter a valid number.")
else:
    total_value = float(total_value)
    value = float(value)
    if total_value == 0:
        print("Your total value cannot be zero")
    else:
        percentage = (value / total_value) * 100
        if value == 0:
            print("The percentage is 0%")
        else:
            print(f"THIS IS {percentage}%")



