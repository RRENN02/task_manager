from database import Database
from task import Task


class TaskManager:
    """
    Task Manager class that provides high-level operations for task management.
    
    Acts as a service layer between the CLI application and the database,
    providing business logic for task operations including CRUD operations
    and task status management.
    """
    
    def __init__(self):
        """Initialize TaskManager with database connection."""
        self.db = Database()

    def add_task(self, task: Task):
        return self.db.insert_task(task)

    def list_tasks(self, filters=None):
        return self.db.get_tasks(filters)

    def update_task(self, task_id, updates: dict):
        return self.db.update_task(task_id, updates)

    def complete_task(self, task_id):
        return self.db.update_task(task_id, {"status": "Completed"})

    def delete_task(self, task_id):
        return self.db.delete_task(task_id)
