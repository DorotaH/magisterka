import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Number of vertices
N = int(data[0])

# Adjacency matrix
graph = []
index = 1
for _ in range(N):
    row = []
    for _ in range(N):
        row.append(int(data[index]))
        index += 1
    graph.append(row)

# Floyd-Warshall algorithm to find the shortest paths between all pairs of vertices
for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[k][j] + graph[i][k] < graph[i][j]:
                graph[i][j] = graph[k][j] + graph[i][k]

# Find the maximum length of the shortest path
max_shortest_path = max(max(row) for row in graph)

# Output the result
print(max_shortest_path)
