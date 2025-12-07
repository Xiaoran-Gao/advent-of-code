with open("advent-of-code/2025/day6/input.txt", "r") as f:
    lines = f.read().splitlines()

num = []

for i in range(len(lines[0])):
    num.append(''.join(lines[j][i] for j in range(len(lines) - 1)))

grouped_num = []
tmp = []

for i in num:
    if not all(j == ' ' for j in i):
        tmp.append(int(i.strip()))
    else:
        grouped_num.append(tmp)
        tmp = []

grouped_num.append(tmp)

op = lines[-1].split()

ans_total = 0

for i in range(len(op)):
    if op[i] == '*':
        ans = 1
    if op[i] == '+':
        ans = 0
    
    for j in range(len(grouped_num[i])):
        if op[i] == '*':
            ans *= grouped_num[i][j]
        if op[i] == '+':
            ans += grouped_num[i][j]
    
    ans_total += ans

print(ans_total)