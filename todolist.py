from colorama import *
# to-do list v0.1

class Task:
    tasks = {}

    def add_task(self, task_name):
        task_number = len(self.tasks) + 1
        self.tasks[task_number] = task_name

    def delete_task(self, task_number):
        if task_number in self.tasks:
            del self.tasks[task_number]
            print(f"Task {task_number} deleted successfully.")
            self.renumber_tasks()
        else:
            print(f"Task {task_number} not found.")

    def renumber_tasks(self):
        new_tasks = {}
        for index, (old_number, task_name) in enumerate(self.tasks.items(), start=1):
            new_tasks[index] = task_name
        self.tasks = new_tasks

    def see_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task_number, task_name in self.tasks.items():
                print(f"{task_number}. {task_name}")


task_manager = Task()

while True:
    print(Fore.CYAN + "***Main Menu***")
    print(Fore.LIGHTWHITE_EX + "Tasks: ")
    task_manager.see_tasks()
    print(Fore.GREEN + "\n[1] Add a task")
    print(Fore.LIGHTRED_EX + "[2] Delete A Task")
    a = input(Fore.LIGHTWHITE_EX + "Option: ")

    if a == "1":
        task_name = input("Enter Task: ")
        task_manager.add_task(task_name)
    elif a == "2":
        task_number = int(input("Enter task number to delete: "))
        task_manager.delete_task(task_number)
    else:
        print("Invalid option. Please choose again.")
