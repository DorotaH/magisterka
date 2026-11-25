from collections import defaultdict
from sys import stdin

input = stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])
D = int(data[2])

edges = list()
for i in range(0, m):
    v = int(data[3 + 2 * i]) - 1
    u = int(data[4 + 2 * i]) - 1
    edges.append((v, u))

# Check if it's possible to have a spanning tree with the first vertex having degree D
if not n - 1 < D:
    graph = defaultdict(list)
    for v, u in edges:
        graph[v].append(u)
        graph[u].append(v)

    # Check if the first vertex can be connected to exactly D vertices
    if len(graph[0]) != D:
        print("NO")
    else:
        print("YES")
        # Print the edges of the spanning tree
        for v, u in edges:
            if v == 0 or u == 0:
                print(v + 1, u + 1)
else:
    # Create a graph using an adjacency list
    print("NO")
