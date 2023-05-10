import tkinter as tk
import webbrowser


def search():
    query = search_entry.get()
    webbrowser.open("https://www.google.co.uk/search?q=" + query)


root = tk.Tk()
root.title("Search")

search_label = tk.Label(root, text="Search:")
search_label.grid(row=0, column=0)

search_entry = tk.Entry(root, width=50)
search_entry.grid(row=0, column=1)

search_button = tk.Button(root, text="Search", command=search)
search_button.grid(row=1, column=0, columnspan=2, pady=10)

root.mainloop()
