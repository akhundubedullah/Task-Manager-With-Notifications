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


def task_manager():
    root = tk.Tk()
    root.title("Management")
    
    task_window = tk.Toplevel
    task_window.title("Task Manager")

    task_listbox = tk.Listbox(task_window)
    task_listbox.pack()

    task_entry = tk.Entry
    task_entry.pack()

    root.mainloop()





#def main():
    #print("Hello")
    #print("Enter 1 ii you want to SignUp")
    #print("Enter 2 if you want to Login")

    #number = input("Enter your desired Number: ")
    #if(number == 1):
    #    signup()

    #elif(number == 2):
    #    login()

    #else:
        #print("Please try again.")


#main()

task_manager()