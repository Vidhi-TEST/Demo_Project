import unittest

class TicTacToeTest(unittest.TestCase):
    def test_print_board(self):
        # Arrange
        expected_output = " | | \n-----\n | | \n-----\n | | \n"
        
        # Act
        actual_output = print_board()
        
        # Assert
        self.assertEqual(actual_output, expected_output)
    
    def test_check_win(self):
        # Arrange
        player = 'X'
        board = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
        
        # Act
        actual_output = check_win(player, board)
        
        # Assert
        self.assertTrue(actual_output)
    
    def test_play_game(self):
        # Arrange
        expected_output = "X|O|X\n-----\nO|X|O\n-----\nX|O|X\nPlayer X wins!"
        
        # Act
        actual_output = play_game()
        
        # Assert
        self.assertEqual(actual_output, expected_output)

class TodoListTest(unittest.TestCase):
    def test_add_task(self):
        # Arrange
        todo_list = TodoList()
        task = "Buy groceries"
        expected_output = ["Buy groceries"]
        
        # Act
        todo_list.add_task(task)
        actual_output = todo_list.tasks
        
        # Assert
        self.assertEqual(actual_output, expected_output)
    
    def test_remove_task(self):
        # Arrange
        todo_list = TodoList()
        task = "Clean the house"
        expected_output = []
        
        # Act
        todo_list.add_task(task)
        todo_list.remove_task(task)
        actual_output = todo_list.tasks
        
        # Assert
        self.assertEqual(actual_output, expected_output)
    
    def test_print_tasks(self):
        # Arrange
        todo_list = TodoList()
        expected_output = "Buy groceries\nClean the house\nDo laundry\n"
        
        # Act
        todo_list.add_task("Buy groceries")
        todo_list.add_task("Clean the house")
        todo_list.add_task("Do laundry")
        actual_output = todo_list.print_tasks()
        
        # Assert
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()