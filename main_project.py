tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option")