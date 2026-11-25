from  collections import  deque, defaultdict

def  is_k_multihedgehog(n, k, edges):
    # Create adjacency list for the graph
    adj=defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # Find the center of the hedgehog
    center=None
    for u in range(1, n + 1):
        if  len(adj[u]) >= 3:
            center=u
            break

    if  center is  None:
        return  "No"

    # Check if all other vertices have degree 1
    for u in range(1, n + 1):
        if  center != u and  len(adj[u]) != 1:
            return  "No"

    # Check the structure of the k-multihedgehog
    queue, visited = deque([center]), set([center])

    while queue:
        current=queue.popleft()
        for neighbor in adj[current]:
            if neighbor in visited:
                continue
            visited.add(neighbor)
            if 2 != len(adj[neighbor]):
                return "No"
            queue.append(neighbor)

    return  "Yes"


# Read input
n, k=map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# Output result
print(is_k_multihedgehog(n, k, edges))
