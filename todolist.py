tasks = []   
while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Search Task")
    print("6. Exit")
    choice = input("Enter your choice: ")

    
    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added successfully!")

    
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    
    elif choice == "3":
        for i in range(len(tasks)):
            print(i + 1, ".", tasks[i])

        index = int(input("Enter task number to update: ")) - 1

        if 0 <= index < len(tasks):
            new_task = input("Enter new task: ")
            tasks[index] = new_task
            print("Task updated successfully!")
        else:
            print("Invalid task number!")

    
    elif choice == "4":
        for i in range(len(tasks)):
            print(i + 1, ".", tasks[i])

        index = int(input("Enter task number to delete: ")) - 1

        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print("Removed task:", removed)
        else:
            print("Invalid task number!")

    
    elif choice == "5":
        search = input("Enter task to search: ")
        if search in tasks:
            print("Task found!")
        else:
            print("Task not found!")

    
    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")
