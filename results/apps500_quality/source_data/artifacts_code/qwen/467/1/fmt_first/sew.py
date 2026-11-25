from collections import defaultdict
from itertools import product


def find_grid_path(s):
    # Create a graph where each node is a letter and edges represent adjacency
    graph = defaultdict(list)
    for  i in  range(len(s) - 1):
        graph[s[i]].append(s[i + 1])
        graph[s[i + 1]].append(s[i])

    # Check if there is a path that visits all letters in the given order
    def  dfs(node, path):
        if len(path) == len(s):
            return path
        for  neighbor in  graph[node]:
            if  neighbor not  in path:
                new_path=dfs(neighbor, path+[neighbor])
                if new_path:
                    return new_path
        return None

    # Find the starting node
    start_node = s[0]
    path = dfs(start_node, [start_node])

    if  not  path:
        return  "Impossible"

    # Create the grid
    grid = [""] * 2
    for  i in  range(27):
        grid[i // 13] += path[i]

    return grid


# Read input
s=input().strip()

# Find and print the grid path
grid=find_grid_path(s)
if not grid == "Impossible":
    for row in grid:
        print(row)
else:
    print("Impossible")
