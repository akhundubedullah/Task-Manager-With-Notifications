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
        
    task_window = tk.Toplevel
    task_window.title("Task Manager")

    task_listbox = tk.Listbox(task_window)
    task_listbox.pack()

    task_entry = tk.Entry
    task_entry.pack()

    add_button = tk.Button(task_window, text="Add Task", command=lambda: add_task(task_listbox, task_entry))
    add_button.pack()

    delete_button = tk.button(task_window, text = "Delete Task",command = lambda :delete_task(task_listbox))
    delete_button.pack()

    update_button = tk.Button(task_window, text = "Update Task",command = lambda :update_task(task_listbox,task_entry))
    update_button.pack()


    def add_task(task_listbox, task_entry):
        task = task_entry.get()
        if task:
            task.append(task) # what will happen if i remove this
            task_listbox.insert(tk.END, task)
            task_entry.delete(0, tk.END)
        else:
            tk.messagebox.showwarning("Input Error", "Please enter a task.")


    def delete_task(task_listbox):
        try:
            task_index = task_listbox.curselection()
            task_listbox.delete(task_index)
        except:
            tk.messagebox.showwarning("Selection Error", "Please select a task to delete.")    
