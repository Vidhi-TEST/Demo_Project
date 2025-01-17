# Updated code:

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

# Calculator

# Addition
def add(a, b):
    return a + b

# Subtraction
def subtract(a, b):
    return a - b

# Multiplication
def multiply(a, b):
    return a * b

# Division
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

# Test the calculator functions
print(add(5, 3))
print(subtract(10, 4))
print(multiply(2, 6))
print(divide(8, 2))
print(divide(10, 0))

# Tic-Tac-Toe Game

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
        position = int(input("Enter a position (1-9): ")) - 1

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