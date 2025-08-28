import csv

FILE = "tasks.csv"

def add_task(task):
    with open(FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([task, "Pending"])

def view_tasks():
    try:
        with open(FILE, "r") as file:
            reader = csv.reader(file)
            print("\n📋 To-Do List:")
            for i, row in enumerate(reader, start=1):
                print(f"{i}. {row[0]} - {row[1]}")
    except FileNotFoundError:
        print("\nNo tasks found.")

def mark_complete(task_number):
    tasks = []
    with open(FILE, "r") as file:
        tasks = list(csv.reader(file))
    if 0 < task_number <= len(tasks):
        tasks[task_number-1][1] = "Completed"
        with open(FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(tasks)

def delete_task(task_number):
    tasks = []
    with open(FILE, "r") as file:
        tasks = list(csv.reader(file))
    if 0 < task_number <= len(tasks):
        tasks.pop(task_number-1)
        with open(FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(tasks)

while True:
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        view_tasks()
        num = int(input("Enter task number to mark complete: "))
        mark_complete(num)
    elif choice == "4":
        view_tasks()
        num = int(input("Enter task number to delete: "))
        delete_task(num)
    elif choice == "5":
        break
    else:
        print("Invalid choice, try again.")
