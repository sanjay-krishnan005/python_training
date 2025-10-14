task = []
def view_tasks():
    print("Tasks:", task)
def add_task(task):
    task.append(task)
    print("Task added:", task)
def delete_task(task):
    if task in task:
        task.delete(task)
        print("Task delete:", task)
    else:
        print("Task not found:", task)
def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Tasks")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")
        if choice == '1':
            task = input("Enter the task to add: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task = input("Enter the task to remove: ")
            delete_task(task)
        elif choice == '4':
            print("Exiting the to-do list application.")
            break
        else:
            print("Invalid choice, please try again.")         
if __name__ == "__main__":
    main()       