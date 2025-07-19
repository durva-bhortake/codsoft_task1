import tkinter as tk
from tkinter import messagebox

# Main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("420x500")
root.configure(bg="light yellow")  # Main background

tasks = []

# FUNCTIONS
def update_listbox():
    listbox.delete(0, tk.END)
    for index, task in enumerate(tasks, start=1):
        listbox.insert(tk.END, f"{index}. {task}")

def add_task():
    task = entry.get().strip()
    if task:
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("⚠️ Empty Task", "Please enter a task.")

def delete_task():
    try:
        index = listbox.curselection()[0]
        task = tasks.pop(index)
        update_listbox()
        messagebox.showinfo("🗑️ Deleted", f"Task '{task}' removed.")
    except IndexError:
        messagebox.showwarning("⚠️ No Selection", "Please select a task to delete.")

def clear_all():
    if tasks:
        confirm = messagebox.askyesno("🧹 Clear All", "Are you sure you want to delete all tasks?")
        if confirm:
            tasks.clear()
            update_listbox()
    else:
        messagebox.showinfo("ℹ️ No Tasks", "There are no tasks to clear.")

# UI ELEMENTS
title = tk.Label(root, text="📝 TO-DO LIST", font=("Helvetica", 18, "bold"), bg="light yellow", fg="dark green")
title.pack(pady=15)

entry = tk.Entry(root, width=30, font=("Arial", 13), bg="white")
entry.pack(pady=10)

btn_frame = tk.Frame(root, bg="light yellow")
btn_frame.pack(pady=5)

# Button styles
button_style = {
    "font": ("Arial", 10, "bold"),
    "bg": "medium sea green",
    "fg": "white",
    "activebackground": "green",
    "activeforeground": "white",
    "bd": 0,
    "width": 12,
    "cursor": "hand2"
}

tk.Button(btn_frame, text="Add Task", command=add_task, **button_style).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Delete Task", command=delete_task, **button_style).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Clear All", command=clear_all, **button_style).grid(row=0, column=2, padx=5)

listbox = tk.Listbox(
    root,
    width=45,
    height=12,
    font=("Arial", 12),
    bg="honeydew",
    fg="black",
    selectbackground="light coral",
    selectforeground="black"
)
listbox.pack(pady=20)

root.mainloop()
