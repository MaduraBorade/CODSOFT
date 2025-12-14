tasks = []

def add_task():
    task = input("\nENTER NEW TASK: ")
    tasks.append(task)
    print("Task added successfully!!!")
    input("Press Enter to return to menu........")

def view_tasks():
    print("\nYOUR TO-DO LIST:")
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    input("\nPress Enter to return to menu...")

def update_task():
    view_tasks()
    if not tasks:
        return

    try:
        task_no = int(input("\nEnter task number to update: "))
        if 1 <= task_no <= len(tasks):
            new_task = input("Enter updated task: ")
            tasks[task_no - 1] = new_task
            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

    input("Press Enter to return to menu...")

def delete_task():
    view_tasks()
    if not tasks:
        return

    try:
        task_no = int(input("\nEnter task number to delete: "))
        if 1 <= task_no <= len(tasks):
            tasks.pop(task_no - 1)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

    input("Press Enter to return to menu...")

def menu():
    while True:
        print("\n=============== TO-DO LIST MENU =============")
        print("1. ADD TASK HERE")
        print("2. VIEW TASK HERE")
        print("3. UPDATE TASK HERE")
        print("4. DELETE TASK HERE")
        print("5. EXIT HERE")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("\nThank you for using To-Do List App!")
            break
        else:
            print("Invalid choice! Please try again.")

menu()
