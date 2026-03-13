tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added")


def show_tasks():

    if not tasks:
        print("No tasks")

    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")


while True:

    print("\n1 Add Task")
    print("2 Show Tasks")
    print("3 Exit")

    choice = input("Select: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        break
