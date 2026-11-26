import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])

edges = []
for i in range(M):
    A = int(data[2 + i * 2])
    B = int(data[3 + i * 2])
    edges.append((A, B))

# Check if there exists an induced subgraph where each vertex has in-degree and out-degree 1
# This subgraph is a directed cycle

# Find a directed cycle
visited = [False] * (N + 1)
stack = []
in_stack = [False] * (N + 1)


def dfs(node):
    stack.append(node)
    in_stack[node] = True
    visited[node] = True
    for neighbor in range(1, N + 1):
        if (node, neighbor) in edges and not visited[neighbor]:
            dfs(neighbor)
    stack.pop()
    in_stack[node] = False


for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)

# Check if there is a cycle in the stack
cycle = []
for i in range(len(stack) - 1, -1, -1):
    if in_stack[stack[i]]:
        cycle.append(stack[i])
    else:
        break

# If there is a cycle, check if it forms a directed cycle
if 1 < len(cycle):
    is_cycle = all((cycle[i], cycle[i + 1]) in edges for i in range(len(cycle) - 1))
    is_cycle = True if (cycle[-1], cycle[0]) in edges else False
    if is_cycle:
        print(len(cycle))
        for vertex in cycle:
            print(vertex)
        exit(0)

print(-1)
