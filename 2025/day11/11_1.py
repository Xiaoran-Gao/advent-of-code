with open("advent-of-code/2025/day11/input.txt", "r") as f:
    input = [list(c.split(': ')) for c in f.read().splitlines()]

graph = {}
for line in input:
    graph[line[0]] = list(line[1].split(' '))

def dfs(node, goal):
    if node == goal:
        return 1
    
    n_paths = 0

    for k in graph.get(node, []):
        n_paths += dfs(k, goal)
    
    return n_paths

print(dfs('you', 'out'))