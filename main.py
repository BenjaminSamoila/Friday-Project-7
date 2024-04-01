import tkinter as tk
from tkinter import messagebox
import sqlite3
import re

# Connect to the SQLite database
conn = sqlite3.connect('database.spl.db')
c = conn.cursor()

# Create a table for users if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, email TEXT, password TEXT)''')
conn.commit()

def validate_email(email):
    # Simple regex for checking if the email has @ and ends with .com or .edu
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

def signup():
    def add_user():
        email = email_entry.get()
        password = password_entry.get()
        if not validate_email(email):
            message_label.config(text="Invalid email format", fg="red")
            return
        c.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
        conn.commit()
        message_label.config(text="Account created successfully", fg="green")

    signup_window = tk.Toplevel(root)
    signup_window.title("Sign Up")

    email_label = tk.Label(signup_window, text="Email:")
    email_label.pack()
    email_entry = tk.Entry(signup_window)
    email_entry.pack()

    password_label = tk.Label(signup_window, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(signup_window, show="*")
    password_entry.pack()

    signup_button = tk.Button(signup_window, text="Sign Up", command=add_user)
    signup_button.pack()

    message_label = tk.Label(signup_window, text="", fg="black")
    message_label.pack()

def signin():
    def check_credentials():
        email = email_entry.get()
        password = password_entry.get()
        c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
        user = c.fetchone()
        if user:
            message_label.config(text="Log in successful", fg="green")
        else:
            message_label.config(text="Email or password incorrect", fg="red")

    signin_window = tk.Toplevel(root)
    signin_window.title("Sign In")

    email_label = tk.Label(signin_window, text="Email:")
    email_label.pack()
    email_entry = tk.Entry(signin_window)
    email_entry.pack()

    password_label = tk.Label(signin_window, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(signin_window, show="*")
    password_entry.pack()

    signin_button = tk.Button(signin_window, text="Sign In", command=check_credentials)
    signin_button.pack()

    message_label = tk.Label(signin_window, text="", fg="black")
    message_label.pack()

root = tk.Tk()
root.title("User Portal")

signup_button = tk.Button(root, text="Sign Up", command=signup)
signup_button.pack()

signin_button = tk.Button(root, text="Sign In", command=signin)
signin_button.pack()

root.mainloop()