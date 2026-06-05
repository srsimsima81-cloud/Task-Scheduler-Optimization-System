import csv
import os


def generate_timeline(tasks):

    timeline = []

    start_time = 0

    for task in tasks:

        end_time = start_time + task.duration

        timeline.append(
            [
                task.name,
                start_time,
                end_time
            ]
        )

        start_time = end_time

    return timeline


def save_schedule_csv(timeline):

    os.makedirs("outputs", exist_ok=True)

    with open(
        "outputs/schedule.csv",
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow(
            ["Task", "Start", "End"]
        )

        writer.writerows(timeline)


def save_report(
    scheduled_tasks,
    missed_tasks,
    total_profit
):

    os.makedirs("outputs", exist_ok=True)

    with open(
        "outputs/report.txt",
        "w"
    ) as file:

        file.write(
            "TASK SCHEDULER REPORT\n"
        )

        file.write(
            "=" * 30 + "\n\n"
        )

        file.write(
            f"Completed Tasks: {len(scheduled_tasks)}\n"
        )

        file.write(
            f"Missed Tasks: {len(missed_tasks)}\n"
        )

        file.write(
            f"Total Profit: {total_profit}\n\n"
        )

        file.write(
            "Completed Task List:\n"
        )

        for task in scheduled_tasks:
            file.write(
                f"- {task.name}\n"
            )

        file.write(
            "\nMissed Task List:\n"
        )

        for task in missed_tasks:
            file.write(
                f"- {task.name}\n"
            )