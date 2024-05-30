# Initialize an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task():
  task = input("Enter a task to add: ")
  tasks.append(task)
  print("Task added successfully!")

# Function to view all tasks
def view_tasks():
  if not tasks:
    print("There are no tasks in the list.")
    return
  print("Your To-Do List:")
  for index, task in enumerate(tasks):
    print(f"{index + 1}. {task}")

# Function to mark a task as done
def mark_done():
  if not tasks:
    print("There are no tasks to mark as done.")
    return
  view_tasks()
  try:
    task_number = int(input("Enter the number of the task you want to mark as done: ")) - 1
    if task_number < 0 or task_number >= len(tasks):
      print("Invalid task number.")
      return
    tasks.pop(task_number)
    print("Task marked as done!")
  except ValueError:
    print("Invalid input. Please enter a number.")

# Main loop to keep the program running
while True:
  print("\nTo-Do List App")
  print("1. Add Task")
  print("2. View Tasks")
  print("3. Mark Task Done")
  print("4. Exit")
  choice = input("Enter your choice: ")

  if choice == '1':
    add_task()
  elif choice == '2':
    view_tasks()
  elif choice == '3':
    mark_done()
  elif choice == '4':
    print("Exiting the To-Do List App.")
    break
  else:
    print("Invalid choice. Please try again.")
