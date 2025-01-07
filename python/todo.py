# Todo List

# Create an empty list to store the tasks
tasks = []

# Function to add a task to the list
def add_task(task):
    tasks.append(task)

# Function to remove a task from the list
def remove_task(task):
    tasks.remove(task)

# Function to print all tasks in the list
def print_tasks():
    for task in tasks:
        print(task)

# Test the functions
add_task("Buy groceries")
add_task("Clean the house")
add_task("Do laundry")
print_tasks()
remove_task("Clean the house")
print_tasks()