import heapq


def sort_by_deadline(tasks):
    return sorted(tasks, key=lambda task: task.deadline)


def create_profit_heap(tasks):

    heap = []

    for task in tasks:
        heapq.heappush(
            heap,
            (-task.profit, task)
        )

    return heap


def schedule_tasks(tasks):

    tasks = sort_by_deadline(tasks)

    current_time = 0

    scheduled_tasks = []

    missed_tasks = []

    total_profit = 0

    heap = []

    for task in tasks:
        heapq.heappush(
            heap,
            (-task.profit, task)
        )

    while heap:

        _, task = heapq.heappop(heap)

        if current_time + task.duration <= task.deadline:

            scheduled_tasks.append(task)

            current_time += task.duration

            total_profit += task.profit

        else:
            missed_tasks.append(task)

    return (
        scheduled_tasks,
        missed_tasks,
        total_profit
    )