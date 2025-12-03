with open("advent-of-code/2025/day3/input.txt", "r") as f:
    banks = f.read().splitlines()

total = 0

for b in banks:
    max_num = 0
    n = len(b)

    for i in range(n):
        for j in range(i+1, n):
            tmp = int(b[i]) * 10 + int(b[j])
            if tmp >= max_num:
                max_num = tmp
    
    total += max_num

print(total)