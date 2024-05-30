import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x650+400+100")
root.resizable(False, False)

task_List = []
completed_tasks = []

update_window = None  # Variable to store the update window
update_entry = None  # Variable to store the update entry widget


def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)
    if task:
        with open("tasklist.txt", "a") as taskfile:
            taskfile.write(f"\n{task}")
        task_List.append(task)
        listbox.insert(tk.END, task)


def deleteTask():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        selected_task_index = int(selected_task_index[0])
        task = listbox.get(selected_task_index)

        if task in task_List:
            task_List.remove(task)
            with open("tasklist.txt", "w") as taskfile:
                for t in task_List:
                    taskfile.write(t + "\n")
            listbox.delete(selected_task_index)


def updateTask():
    global update_window, update_entry
    selected_task_index = listbox.curselection()
    if selected_task_index:
        selected_task_index = int(selected_task_index[0])
        task = listbox.get(selected_task_index)

        # Create a new window for updating the task
        update_window = tk.Toplevel(root)
        update_window.title("Update Task")

        # Entry widget for updating the task
        update_entry = tk.Entry(update_window, width=30, font="arial 12", bd=5)
        update_entry.insert(0, task)
        update_entry.pack(pady=10)

        # Button to perform the update
        update_button = tk.Button(update_window, text="Update", font="arial 12 bold", command=perform_update)
        update_button.pack()

def perform_update():
    global update_window, update_entry
    selected_task_indices = listbox.curselection()
    if selected_task_indices:
        updated_task = update_entry.get()
        for index in selected_task_indices:
            if updated_task:
                task_List[index] = updated_task
                listbox.delete(index)
                listbox.insert(index, updated_task)
        update_window.destroy()


def markAsCompleted():
    selected_task_indices = listbox.curselection()
    if selected_task_indices:
        for index in selected_task_indices:
            task = listbox.get(index)
            if task not in completed_tasks:
                updated_task = task + " (Completed)"
                task_List[index] = updated_task
                completed_tasks.append(updated_task)
                listbox.delete(index)
                listbox.insert(index, updated_task)
                with open("tasklist.txt", "w") as taskfile:
                    for t in task_List:
                        taskfile.write(t + "\n")
                break  # Stop after marking the first task as completed
            else:
                completed_tasks.remove(task)
                listbox.delete(index)


def openTaskFile():
    try:
        global task_List
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            task = task.strip()  # Remove leading and trailing whitespaces, including newline characters
            if task:
                task_List.append(task)
                listbox.insert(tk.END, task)

    except FileNotFoundError:
        file = open("tasklist.txt", "w")
        file.close()

# ICON
Image_icon = PhotoImage(file="Images/To-Do-List1.png")
root.iconphoto(False, Image_icon)

# TOP BAR
Top_Image = PhotoImage(file="Images/Topbar2.png")
tk.Label(root, image=Top_Image).pack()

dock_Image = PhotoImage(file="Images/Logodus1.png")
tk.Label(root, image=dock_Image, bg="#02605B").place(x=30, y=25)

note_Image = PhotoImage(file="Images/To-Do-List1.png")
tk.Label(root, image=note_Image, bg="#015A54").place(x=340, y=25)

heading = tk.Label(root, text="TASKS", font="arial 20 bold", fg="white", bg="#016A65")
heading.place(x=155, y=25)

# MAIN
frame = tk.Frame(root, width=400, height=50, bg="white")
frame.place(x=0, y=180)

task = tk.StringVar()
task_entry = tk.Entry(frame, width=18, font="arial 20", bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()

# Buttons for Add, Delete, Update
add_button = tk.Button(frame, text="Add", font="arial 20 bold", width=6, bg="#5a95ff", fg="#fff", bd=0, command=addTask)
add_button.place(x=300, y=0)

delete_button = tk.Button(root, text="Delete", font="arial 12", command=deleteTask)
delete_button.pack(side=tk.BOTTOM, pady=5)

update_button = tk.Button(root, text="Update", font="arial 12", command=updateTask)
update_button.pack(side=tk.BOTTOM, pady=5)

complete_button = tk.Button(root, text="Mark as Completed", font="arial 12", command=markAsCompleted)
complete_button.pack(side=tk.BOTTOM, pady=5)

# LISTBOX
frame1 = tk.Frame(root, bd=3, width=700, height=280, bg="#32485b")
frame1.pack(pady=(160, 0))

listbox = tk.Listbox(frame1, font=("arial", 12), width=40, height=16, bg="#32405b", fg="white", cursor="hand2",
                     selectbackground="#5a95ff")
listbox.pack(side=tk.LEFT, fill=tk.BOTH, padx=2)
scrollbar = tk.Scrollbar(frame1)

openTaskFile()  # Load tasks from file upon startup

root.mainloop()
