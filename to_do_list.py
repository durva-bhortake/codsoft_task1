#command line based to do list
todo_list = []
def show_menu():
    print("\n=== To-Do List Manager ===")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Clear All Tasks")
    print("6. Exit")

def add_task():
    task = input("Enter a new task: ").strip()
    if not task:
        print("Error: Task cannot be empty!")
        return
    todo_list.append({"task": task, "done": False, "created_at": time.ctime()})
    print(f"Task '{task}' added successfully!")

def view_tasks():
    if not todo_list:
        print("No tasks in the list.")
        return
    print("\n=== Your Tasks ===")
    for index, task in enumerate(todo_list, 1):
        status = "✔️ Done" if task["done"] else "❌ Pending"
        print(f"{index}. {task['task']} [{status}] (Added: {task['created_at']})")

def mark_done():
    if not todo_list:
        print("No tasks to mark as completed.")
        return
    view_tasks()
    try:
        task_num = int(input("Enter task number to mark as completed: "))
        if 1 <= task_num <= len(todo_list):
            if todo_list[task_num - 1]["done"]:
                print("Task is already marked as completed!")
            else:
                todo_list[task_num - 1]["done"] = True
                print(f"Task '{todo_list[task_num - 1]['task']}' marked as completed.")
        else:
            print(f"Error: Task number must be between 1 and {len(todo_list)}!")
    except ValueError:
        print("Error: Please enter a valid number!")

def delete_task():
    if not todo_list:
        print("No tasks to delete.")
        return
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(todo_list):
            removed = todo_list.pop(task_num - 1)
            print(f"Task '{removed['task']}' deleted successfully.")
        else:
            print(f"Error: Task number must be between 1 and {len(todo_list)}!")
    except ValueError:
        print("Error: Please enter a valid number!")

def clear_all_tasks():
    if not todo_list:
        print("No tasks to clear.")
        return
    confirm = input("Are you sure you want to delete all tasks? (y/n): ").lower()
    if confirm == 'y':
        todo_list.clear()
        print("All tasks deleted successfully.")
    else:
        print("Operation cancelled.")

def save_tasks():
    with open("todo_list.txt", "w") as file:
        for task in todo_list:
            file.write(f"{task['task']}|{task['done']}|{task['created_at']}\n")
    print("Tasks saved to file.")

def load_tasks():
    try:
        with open("todo_list.txt", "r") as file:
            for line in file:
                task, done, created_at = line.strip().split("|")
                todo_list.append({"task": task, "done": done == "True", "created_at": created_at})
        print("Tasks loaded from file.")
    except FileNotFoundError:
        print("No saved tasks found.")

import time
import os

# Load tasks at startup
if os.path.exists("todo_list.txt"):
    load_tasks()

while True:
    show_menu()
    choice = input("Choose an option (1-6): ").strip()
    if choice == '1':
        add_task()
        save_tasks()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_done()
        save_tasks()
    elif choice == '4':
        delete_task()
        save_tasks()
    elif choice == '5':
        clear_all_tasks()
        save_tasks()
    elif choice == '6':
        print("Thank you for using To-Do List Manager! Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1-6.")