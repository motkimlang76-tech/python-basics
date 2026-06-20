import json 

FILE_NAME = "tasks.json"

def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return[]
    except json.JSONecodeError:
        return[]

def save_tasks(tasks):
        with open(FILE_NAME, "w") as file:
            json.dump(tasks, file, indent=2)

def show_menu():
    print("\nTo_Do App")
    print("1. Add task")
    print("2. Show tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Edit task")
    print("6. Exit")

def add_task(tasks):
    title = input("Enter your task: "). strip()
    if not title:
        print("Task title cannot be empty.")
        return

    task = {"title": title, "done": False}
    tasks.append(task)
    save_tasks(tasks)

def show_tasks(tasks):
    if not tasks:
        print("No task yet!")
    else:
        print("\nYour tasks: ")
        for index, task in enumerate(tasks, start=1):
            status = "Done" if task["done"] else "Not done"
            print(f"{index}. {task['title']} [{status}]")
def mark_task_done(tasks):
    if not tasks:
        print("No task to uptade.")
        return
    show_tasks(tasks)

    try:
        number = int(input("Enter task number to mark as done: "))

        if number < 1 or number > len(tasks):
            print("Invalid task number.")
            return

        tasks[number - 1]["done"] = True
        save_tasks(tasks)
        print("Task updated and saved.")

    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        return

    show_tasks(tasks)

    try:
        number = int(input("Enter task number to delete: "))

        if number < 1 or number > len(tasks):
            print("Invalid task number.")
            return

        deleted_task = tasks[number - 1]
        del tasks[number - 1]
        save_tasks(tasks)
        print(f"Deleted task: {deleted_task['title']}")

    except ValueError:
        print("Please enter a valid number.") 
def edit_task(tasks):
    if not tasks:
        print("No task to edit.")
        return
    
    show_tasks(tasks)

    try:
        number = int(input("Enter task number to edit: "))
        if number < 1 or number > len(tasks):
            print("Invalid task number.")
            return

        new_title = input("Enter new task title: ").strip()
        if not new_title:
            print("Task title cannot be empty.")
            return

        tasks[number - 1]["title"] = new_title
        save_tasks(tasks)
        print("Task updated and saved.")

    except ValueError:
        print("Please enter a valid number.")


tasks = load_tasks()

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        show_tasks(tasks)
    elif choice == "3":
        mark_task_done(tasks)
    elif choice == "4":
        delete_task(tasks)
    elif choice == "5":
        edit_task(tasks)
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")
        









