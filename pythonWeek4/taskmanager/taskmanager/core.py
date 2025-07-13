import sqlite3

DB_NAME = "tasks.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            completed BOOLEAN NOT NULL DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def add_task(description):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (description) VALUES (?)', (description,))
    conn.commit()
    conn.close()

def list_tasks():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT id, description, completed FROM tasks')
    return cursor.fetchall()

def complete_task(task_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET completed = 1 WHERE id = (?)', (task_id,))
    conn.commit()
    conn.close()