with open("advent-of-code/2025/day5/input.txt", "r") as f:
    lines = f.read()

range_lines, id_lines = lines.split('\n\n', 1)

ranges = [list(map(int, i.split('-'))) for i in range_lines.splitlines()]
ranges.sort(key=lambda x: x[0])

merged_ranges = []
for left, right in ranges:
    if len(merged_ranges) == 0:
        merged_ranges.append([left, right])

    if left > merged_ranges[-1][1]:
        merged_ranges.append([left, right])
    else:
        merged_ranges[-1][1] = max(right, merged_ranges[-1][1])

n_fresh = 0

for i in merged_ranges:
    n_fresh += i[1] - i[0] + 1

print(n_fresh)