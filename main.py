import csv

from src.task import Task
from src.validator import validate_tasks
from src.scheduler import schedule_tasks
from src.report import (
    generate_timeline,
    save_schedule_csv,
    save_report
)


def load_tasks():

    tasks = []

    with open(
        "data/tasks.csv",
        "r"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:

            task = Task(
                row["name"],
                row["priority"],
                row["deadline"],
                row["duration"],
                row["profit"]
            )

            tasks.append(task)

    return tasks


def main():

    print("\nTASK SCHEDULER OPTIMIZATION SYSTEM\n")

    tasks = load_tasks()

    tasks = validate_tasks(tasks)

    print("Loaded Tasks:\n")

    for task in tasks:
        print(task)

    (
        scheduled_tasks,
        missed_tasks,
        total_profit
    ) = schedule_tasks(tasks)

    print("\nOPTIMIZED SCHEDULE\n")

    for task in scheduled_tasks:
        print(task.name)

    print("\nMISSED TASKS\n")

    for task in missed_tasks:
        print(task.name)

    print(
        f"\nTOTAL PROFIT: {total_profit}"
    )

    timeline = generate_timeline(
        scheduled_tasks
    )

    save_schedule_csv(timeline)

    save_report(
        scheduled_tasks,
        missed_tasks,
        total_profit
    )

    print(
        "\nReports saved in outputs folder."
    )


if __name__ == "__main__":
    main()