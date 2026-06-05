def validate_tasks(tasks):
    valid_tasks = []

    for task in tasks:
        if (
            task.deadline > 0
            and task.duration > 0
            and task.profit > 0
        ):
            valid_tasks.append(task)

    return valid_tasks