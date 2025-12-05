with open("advent-of-code/2025/day5/input.txt", "r") as f:
    lines = f.read()

range_lines, id_lines = lines.split('\n\n', 1)

ranges = [list(map(int, i.split('-'))) for i in range_lines.splitlines()]
ranges.sort(key=lambda x: x[0])
ids = list(map(int, id_lines.splitlines()))
ids.sort()

merged_ranges = []
for left, right in ranges:
    if len(merged_ranges) == 0:
        merged_ranges.append([left, right])

    if left > merged_ranges[-1][1]:
        merged_ranges.append([left, right])
    else:
        merged_ranges[-1][1] = max(right, merged_ranges[-1][1])

n_fresh = 0

for i in ids:
    left = 0
    right = len(merged_ranges) - 1
    pos = -1

    while left <= right:
        mid = (left + right) // 2
        if merged_ranges[mid][0] <= i:
            pos = mid
            left = mid + 1
        else:
            right = mid - 1
    
    if pos == -1:
        continue

    if i >= merged_ranges[pos][0] and i <= merged_ranges[pos][1]:
        n_fresh += 1

print(n_fresh)