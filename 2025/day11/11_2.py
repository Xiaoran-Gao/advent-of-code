from functools import cache

with open("advent-of-code/2025/day11/input.txt", "r") as f:
    input = [list(c.split(': ')) for c in f.read().splitlines()]

graph = {}
for line in input:
    graph[line[0]] = list(line[1].split(' '))

nodes = ['svr', 'fft', 'dac']
goals = ['fft', 'dac', 'out']
ans = 1

@cache
def dfs(node, goal):
    if node == goal:
        return 1
    
    n_paths = 0

    for k in graph.get(node, []):
        n_paths += dfs(k, goal)
    
    return n_paths

for i in range(len(nodes)):
    ans *= dfs(nodes[i], goals[i])

print(ans)