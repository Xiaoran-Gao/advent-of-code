with open("advent-of-code/2025/day4/input.txt", "r") as f:
    lines = f.read().splitlines()

rolls = set()
for r in range(len(lines)):
    for c in range(len(lines[r])):
        if lines[r][c] == '@':
            rolls.add((r, c))

n = 0

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

    if cnt < 4:
        n += 1

print(n)