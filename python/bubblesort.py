# Bubble Sort implementation in Python

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Create an empty board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board():
    row1 = '|'.join(board[0:3])
    row2 = '|'.join(board[3:6])
    row3 = '|'.join(board[6:9])
    print(row1)
    print('-' * 5)
    print(row2)
    print('-' * 5)
    print(row3)

# Function to check if a player has won
def check_win(player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True

    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True

    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True

    return False

# Function to play the game
def play_game():
    current_player = 'X'
    game_over = False

    while not game_over:
        print_board()
        position = int(input("Enter a position(1-9): ")) - 1

        if board[position] == ' ':
            board[position] = current_player

            if check_win(current_player):
                print_board()
                print(f"Player {current_player} wins!")
                game_over = True
            elif ' ' not in board:
                print_board()
                print("It's a tie!")
                game_over = True
            else:
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("That position is already taken. Try again.")

# Start the game
play_game()

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