import argparse
import json
import logging
import os

TASK_FILE = "tasks.json"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def load_tasks():

    if not os.path.exists(TASK_FILE):
        return []

    with open(TASK_FILE, "r") as f:
        return json.load(f)


def save_tasks(tasks):

    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(task):

    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)

    logging.info("Task added successfully")


def list_tasks():

    tasks = load_tasks()

    if not tasks:
        logging.info("No tasks found")
        return

    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")


def main():

    parser = argparse.ArgumentParser(description="Todo Manager CLI Tool")

    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("task", help="Task description")

    subparsers.add_parser("list", help="List all tasks")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.task)

    elif args.command == "list":
        list_tasks()

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
