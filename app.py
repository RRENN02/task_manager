from manager import TaskManager
from task import Task
from utils import validate_date, get_input, print_task, pause


def main():
    """
    Main function that runs the Task Manager CLI application.
    
    Provides a command-line interface for managing tasks with options to:
    - Add new tasks
    - List tasks with optional filtering
    - Update existing tasks
    - Mark tasks as completed
    - Delete tasks
    """
    manager = TaskManager()

    while True:
        print("\nTask Manager CLI")
        print("[1] Add Task\n[2] List Tasks\n[3] Update Task\n[4] Complete Task\n[5] Delete Task\n[0] Exit")
        choice = input("Select option: ")

        if choice == "1":
            title = get_input("Title: ")
            desc = input("Description: ")
            due = validate_date("Due Date (YYYY-MM-DD): ")
            priority = get_input("Priority (Low/Medium/High): ", ["Low", "Medium", "High"])
            task = Task(title, desc, due, priority)
            task_id = manager.add_task(task)
            print(f"Task added with ID: {task_id}")

        elif choice == "2":
            # Task listing with optional filtering functionality
            print("\n-- Filter Tasks --")
            print("[1] No Filter")
            print("[2] Filter by Due Date")
            print("[3] Filter by Priority")
            print("[4] Filter by Status")
            filter_choice = input("Choose filter: ")

            # Build filter dictionary based on user selection
            filters = {}

            if filter_choice == "2":
                filters["due_date"] = validate_date("Enter Due Date (YYYY-MM-DD): ")
            elif filter_choice == "3":
                filters["priority"] = get_input("Priority (Low/Medium/High): ", ["Low", "Medium", "High"])
            elif filter_choice == "4":
                filters["status"] = get_input("Status (Pending/In Progress/Completed): ", ["Pending", "In Progress", "Completed"])

            # Retrieve and display filtered tasks
            tasks = manager.list_tasks(filters)

            if tasks:
                for task in tasks:
                    print_task(task)
            else:
                print("📭 No tasks found.")
            pause()


        elif choice == "3":
            # Task update functionality with field-specific validation
            task_id = int(input("Task ID to update: "))
            field = input("Field to update (title/task_description/due_date/priority/status): ").strip()

            # Apply field-specific validation for different update types
            if field == "due_date":
                value = validate_date("New Due Date (YYYY-MM-DD): ")
            elif field == "priority":
                value = get_input("New Priority (Low/Medium/High): ", ["Low", "Medium", "High"])
            elif field == "status":
                value = get_input("New Status (Pending/In Progress/Completed): ", ["Pending", "In Progress", "Completed"])
            else:
                # For title and task_description fields, simple text input
                value = input("New value: ").strip()
            
            manager.update_task(task_id, {field: value})
            print("Task updated.")

        elif choice == "4":
            task_id = int(input("Task ID to mark as completed: "))
            manager.complete_task(task_id)
            print("Task completed.")

        elif choice == "5":
            task_id = int(input("Task ID to delete: "))
            manager.delete_task(task_id)
            print("Task deleted.")

        elif choice == "0":
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
