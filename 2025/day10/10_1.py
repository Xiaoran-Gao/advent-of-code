from collections import deque

with open("advent-of-code/2025/day10/input.txt", "r") as f:
    input = [list(c.split(' ')) for c in f.read().splitlines()]

n_presses = 0
n_machines = len(input)

for i in range(n_machines):
    goal_input = input[i][0].strip("[]")
    goal = [1 if s == '#' else 0 for s in goal_input]
    init = [0 for _ in range(len(goal))]

    buttons_input = [[int(x) for x in s.strip("()").split(",")] for s in input[i][1:-1]]
    buttons = []
    for b in buttons_input:
        buttons.append([1 if idx in b else 0 for idx in range(len(goal))])

    # Do BFS
    queue = deque([(init, 0)])
    visited = {tuple(init)}

    while len(queue) > 0:
        curr_status, curr_depth = queue.popleft()
        if curr_status == goal:
            break
        
        for b in buttons:
            next_status = [a ^ b for (a, b) in zip(curr_status, b)]
            if tuple(next_status) not in visited:
                visited.add(tuple(next_status))
                queue.append((next_status, curr_depth + 1))
    
    n_presses += curr_depth

print(n_presses)