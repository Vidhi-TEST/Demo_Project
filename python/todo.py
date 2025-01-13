import unittest

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
class TodoListTestCase(unittest.TestCase):
    def setUp(self):
        self.todo_list = TodoList()

    def test_add_task(self):
        self.todo_list.add_task("Buy groceries")
        self.assertEqual(self.todo_list.tasks, ["Buy groceries"])

    def test_remove_task(self):
        self.todo_list.add_task("Buy groceries")
        self.todo_list.add_task("Clean the house")
        self.todo_list.remove_task("Clean the house")
        self.assertEqual(self.todo_list.tasks, ["Buy groceries"])

    def test_print_tasks(self):
        self.todo_list.add_task("Buy groceries")
        self.todo_list.add_task("Clean the house")
        self.todo_list.add_task("Do laundry")
        expected_output = "Buy groceries\nClean the house\nDo laundry\n"
        with captured_output() as (out, err):
            self.todo_list.print_tasks()
        self.assertEqual(out.getvalue(), expected_output)

if __name__ == "__main__":
    unittest.main()