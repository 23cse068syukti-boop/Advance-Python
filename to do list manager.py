tasks = []

while True:
    print("\n---- To-Do List Menu ----")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    # Add Task
    if choice == "1":
        name = input("Enter task name: ")
        category = input("Enter category: ")
        priority = input("Enter priority (High/Low): ")

        task = {
            "task": name,
            "category": category,
            "priority": priority
        }

        tasks.append(task)
        print("Task added successfully!")

    # Show Tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(tasks, 1):
                print(i, "-", t["task"], "|", t["category"], "|", t["priority"])

    # Delete Task
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                tasks.pop(num - 1)
                print("Task deleted.")
            else:
                print("Invalid task number.")

    # Exit
    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please enter 1-4.")