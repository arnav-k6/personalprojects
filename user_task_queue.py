import os
import tkinter as tk
from tkinter import messagebox, simpledialog
import re

TASK_FOLDER = "tasks"
os.makedirs(TASK_FOLDER, exist_ok=True)

task_files_list = []

time_pattern = re.compile(r"^(?:[01]\d|2[0-3]):[0-5]\d$")

def add_new_task():
    name = simpledialog.askstring("Task Name", "What's your task?")
    if not name:
        return

    priority_str = simpledialog.askstring("Priority", "Enter task priority (1 = highest)")
    if not priority_str or not priority_str.isdigit():
        messagebox.showerror("Oops!", "Priority must be a number.")
        return

    while True:
        startTime = simpledialog.askstring("Start", "Enter the start time of the activity in hh:mm format")
        if startTime is None: 
            return
        if time_pattern.match(startTime):
            break
        else:
            messagebox.showerror("Invalid Input", "Please enter time in hh:mm format (e.g. 09:30).")

    priority = int(priority_str)
    filename = f"{priority}_{name}.txt"
    path = os.path.join(TASK_FOLDER, filename)

    with open(path, "w") as f:
        f.write(f"Task: {name}\nPriority: {priority}\nStart Time: {startTime}")

    refresh_task_display()


def complete_selected_task():
    selection = task_listbox.curselection()
    if not selection:
        messagebox.showwarning("Nothing selected", "Pick a task first!")
        return

    file_to_remove = task_files_list[selection[0]]
    os.remove(os.path.join(TASK_FOLDER, file_to_remove))
    refresh_task_display()


def refresh_task_display():
    global task_files_list
    task_listbox.delete(0, tk.END)

    task_files_list = os.listdir(TASK_FOLDER)
    task_files_list.sort(key=lambda f: int(f.split("_")[0]))

    for file in task_files_list:
        path = os.path.join(TASK_FOLDER, file)
        priority = file.split("_")[0]
        name = "_".join(file.split("_")[1:]).replace(".txt", "")

        start_time = "??:??"

        try:
            with open(path, "r") as f:
                for line in f:
                    if line.startswith("Start Time:"):
                        start_time = line.strip().split(":", 1)[1].strip()
                        break
        except Exception:
            pass

        task_listbox.insert(tk.END, f"{priority} -> {name} @ {start_time}")

root = tk.Tk()
root.title("My Task Manager")

list_frame = tk.Frame(root)
list_frame.pack(pady=20)

task_listbox = tk.Listbox(list_frame, width=50)
task_listbox.pack(side=tk.LEFT, padx=(0, 10))

scrollbar = tk.Scrollbar(list_frame, orient=tk.VERTICAL, command=task_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox.config(yscrollcommand=scrollbar.set)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add Task", width=15, command=add_new_task).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Complete Task", width=15, command=complete_selected_task).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Refresh List", width=15, command=refresh_task_display).grid(row=0, column=2, padx=5)

refresh_task_display()
root.mainloop()
