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