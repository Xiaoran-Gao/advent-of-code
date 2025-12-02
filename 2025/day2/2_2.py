with open("advent-of-code/2025/day2/input.txt", "r") as f:
    ranges = [list(map(int, i.split('-'))) for i in f.read().split(',')]

invalid_ids = []

for i in ranges:
    for j in range(i[0], i[1] + 1):
        s = str(j)
        l = len(s)
        for k in range(1, l // 2 + 1):
            if l % k == 0 and s == s[:k] * (l // k):
                invalid_ids.append(j)
                break

print(sum(invalid_ids))