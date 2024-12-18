# Student Name: Ricardo Danganan Jnr
# Student ID: X00191395
# Student Email: x00191395@mytudublin.ie
# Module: DevOps - Continuous Integration and Deployment
# Lecturer Name: Damian Niezgoda
# Created on: 19/11/2024
# Submitted on: 20/11/2024

# This is a simple to-do list application that allows users to add tasks, view tasks, mark tasks as complete or incomplete, and delete tasks.

# list to store tasks in the to-do list application 
tasks = []

# functions to interact with the to-do list application 
def add_task(task):
    tasks.append({'task': task, 'completed': False})
    print(f'Task "{task}" added successfully.')

# function to view all tasks in the to-do list application
def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for index, task in enumerate(tasks, start=1):
            status = "Completed" if task['completed'] else "Incomplete"
            print(f'{index}. {task["task"]} - {status}')

# functions to mark tasks as complete or incomplete
def mark_task(index, completed=True):
    if 0 <= index < len(tasks):
        tasks[index]['completed'] = completed
        status = "completed" if completed else "incomplete"
        print(f'Task "{tasks[index]["task"]}" marked as {status}.')
    else:
        print("Invalid task index.")

# function to delete a task
def delete_task(index):
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        print(f'Task "{removed_task["task"]}" deleted successfully.')
    else:
        print("Invalid task index.")

# menu to interact with the to-do list application
def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Mark Task as Complete")
        print("4. Mark Task as Incomplete")
        print("5. Delete Task")
        print("6. Exit")
        
        # get user choice
        choice = input("Choose an option: ")

        # perform action based on user choice
        if choice == "1":
            task = input("Enter the task description: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            index = int(input("Enter the task number to mark as complete: ")) - 1
            mark_task(index, True)
        elif choice == "4":
            index = int(input("Enter the task number to mark as incomplete: ")) - 1
            mark_task(index, False)
        elif choice == "5":
            index = int(input("Enter the task number to delete: ")) - 1
            delete_task(index)
        elif choice == "6":
            print("Exiting the To-Do List Application.")
            break
        else:
            print("Invalid choice. Please try again.")

# run the to-do list application
if __name__ == "__main__":
    main()
