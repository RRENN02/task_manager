class Task:
    def __init__(self, title, task_description, due_date, priority, status="Pending", task_id=None, created_at=None):
        self.__id = task_id
        self.__title = title
        self.__task_description = task_description
        self.__due_date = due_date
        self.__priority = priority
        self.__status = status
        self.__created_at = created_at

    def to_dict(self):
        return {
            "id": self.__id,
            "title": self.__title,
            "task_description": self.__task_description,
            "due_date": self.__due_date,
            "priority": self.__priority,
            "status": self.__status,
            "created_at": self.__created_at,
        }


    def __str__(self):
        return f"[{self.__id}] {self.__title} - {self.__status} ({self.__priority})"
class Task:
    def __init__(self, title, task_description, due_date, priority, status="Pending", task_id=None, created_at=None):
        self.__id = task_id
        self.__title = title
        self.__task_description = task_description
        self.__due_date = due_date
        self.__priority = priority
        self.__status = status
        self.__created_at = created_at

    def to_dict(self):
        return {
            "id": self.__id,
            "title": self.__title,
            "description": self.__task_description,
            "due_date": self.__due_date,
            "priority": self.__priority,
            "status": self.__status,
            "created_at": self.__created_at,
        }

    def __str__(self):
        return f"[{self.__id}] {self.__title} - {self.__status} ({self.__priority})"
class Task:
    def __init__(self, title, task_description, due_date, priority, status="Pending", task_id=None, created_at=None):
        self.__id = task_id
        self.__title = title
        self.__task_description = task_description
        self.__due_date = due_date
        self.__priority = priority
        self.__status = status
        self.__created_at = created_at

    def to_dict(self):
        return {
            "id": self.__id,
            "title": self.__title,
            "task_description": self.__task_description,
            "due_date": self.__due_date,
            "priority": self.__priority,
            "status": self.__status,
            "created_at": self.__created_at,
        }

    def __str__(self):
        return f"[{self.__id}] {self.__title} - {self.__status} ({self.__priority})"

