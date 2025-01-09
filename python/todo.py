# Refactored Todo List

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def print_tasks(self):
        for task in self.tasks:
            print(task)

# Test the TodoList class
todo_list = TodoList()
todo_list.add_task("Buy groceries")
todo_list.add_task("Clean the house")
todo_list.add_task("Do laundry")
todo_list.print_tasks()
todo_list.remove_task("Clean the house")
todo_list.print_tasks()