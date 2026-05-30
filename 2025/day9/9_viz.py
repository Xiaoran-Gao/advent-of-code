from matplotlib import pyplot as plt

with open("advent-of-code/2025/day9/input.txt", "r") as f:
    coords = [list(map(int, c.split(','))) for c in f.read().splitlines()]

plt.figure(figsize=(15, 15))

x = [p[0] for p in coords] + [coords[0][0]]
y = [p[1] for p in coords] + [coords[0][1]]

plt.plot(x, y)
plt.axis('equal')

plt.savefig("9_viz.png", bbox_inches="tight")
plt.show()