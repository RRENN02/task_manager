from datetime import datetime

def validate_date(prompt="Enter date (YYYY-MM-DD): "):
    """
    Keep prompting the user until a valid YYYY-MM-DD date is entered.
    Returns the valid date string.
    """
    while True:
        date_str = input(prompt).strip()
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print("❌ Invalid date format. Please use YYYY-MM-DD.")

def get_input(prompt, allowed_values=None):
    """
    Prompts the user for input. If allowed_values is given, it validates the response.
    """
    while True:
        value = input(prompt).strip()
        if allowed_values:
            if value in allowed_values:
                return value
            else:
                print(f"❌ Invalid input. Allowed values: {', '.join(allowed_values)}")
        else:
            if value:
                return value
            else:
                print("❌ Input cannot be empty.")

def print_task(task_dict):
    """
    Prints task in a user-friendly format.
    """
    print(f"""
🆔 ID: {task_dict['id']}
📝 Title: {task_dict['title']}
📄 Description: {task_dict['task_description']}
📅 Due Date: {task_dict['due_date']}
⭐ Priority: {task_dict['priority']}
📌 Status: {task_dict['status']}
🕓 Created At: {task_dict['created_at']}
""")

def pause():
    input("Press Enter to continue...")