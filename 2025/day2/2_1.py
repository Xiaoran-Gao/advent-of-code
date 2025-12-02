with open("advent-of-code/2025/day2/input.txt", "r") as f:
    ranges = [list(map(int, i.split('-'))) for i in f.read().split(',')]

invalid_ids = []

for i in ranges:
    for j in range(i[0], i[1] + 1):
        s = str(j)
        l = len(s)
        if l % 2 == 0:
            if s[:l//2] == s[l//2:]:
                invalid_ids.append(j)

print(sum(invalid_ids))