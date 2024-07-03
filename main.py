from asyncio import Task
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from plyer import notification


credentials = {}

def send_notification(title,message):
    notification.notify(
        title = title,
        app_name = "Task Manager",
        timeout = 10,
    )

def check():
    username = e1.get()
    password = e2.get()
    if username in credentials and credentials[username] == password:
        greet_window = tk.Toplevel()
        greet_window.title("Welcome")

        greet_label = tk.Label(greet_window, text=f"Hi {username}!")
        greet_label.pack()

        task_manager_button = tk.Button(greet_window, text="Task Manager", command=task_manager)
        task_manager_button.pack()

        greet_window.protocol("WM_DELETE_WINDOW", greet_window.destroy)

    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")


def login():
    global e1, e2  
    root = tk.Tk()
    root.title("Login Page")
    root.geometry("300x150")

    tk.Label(root, text='Username').grid(row=0)
    tk.Label(root, text='Password').grid(row=1)

    e1 = tk.Entry(root)
    e2 = tk.Entry(root, show='*')  
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
    root.geometry("300x150")

    tk.Label(root, text='Username').grid(row=0)
    tk.Label(root, text='Password').grid(row=1)

    e1 = tk.Entry(root)
    e2 = tk.Entry(root, show='*')  
    e1.grid(row=0, column=1, sticky=tk.W)
    e2.grid(row=1, column=1, sticky=tk.W)
    
    button = tk.Button(root, text='Submit', width=25, command=store_credentials)
    button.grid(row=2, columnspan=2)  
    root.mainloop()


def task_manager():
    task_window = tk.Toplevel()
    task_window.title("Task Manager")

    task_listbox = tk.Listbox(task_window)
    task_listbox.pack()

    task_entry = tk.Entry(task_window)
    task_entry.pack()

    add_button = tk.Button(task_window, text="Add Task", command=lambda: add_task(task_listbox, task_entry))
    add_button.pack()

    delete_button = tk.Button(task_window, text="Delete Task", command=lambda: delete_task(task_listbox))
    delete_button.pack()

    update_button = tk.Button(task_window, text="Update Task", command=lambda: update_task(task_listbox, task_entry))
    update_button.pack()



    def add_task(task_listbox, task_entry):
        task = task_entry.get()
        if task:
            task_listbox.insert(tk.END, task)
            task_entry.delete(0, tk.END)
            send_notification("Task Added", f"Task {task} has been added.")
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def delete_task(task_listbox):
        try:
            task_index = task_listbox.curselection()
            task_listbox.delete(task_index)
            send_notification("Task Deleted", "Task has been deleted.")
        except:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def update_task(task_listbox, task_entry):
        try:
            selected_index = task_listbox.curselection()
            if selected_index:
                updated_task = task_entry.get()
                if updated_task:
                    task_listbox.delete(selected_index)
                    task_listbox.insert(selected_index, updated_task)
                    task_entry.delete(0, tk.END)
                    send_notification("Task Updated", "Task has been updated.")
                else:
                    messagebox.showwarning("Input Error", "Please enter an updated task.")
            else:
                messagebox.showwarning("Selection Error", "Please select a task to update.")
        except:
            messagebox.showwarning("Error", "An error occurred while updating the task.")


def main():
    root = tk.Tk()
    root.title("Task Manager")
    root.geometry("300x300")
    login_button = tk.Button(root, text="Login", command=login)
    login_button.pack()

    signup_button = tk.Button(root, text="Signup", command=signup)
    signup_button.pack()
        
    root.mainloop()


if __name__ == "__main__":
   
   main()



