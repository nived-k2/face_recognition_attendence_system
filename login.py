import tkinter as tk
from tkinter import messagebox
import os

def login():
    username = username_entry.get()
    password = password_entry.get()

    # Check if username and password match
    if username == "admin" and password == "admin":
        # Open first page GUI
        os.system("python firstpage_gui.py")
    elif username == "student" and password == "student":
        # Open student GUI
        os.system("python student_gui.py")
    else:
        messagebox.showerror("Error", "Invalid username or password")

# Create the main window
root = tk.Tk()
root.title("Login")

# Username label and entry
username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=5)

# Password label and entry
password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

# Login button
login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
