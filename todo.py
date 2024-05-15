import re

class User:
    def __init__(self, username):
        self.username = username
        self.tasks = []

    def sanitize_input(self, input_string):
        return re.sub(r'[<>]', '', input_string)

    def add_task(self):
        task_name = input("Please enter a task: ")
        task_name = self.sanitize_input(task_name)
        
        priority = input("Enter priority (high, medium, low): ").lower()
        while priority not in ['high', 'medium', 'low']:
            print("Invalid priority. Please enter 'high', 'medium', or 'low'.")
            priority = input("Enter priority (high, medium, low): ").lower()

        task_time = input("Enter the time of task (hrs): ")
        while not task_time.isdigit():
            print("Invalid time. Please enter a numeric value.")
            task_time = input("Enter the time of task (hrs): ")

        self.tasks.append({"name": task_name, "priority": priority, "time": task_time})
        print(f"Task '{task_name}' with priority '{priority}' added to the list.")

    def list_tasks(self):
        if not self.tasks:
            print("There are no tasks currently.")
        else:
            print("Current Tasks:")
            for index, task in enumerate(self.tasks, 1): 
                print(f"Task #{index}: {task['name']} [{task['priority']}] at {task['time']}")

    def delete_task(self):
        if not self.tasks:
            print("There are no tasks to delete.")
            return
        self.list_tasks()
        try:
            index = int(input("Enter the task number to delete: "))
            while index < 1 or index > len(self.tasks):
                print("Invalid task number.")
                index = int(input("Enter the task number to delete: "))
            deleted_task = self.tasks.pop(index - 1)
            print(f"Task #{index} '{deleted_task['name']}' deleted successfully.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")

    def search_task(self):
        search_query = input("Enter search term (supports regex): ")
        try:
            found_tasks = [task for task in self.tasks if re.search(search_query, task['name'], re.IGNORECASE)]
            if found_tasks:
                print("Matching Tasks:")
                for idx, task in enumerate(found_tasks, 1):
                    print(f"{idx}. {task['name']} [{task['priority']}] at {task['time']}")
            else:
                print("No tasks found matching the search term.")
        except re.error:
            print("Invalid regex pattern. Please try again.")

    def sort_tasks_by_priority(self):
        priority_order = {"high": 1, "medium": 2, "low": 3}
        self.tasks.sort(key=lambda task: priority_order.get(task['priority'], 4))
        print("Tasks sorted by priority.")
        self.list_tasks()

    def backup_tasks(self):
        try:
            backup_file = f'{self.username}_backup_todo_data.txt'
            with open(backup_file, 'w') as file:
                for task in self.tasks:
                    file.write(f"{task['name']}|{task['priority']}|{task['time']}\n")
            print(f"Tasks backed up successfully to {backup_file}!")
        except Exception as e:
            print(f"An error occurred while backing up tasks: {e}")

    def restore_tasks(self):
        try:
            backup_file = f'{self.username}_backup_todo_data.txt'
            with open(backup_file, 'r') as file:
                lines = file.readlines()
                self.tasks.clear()
                for line in lines:
                    name, priority, time = line.strip().split('|')
                    self.tasks.append({"name": name, "priority": priority, "time": time})
            print(f"Tasks restored successfully from {backup_file}!")
        except FileNotFoundError:
            print(f"No backup data found for user {self.username}.")
        except Exception as e:
            print(f"An error occurred while restoring tasks: {e}")

    def edit_task(self):
        if not self.tasks:
            print("There are no tasks to edit.")
            return
        self.list_tasks()
        try:
            index = int(input("Enter the task number to edit: ")) - 1
            while index < 0 or index >= len(self.tasks):
                print("Invalid task number.")
                index = int(input("Enter the task number to edit: ")) - 1
            task = self.tasks[index]

            print(f"Editing Task #{index + 1}: {task['name']} [{task['priority']}] at {task['time']}")
            new_name = input(f"Enter new name (leave blank to keep '{task['name']}'): ")
            new_priority = input(f"Enter new priority (high, medium, low) (leave blank to keep '{task['priority']}'): ").lower()
            new_time = input(f"Enter new time (hrs) (leave blank to keep '{task['time']}'): ")

            if new_name:
                task['name'] = self.sanitize_input(new_name)
            if new_priority in ['high', 'medium', 'low']:
                task['priority'] = new_priority
            if new_time.isdigit():
                task['time'] = new_time

            print(f"Task #{index + 1} updated successfully.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")


class TodoApp:
    def __init__(self):
        self.users = {}
        self.current_user = None

    def get_user(self):
        username = input("Enter your username: ")
        username = re.sub(r'[<>]', '', username)
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
            print("8. Edit a task")
            print("9. Switch user")
            print("10. Quit")

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
                self.current_user.edit_task()
            elif choice == "9":
                self.switch_user()
            elif choice == "10":
                break
            else:
                print("Invalid input. Please try again.")

        print("Goodbye 👋👋")


if __name__ == "__main__":
    app = TodoApp()
    app.run()
