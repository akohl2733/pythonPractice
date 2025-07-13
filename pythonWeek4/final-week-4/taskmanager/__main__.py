import argparse
import logging
from taskmanager import core, logger

def main():
    logger.setup_logging()
    core.init_db()

    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Add task
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", type=str, help="Task description")

    # List tasks
    subparsers.add_parser("list", help="List all tasks")

    # Complete task
    complete_parser = subparsers.add_parser("complete", help="Complete a task")
    complete_parser.add_argument("task_id", type=int, help="Task ID")

    # Delete task
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("task_id", type=int, help="Task ID")

    args = parser.parse_args()

    if args.command == "add":
        core.add_task(args.description)
        logging.info(f"Added task: {args.description}")

    elif args.command == "list":
        tasks = core.list_tasks()
        if not tasks:
            print("No tasks found")
        else:
            for task_id, desc, completed in tasks:
                status = "Completed" if completed else "Not completed"
                print(f"[{task_id}] - {desc} - {status}")
        logging.info(f"Listed {len(tasks)} tasks.")

    elif args.command == "complete":
        core.complete_task(args.task_id)
        logging.info(f"Completed task ID: {args.task_id}")

    elif args.command == "delete":
        core.delete_task(args.task_id)
        logging.info(f"Deleted task ID: {args.task_id}")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()