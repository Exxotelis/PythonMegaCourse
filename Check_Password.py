# import tkinter as tk
# from tkinter import messagebox


# def check_password():
#     password = entry.get()
#     result = []

#     if len(password) >= 8:
#         result.append(True)
#     else:
#         result.append(False)

#     digit = False
#     for i in password:
#         if i.isdigit():
#             digit = True

#     result.append(digit)

#     uppercase = False
#     for i in password:
#         if i.isupper():
#             uppercase = True

#     result.append(uppercase)

#     if all(result):
#         messagebox.showinfo("Password Strength", "Strong password")
#     else:
#         message = "Weak password. Please try again and make sure your password has at least 8 characters, a digit, " \
#                   "and an uppercase letter. "
#         messagebox.showerror("Password Strength", message)
#         entry.delete(0, tk.END)


# # Create the GUI
# root = tk.Tk()
# root.title("Password Checker")

# label = tk.Label(root, text="Enter a password:")
# label.pack()

# entry = tk.Entry(root, show="*")
# entry.pack()

# button = tk.Button(root, text="Check Password", command=check_password)
# button.pack()

# root.mainloop()
