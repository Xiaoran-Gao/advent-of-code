import numpy as np
from scipy.optimize import linprog

with open("advent-of-code/2025/day10/input.txt", "r") as f:
    input = [list(c.split(' ')) for c in f.read().splitlines()]

n_presses = 0
n_machines = len(input)

for i in range(n_machines):
    joltage = [int(x) for x in input[i][-1].strip("\{\}").split(",")]

    buttons_input = [[int(x) for x in s.strip("()").split(",")] for s in input[i][1:-1]]
    buttons = []
    for b in buttons_input:
        buttons.append([1 if idx in b else 0 for idx in range(len(joltage))])

    c = [1 for _ in range(len(buttons))]
    res = linprog(c=c, A_eq=np.array(buttons).T, b_eq=joltage, integrality=1)
    n_presses += res.fun

print(n_presses)