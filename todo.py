def delete_task(tasks):
    tasks = get_tasks()
    if task_id >= 0 and task_id < len(tasks):
        deleted_task = tasks.pop(task_id)
        save_tasks(tasks)
        print(f"Task '{deleted_task}' deleted successfully.")
    else:
        print("Invalid task ID.")
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        file.writelines(task + "\n" for task in tasks)
def main():
    tasks = load_tasks()
    while True:
        print("\nTODO App")
        print("1. Create Task")
        print("2. List Tasks")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Search Task")
        print("6. Backup Tasks")
        print("7. Restore Tasks")
        print("8. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            create_task(tasks)
        elif choice == '2':
            list_tasks(tasks)
        elif choice == '3':
            edit_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            search_task(tasks)
        elif choice == '6':
            backup_tasks()
        elif choice == '7':
            restore_tasks()
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
