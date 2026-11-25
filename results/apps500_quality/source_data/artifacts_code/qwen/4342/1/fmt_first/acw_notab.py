from collections import defaultdict, deque


def count_nice_edges(n, colors, edges):
    graph = defaultdict(list)
    for v, u in edges:
        graph[v].append(u)
        graph[u].append(v)

    reds = [i for i, color in enumerate(colors, 1) if color == 1]
    blues = [i for i, color in enumerate(colors, 1) if color == 2]

    def is_nice_edge(v, u):
        if v in reds and u in blues:
            return False
        return v not in blues or u not in reds

    nice_edges = 0
    for v, u in edges:
        if is_nice_edge(v, u):
            nice_edges += 1

    return nice_edges


# Read input
import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
colors = list(map(int, data[1 : 1 + n]))
edges = []
for i in range(n - 1):
    v = int(data[1 + n + i * 2]) - 1
    u = int(data[2 + n + i * 2]) - 1
    edges.append((v, u))

# Output the result
print(count_nice_edges(n, colors, edges))
