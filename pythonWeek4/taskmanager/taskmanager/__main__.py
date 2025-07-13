import sys
from taskmanager import core

def main():
    core.init_db()

    if len(sys.argv) < 2:
        print("Usage: python3 -m taskmanager <add|list|complete> [args]")
        return
    
    command = sys.argv[1]

    if command == "add":
        description = " ".join(sys.argv[2:])
        core.add_task(description)
        print(f"Added task: {description}")

    elif command == "list":
        tasks = core.list_tasks()
        for task_id, desc, completed in tasks:
            status = "Completed" if completed else "Not Completed"
            print(f"({task_id}) {desc} -- {status}")

    elif command == "complete":
        task_id = sys.argv[2]
        core.complete_task(task_id)
        print(f"Completed task {task_id}")

    else:
        print("Please enter a valid command")

if __name__ == "__main__":
    main()