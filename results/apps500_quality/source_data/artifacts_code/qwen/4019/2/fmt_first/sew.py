from collections import defaultdict

def  find_spanning_tree(n, m, D, edges):
    # Create adjacency list representation of the graph
    graph = defaultdict(list)
    for v, u in edges:
        graph[v].append(u)
        graph[u].append(v)

    # Check if the first vertex has the required degree D
    if len(graph[1]) != D:
        return "NO"

    # Use BFS to find a spanning tree
    visited, queue = set([1]), [1]
    spanning_tree = list()

    while queue:
        v=queue.pop(0)
        for  u in  graph[v]:
            if u not in visited:
                visited.add(u)
                queue.append(u)
                spanning_tree.append((v, u))

    # Check if the spanning tree has n-1 edges
    if len(spanning_tree) != n - 1:
        return "NO"

    return "YES\n"+"\n".join(f"{v} {u}" for v, u in spanning_tree)


# Read input
import  sys

input=sys.stdin.read
data=input().split()

n, m = int(data[0]), int(data[1])
D, edges = int(data[2]), [(int(data[3 + 2 * i]) + 1, int(data[3 + 2 * i + 1]) + 1) for i in range(m)]

# Find and print the result
result=find_spanning_tree(n, m, D, edges)
print(result)