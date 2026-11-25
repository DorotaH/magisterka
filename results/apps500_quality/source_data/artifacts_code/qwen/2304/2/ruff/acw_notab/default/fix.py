import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])

edges = []
for i in range(M):
    L = int(data[i * 3 + 2]) - 1
    R = int(data[i * 3 + 3]) - 1
    D = int(data[i * 3 + 4])
    edges.append((L, R, D))

# Find connected components
components = {}
component_id = 0
for i in range(N):
    if i not in components:
        components[i] = component_id
        stack = [i]
        while stack:
            node = stack.pop()
            for edge in edges:
                if edge[0] == node and edge[1] not in components:
                    components[edge[1]] = component_id
                    stack.append(edge[1])
            for edge in edges:
                if edge[1] == node and edge[0] not in components:
                    components[edge[0]] = component_id
                    stack.append(edge[0])
        component_id += 1

# Check if distances within components are consistent
for component in components.values():
    component_nodes = [i for i in range(N) if components[i] == component]
    component_edges = [edge for edge in edges if edge[0] in component_nodes and edge[1] in component_nodes]
    if 1 < len(component_edges):
        distances = [edge[2] for edge in component_edges]
        if any(d != distances[0] for d in distances):
            print("No")
            sys.exit(0)

print("Yes")
