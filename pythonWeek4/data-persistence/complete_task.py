import sqlite3
import sys

def complete_task(task_id):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    conn.commit()
    cursor.close()
    print(f'Task {task_id} now marked complete')

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 complete_task.py <task_id>")
        return
    complete_task(sys.argv[1])

if __name__ == "__main__":
    main()