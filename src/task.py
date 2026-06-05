class Task:
    def __init__(self, name, priority, deadline, duration, profit):
        self.name = name
        self.priority = int(priority)
        self.deadline = int(deadline)
        self.duration = int(duration)
        self.profit = int(profit)

    def __str__(self):
        return (
            f"{self.name} | "
            f"Priority={self.priority} | "
            f"Deadline={self.deadline} | "
            f"Duration={self.duration} | "
            f"Profit={self.profit}"
        )