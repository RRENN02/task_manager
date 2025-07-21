import mysql.connector
from task import Task
import configparser


class Database:
    """
    Database class for MySQL task management operations.
    
    Provides CRUD operations with error handling and parameterized queries.
    """
    def __init__(self):
        """
        Initialize database connection with dictionary cursor.
        """
        config = configparser.ConfigParser()
        config.read("config.ini")
        db_config = config["mysql"]

        self.conn = mysql.connector.connect(
            host=db_config.get("host"),
            user=db_config.get("user"),
            password=db_config.get("password"),
            database=db_config.get("database")
        )
        
        """
        If not using config.ini, you can directly specify:
        self.conn = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password",
            database="task_db"
        )
        """
        # Dictionary cursor returns results as dicts instead of tuples
        self.cursor = self.conn.cursor(dictionary=True)

    def insert_task(self, task: Task):
        """
        Insert a new task into the database.
        
        Args:
            task (Task): Task object with task details
            
        Returns:
            int: Auto-generated ID of the new task
        """
        query = "INSERT INTO tasks (title, task_description, due_date, priority, status) VALUES (%s, %s, %s, %s, %s)"
        # Extract values from task object
        values = (
            task.to_dict()["title"],
            task.to_dict()["task_description"],
            task.to_dict()["due_date"],
            task.to_dict()["priority"],
            task.to_dict()["status"]
        )
        self.cursor.execute(query, values)
        self.conn.commit()
        return self.cursor.lastrowid

    def get_tasks(self, filters=None):
        """
        Retrieve tasks from database with optional filtering and sorting.
        
        Args:
            filters (dict, optional): Dictionary of filter criteria where keys are 
                                    column names and values are the filter values
                                    
        Returns:
            list: List of task dictionaries, empty list if error occurs
        """
        try:
            base_query = "SELECT * FROM tasks"
            values = []

            # Dynamic WHERE clause construction based on provided filters
            if filters:
                conditions = []
                for key, value in filters.items():
                    conditions.append(f"{key} = %s")
                    values.append(value)
                where_clause = " WHERE " + " AND ".join(conditions)
                base_query += where_clause

            # Always order by due date for consistent results
            base_query += " ORDER BY due_date ASC"
            self.cursor.execute(base_query, values)
            return self.cursor.fetchall()
        except mysql.connector.Error as e:
            print(f"❌ Error fetching tasks: {e}")
            return []


    def update_task(self, task_id, updates):
        """
        Update specific fields of an existing task.
        
        Args:
            task_id (int): The ID of the task to update
            updates (dict): Dictionary containing field-value pairs to update
            
        Returns:
            int: Number of rows affected (1 if successful, 0 if failed/not found)
        """
        try:
            # Dynamic SET clause construction from updates dictionary
            set_clause = ", ".join(f"{k} = %s" for k in updates)
            # Prepare values list: update values first, then task_id for WHERE clause
            values = list(updates.values()) + [task_id]
            query = f"UPDATE tasks SET {set_clause} WHERE id = %s"
            self.cursor.execute(query, values)
            self.conn.commit()
            return self.cursor.rowcount
        except mysql.connector.Error as e:
            print(f"❌ Database error: {e}")
            return 0

    def delete_task(self, task_id):
        """
        Delete a task from the database.
        
        Args:
            task_id (int): The ID of the task to delete
            
        Returns:
            int: Number of rows affected (1 if successful, 0 if not found)
        """
        self.cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
        self.conn.commit()
        return self.cursor.rowcount
