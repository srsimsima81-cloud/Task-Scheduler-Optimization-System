# Scheduling Algorithm

## Objective

Maximize task completion and profit while satisfying deadlines.

## Algorithm Used

Greedy Scheduling Algorithm

## Steps

1. Sort tasks by deadline.
2. Prioritize important tasks.
3. Check if task fits within available time.
4. Add task to schedule if deadline can be met.
5. Otherwise mark task as missed.
6. Calculate total profit.

## Time Complexity

Sorting:
O(n log n)

Scheduling:
O(n)

Overall:
O(n log n)

## Space Complexity

O(n)

## DSA Concepts Used

- Arrays
- Sorting
- Greedy Algorithms
- Priority Queue
- Heap
- Scheduling Optimization