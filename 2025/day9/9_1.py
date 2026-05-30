with open("advent-of-code/2025/day9/input.txt", "r") as f:
    coords = [list(map(int, c.split(','))) for c in f.read().splitlines()]

area = {}

for i in range(len(coords) - 1):
    for j in range(i + 1, len(coords)):
        area[(i, j)] = (abs(coords[i][0] - coords[j][0]) + 1) * \
                       (abs(coords[i][1] - coords[j][1]) + 1)

area_sort = sorted(area.values(), reverse=True)

print(area_sort[0])