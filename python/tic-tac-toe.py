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

if __name__ == '__main__':
    unittest.main()