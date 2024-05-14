#TO DO APP


tasks = []

def addTask():
    task_name = input("Please enter a task: ")
    priority = input("Enter priority (high, medium, low): ")
    
    tasks.append({"name": task_name, "priority": priority })
    print(f"Task '{task_name}' with priority '{priority}' added to the list.")

def listTasks():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task['name']} [{task['priority']}]")

def deleteTask():
    if not tasks:
        print("There are no tasks to delete.")
        return
    listTasks()
    try:
        index = int(input("Enter the task number to delete: "))
        if 0 <= index < len(tasks):
            deleted_task = tasks.pop(index)
            print(f"Task '{deleted_task['name']}' deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def searchTask():
    search_query = input("Enter search term: ").lower()
    found_tasks = [task for task in tasks if search_query.lower() in task['name'].lower()]
    if found_tasks:
        print("Matching Tasks:")
        for idx, task in enumerate(found_tasks, 1):
            print(f"{idx}. {task['name']} [{task['priority']}]")
    else:
        print("No tasks found matching the search term.")

def backupTasks():
    try:
        with open('backup_todo_data.txt', 'w') as file:
            for task in tasks:
                file.write(f"{task['name']}|{task['priority']}\n")
        print("Tasks backed up successfully!")
    except Exception as e:
        print(f"An error occurred while backing up tasks: {e}")

def restoreTasks():
    try:
        with open('backup_todo_data.txt', 'r') as file:
            lines = file.readlines()
            tasks.clear()
            for line in lines:
                name, priority = line.strip().split('|')
                tasks.append({"name": name, "priority": priority})
        print("Tasks restored successfully!")
    except FileNotFoundError:
        print("No backup data found.")
    except Exception as e:
        print(f"An error occurred while restoring tasks: {e}")

if __name__ == "__main__":
    print("Welcome to the to do list app :)")
    while True:
        print("\n")
        print("Please select one of the following options")
        print("------------------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Search tasks")
        print("5. Backup tasks")
        print("6. Restore tasks")
        print("7. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            addTask()
        elif choice == "2":
            deleteTask()
        elif choice == "3":
            listTasks()
        elif choice == "4":
            searchTask()
        elif choice == "5":
            backupTasks()
        elif choice == "6":
            restoreTasks()
        elif choice == "7":
            break
        else:
            print("Invalid input. Please try again.")

    print("Goodbye 👋👋")
