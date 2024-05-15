class User:
    def _init_(self, username):
        self.username = username
        self.tasks = []

    def add_task(self):
        task_name = input("Please enter a task: ")
        priority = input("Enter priority (high, medium, low): ").lower()
        task_time = input('Enter the time of task (hrs): ')
        self.tasks.append({"name": task_name, "priority": priority, "time": task_time})
        print(f"Task '{task_name}' with priority '{priority}' added to the list.")

    def list_tasks(self):
        if not self.tasks:
            print("There are no tasks currently.")
        else:
            print("Current Tasks:")
            for index, task in enumerate(self.tasks):
                print(f"Task #{index + 1}: {task['name']} [{task['priority']}] at {task['time']}")

    def delete_task(self):
        if not self.tasks:
            print("There are no tasks to delete.")
            return
        self.list_tasks()
        try:
            index = int(input("Enter the task number to delete: ")) - 1
            if 0 <= index < len(self.tasks):
                deleted_task = self.tasks.pop(index)
                print(f"Task #{index + 1} '{deleted_task['name']}' deleted successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")

    def search_task(self):
        search_query = input("Enter search term: ").lower()
        found_tasks = [task for task in self.tasks if search_query in task['name'].lower()]
        if found_tasks:
            print("Matching Tasks:")
            for idx, task in enumerate(found_tasks, 1):
                print(f"{idx}. {task['name']} [{task['priority']}] at {task['time']}")
        else:
            print("No tasks found matching the search term.")

    def sort_tasks_by_priority(self):
        priority_order = {"high": 1, "medium": 2, "low": 3}
        self.tasks.sort(key=lambda task: priority_order.get(task['priority'], 4))
        print("Tasks sorted by priority.")
        self.list_tasks()

    def backup_tasks(self):
        try:
            with open(f'{self.username}_backup_todo_data.txt', 'w') as file:
                for task in self.tasks:
                    file.write(f"{task['name']}|{task['priority']}|{task['time']}\n")
            print("Tasks backed up successfully!")
        except Exception as e:
            print(f"An error occurred while backing up tasks: {e}")

    def restore_tasks(self):
        try:
            with open(f'{self.username}_backup_todo_data.txt', 'r') as file:
                lines = file.readlines()
                self.tasks.clear()
                for line in lines:
                    name, priority, time = line.strip().split('|')
                    self.tasks.append({"name": name, "priority": priority, "time": time})
            print("Tasks restored successfully!")
        except FileNotFoundError:
            print("No backup data found.")
        except Exception as e:
            print(f"An error occurred while restoring tasks: {e}")


class TodoApp:
    def _init_(self):
        self.users = {}
        self.current_user = None

    def get_user(self):
        username = input("Enter your username: ")
        if username not in self.users:
            self.users[username] = User(username)
        self.current_user = self.users[username]

    def switch_user(self):
        self.current_user = None

    def run(self):
        print("Welcome to the to-do list app :)")
        while True:
            if self.current_user is None:
                self.get_user()
            print(f"\nLogged in as: {self.current_user.username}")
            print("Please select one of the following options")
            print("------------------------------------------")
            print("1. Add a new task")
            print("2. Delete a task")
            print("3. List tasks")
            print("4. Search tasks")
            print("5. Sort tasks by priority")
            print("6. Backup tasks")
            print("7. Restore tasks")
            print("8. Switch user")
            print("9. Quit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.current_user.add_task()
            elif choice == "2":
                self.current_user.delete_task()
            elif choice == "3":
                self.current_user.list_tasks()
            elif choice == "4":
                self.current_user.search_task()
            elif choice == "5":
                self.current_user.sort_tasks_by_priority()
            elif choice == "6":
                self.current_user.backup_tasks()
            elif choice == "7":
                self.current_user.restore_tasks()
            elif choice == "8":
                self.switch_user()
            elif choice == "9":
                break
            else:
                print("Invalid input. Please try again.")

        print("Goodbye 👋👋")


if _name_ == "_main_":
    app = TodoApp()
    app.run()
