with open("advent-of-code/2025/day1/input.txt", "r") as f:
    lines = f.read().splitlines()

dial = 50
pwd = 0

for l in lines:
    x = int(l[1:])
    if l[0] == "L":
        dial = (dial - x) % 100
    elif l[0] == "R":
        dial = (dial + x) % 100
    if dial == 0:
        pwd += 1

print(pwd)