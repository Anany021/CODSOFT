import json
def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)
def add_task(tasks):
    task_name = input("Enter task name: ")
    due_date = input("Enter due date: ")
    priority = input("Enter priority (low, medium, high): ")

    tasks.append({
        "name": task_name,
        "due_date": due_date,
        "priority": priority,
        "completed": False
    })
    save_tasks(tasks)
    print("Task added successfully!")
def view_tasks(tasks):
    print("\nTasks:")
    for idx, task in enumerate(tasks):
        status = "Done" if task["completed"] else "Pending"
        print(f"{idx + 1}. {task['name']} - Due: {task['due_date']} - Priority: {task['priority']} - Status: {status}")
    print()
def mark_completed(tasks):
    view_tasks(tasks)
    task_idx = int(input("Enter the index of the task you want to mark as completed: ")) - 1
    if 0 <= task_idx < len(tasks):
        tasks[task_idx]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed!")
    else:
        print("Invalid task index.")
def main():
    tasks = load_tasks()

    while True:
        print("To-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
