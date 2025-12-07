with open("advent-of-code/2025/day6/input.txt", "r") as f:
    lines = f.read().splitlines()

num = [list(map(int, lines[i].split())) for i in range(len(lines) - 1)]
op = lines[-1].split()

ans_total = 0

for i in range(len(op)):
    if op[i] == '*':
        ans = 1
    if op[i] == '+':
        ans = 0
    
    for j in range(len(num)):
        if op[i] == '*':
            ans *= num[j][i]
        if op[i] == '+':
            ans += num[j][i]
    
    ans_total += ans

print(ans_total)