import tkinter as tk
from tkinter import messagebox
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('database.spl.db')
c = conn.cursor()

# Create a table for users if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, email TEXT, password TEXT)''')
conn.commit()

def signup():
    def add_user():
        email = email_entry.get()
        password = password_entry.get()
        c.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
        conn.commit()
        messagebox.showinfo("Success", "Account created successfully")

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

def signin():
    def check_credentials():
        email = email_entry.get()
        password = password_entry.get()
        c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
        user = c.fetchone()
        if user:
            messagebox.showinfo("Success", "Log in successful", icon="info")
        else:
            messagebox.showerror("Error", "Email or password incorrect", icon="error")

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

root = tk.Tk()
root.title("User Portal")

signup_button = tk.Button(root, text="Sign Up", command=signup)
signup_button.pack()

signin_button = tk.Button(root, text="Sign In", command=signin)
signin_button.pack()

root.mainloop()