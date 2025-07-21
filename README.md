# Task Manager CLI App

A simple Python-based Task Manager with MySQL integration using OOP.

## Features
- Add, list, update, complete, and delete tasks
- Filtering and sorting tasks (due date, priority, status)
- Data persisted in MySQL
- Modular design following OOP
- Input validation and error handling

## Requirements
- Python 3.12
- mysql-connector-python
- configparser (if using config.ini)

## Setup
1. Clone the repo
2. Create the MySQL DB using `task_db_schema.sql`
3. Fill in your DB credentials in `database.py` or `config.ini`
4. Run app.py to run the task manager app. Enjoy!
