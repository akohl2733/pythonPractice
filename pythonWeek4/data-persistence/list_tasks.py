import sqlite3

def list_tasks():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, description, completed FROM tasks")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("No tasks found")
        return

    for task_id, desc, completed in rows:
        status = "Completed" if completed else "Not Completed"
        print(f"[{task_id}] {desc} -- {status}")

if __name__ == "__main__":
    list_tasks()