import sqlite3
import sys

def add_task(description):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (description) VALUES (?)", (description,))
    conn.commit()
    conn.close()
    print(f"Tasks added: {description}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 add_tasks.py <task description>")
        return
    description = " ".join(sys.argv[1:])
    add_task(description)

if __name__ == "__main__":
    main()