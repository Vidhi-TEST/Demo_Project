import unittest

class TodoListTest(unittest.TestCase):
    def test_add_task(self):
        todo_list = TodoList()
        todo_list.add_task("Buy groceries")
        self.assertEqual(todo_list.tasks, ["Buy groceries"])

    def test_remove_task(self):
        todo_list = TodoList()
        todo_list.add_task("Buy groceries")
        todo_list.add_task("Clean the house")
        todo_list.remove_task("Clean the house")
        self.assertEqual(todo_list.tasks, ["Buy groceries"])

    def test_print_tasks(self):
        todo_list = TodoList()
        todo_list.add_task("Buy groceries")
        todo_list.add_task("Clean the house")
        todo_list.add_task("Do laundry")
        self.assertEqual(todo_list.print_tasks(), None)

class CalculatorTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 3), 8)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_multiply(self):
        self.assertEqual(multiply(2, 6), 12)

    def test_divide(self):
        self.assertEqual(divide(8, 2), 4)
        self.assertEqual(divide(10, 0), "Error: Division by zero")

class TicTacToeTest(unittest.TestCase):
    def test_check_win(self):
        board = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
        self.assertEqual(check_win('X'), True)
        self.assertEqual(check_win('O'), False)

    def test_play_game(self):
        # TODO: Implement test for play_game function
        pass

if __name__ == '__main__':
    unittest.main()