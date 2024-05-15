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
        
        if any(task['name'] == task_name for task in self.tasks):
            print("This task already exists.")
            return

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
                status = "Completed" if task['completed'] else "Pending"
                print(f"Task #{index}: {task['name']} [{task['priority']}] at {task['time']} - {status}")

    def mark_or_delete_task(self):
        if not self.tasks:
            print("There are no tasks.")
            return
        self.list_tasks()
        try:
            index = int(input("Enter the task number to mark as completed or delete: "))
            while index < 1 or index > len(self.tasks):
                print("Invalid task number.")
                index = int(input("Enter the task number to mark as completed or delete: "))
            choice = input("Do you want to mark this task as completed (C) or delete it (D)? ").upper()
            if choice == "C":
                self.tasks[index - 1]['completed'] = True
                print(f"Task #{index} marked as completed.")
            elif choice == "D":
                deleted_task = self.tasks.pop(index - 1)
                print(f"Task #{index} '{deleted_task['name']}' deleted successfully.")
            else:
                print("Invalid choice. Please enter 'C' to mark as completed or 'D' to delete.")
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
            print("2. List tasks")
            print("3. Mark a task as completed or delete it")
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
                self.current_user.list_tasks()
            elif choice == "3":
                self.current_user.mark_or_delete_task()
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
