with open("advent-of-code/2025/day1/input.txt", "r") as f:
    lines = f.read().splitlines()

dial = 50
pwd = 0

for l in lines:
    x = int(l[1:])
    if l[0] == "L":
        if dial - x <= 0:
            pwd += -(dial - x) // 100 + (dial != 0)
        dial = (dial - x) % 100
    elif l[0] == "R":
        if dial + x >= 100:
            pwd += (dial + x) // 100
        dial = (dial + x) % 100

print(pwd)