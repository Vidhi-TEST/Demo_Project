import unittest

class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.todo_list = TodoList()

    def test_add_task(self):
        self.todo_list.add_task("Buy groceries")
        self.assertEqual(self.todo_list.tasks, ["Buy groceries"])

    def test_remove_task(self):
        self.todo_list.add_task("Buy groceries")
        self.todo_list.add_task("Clean the house")
        self.todo_list.add_task("Do laundry")
        self.todo_list.remove_task("Clean the house")
        self.assertEqual(self.todo_list.tasks, ["Buy groceries", "Do laundry"])

    def test_print_tasks(self):
        self.todo_list.add_task("Buy groceries")
        self.todo_list.add_task("Clean the house")
        self.todo_list.add_task("Do laundry")
        expected_output = "Buy groceries\nClean the house\nDo laundry\n"
        self.assertEqual(self.todo_list.print_tasks(), expected_output)

if __name__ == "__main__":
    unittest.main()