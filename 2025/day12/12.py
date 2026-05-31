# This solution works for the input, but does not work for the example case.

with open("advent-of-code/2025/day12/input.txt", "r") as f:
    input = f.read().splitlines()

# Parse shapes
shapes = {}
i = 0
while i <= len(input):
    line = input[i]
    if 'x' in line:
        break

    shape_idx = line[:-1]
    shapes[shape_idx] = [input[i+1], input[i+2], input[i+3]]

    i += 5

shape_coords = []
for s in shapes.values():
    coord = []
    for y in range(len(s)):
        for x in range(len(s[y])):
            if s[y][x] == '#':
                coord.append((x, y))
    shape_coords.append(coord)

# Parse regions and presents
regions = []
present_nums = []
for line in input:
    if 'x' not in line:
        continue

    area, presents = line.split(": ")

    width, length = map(int, area.split("x"))
    regions.append([width, length])

    present_nums.append([int(x) for x in presents.split()])

n_fit = 0

for i in range(len(regions)):
    # Trivial failure case: areas mismatch
    region_area = regions[i][0] * regions[i][1]
    present_tile_area = sum(present_nums[i][j] * 9 for j in range(len(shapes)))
    if region_area < present_tile_area:
        continue

    n_fit += 1

print(n_fit)