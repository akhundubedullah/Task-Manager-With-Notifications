from tkinter import *
import tkinter as tk

credentials = {}

def check():
    username = e1.get()
    password = e2.get()
    if username in credentials and credentials[username] == password:
        print(f"Login successful for {username}")
    else:
        print("Login failed. Invalid username or password.")

def login():
    global e1, e2  # make e1 and e2 global so they can be accessed in check()
    root = tk.Tk()
    root.title("Login Page")

    tk.Label(root, text='Username').grid(row=0)
    tk.Label(root, text='Password').grid(row=1)

    e1 = tk.Entry(root)
    e2 = tk.Entry(root, show='*')  # show='*' hides the password
    e1.grid(row=0, column=1, sticky=tk.W)
    e2.grid(row=1, column=1, sticky=tk.W)

    button = tk.Button(root, text='Submit', width=25,command=check)
    button.grid(row=2, columnspan=2)  
    root.mainloop()

def signup():
    def store_credentials():
        username = e1.get()
        password = e2.get()
        credentials[username] = password
        print(f"Credentials stored for {username}")
        root.destroy()

    root = tk.Tk()
    root.title("Signup Page")

    tk.Label(root, text='Username').grid(row=0)
    tk.Label(root, text='Password').grid(row=1)

    e1 = tk.Entry(root)
    e2 = tk.Entry(root, show='*')  # show='*' hides the password
    e1.grid(row=0, column=1, sticky=tk.W)
    e2.grid(row=1, column=1, sticky=tk.W)
    
    button = tk.Button(root, text='Submit', width=25, command=store_credentials)
    button.grid(row=2, columnspan=2)  
    root.mainloop()

signup()
login()
