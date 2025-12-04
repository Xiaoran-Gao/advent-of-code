from collections import deque

with open("advent-of-code/2025/day4/input.txt", "r") as f:
    lines = f.read().splitlines()

rolls = set()
for r in range(len(lines)):
    for c in range(len(lines[r])):
        if lines[r][c] == '@':
            rolls.add((r, c))

cnt_dict = dict()

for (r, c) in rolls:
    cnt = 0
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            if i == 0 and j == 0:
                continue
            else:
                r1 = r + i
                c1 = c + j
                if (r1, c1) in rolls:
                    cnt += 1
    
    cnt_dict[(r, c)] = cnt

removed = deque([(r, c) for (r, c) in rolls if cnt_dict[(r, c)] < 4])
rmv_ind = {x: 0 for x in rolls}
for (r, c) in removed:
    rmv_ind[(r, c)] = 1
n_removed = len(removed)

while len(removed) > 0:
    r, c = removed.popleft()

    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            if i == 0 and j == 0:
                continue
            else:
                r1 = r + i
                c1 = c + j
                if (r1, c1) in rolls:
                    cnt_dict[(r1, c1)] -= 1
                    if rmv_ind[(r1, c1)] == 0 and cnt_dict[(r1, c1)] < 4:
                        removed.append((r1, c1))
                        rmv_ind[(r1, c1)] = 1
                        n_removed += 1

print(n_removed)