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
    print("4. Exit")

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
        print("Good bye!")
        break

    else:
        print("Invalid option.")
    










