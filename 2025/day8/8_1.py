with open("advent-of-code/2025/day8/input.txt", "r") as f:
    coords = [list(map(int, c.split(','))) for c in f.read().splitlines()]

class DSU:
    def __init__(self, n):
        self.parent = {i: i for i in range(n)}
        self.size = {i: 1 for i in range(n)}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)

        if ra == rb:
            return False
        
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True

dist_sq = {}
for i in range(len(coords) - 1):
    for j in range(i + 1, len(coords)):
        dist_sq[(i, j)] = (coords[i][0] - coords[j][0]) ** 2 + \
                          (coords[i][1] - coords[j][1]) ** 2 + \
                          (coords[i][2] - coords[j][2]) ** 2

dist_sq_sort = dict(sorted(dist_sq.items(), key=lambda x: x[1]))

dsu = DSU(len(coords))

n_union = 0

for (i, j) in dist_sq_sort:
    n_union += 1
    dsu.union(i, j)

    if n_union == 1000:
        break

circuits = list(set(dsu.parent.values()))
sizes = []

for c in circuits:
    sizes.append(dsu.size.get(c, 0))

sizes.sort(reverse=True)
print(sizes[0] * sizes[1] * sizes[2])