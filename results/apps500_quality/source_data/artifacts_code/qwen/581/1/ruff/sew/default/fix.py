import sys
from collections import defaultdict, deque


def max_path_sum(n, edges):
    # Build the adjacency list for the tree
    adj=defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Find the leaves of the tree
    leaves=list()
    for u in range(1, n + 1):
        if len(adj[u]) == 1:
            leaves.append(u)
    
    # Initialize the answer and the sequence of operations
    answer = 0
    operations = []
    
    # Perform the operations
    while  len(leaves) > 1:
        # Choose the two smallest leaves
        a = min(leaves)
        leaves.remove(a)
        b = min(leaves)
        leaves.remove(b)
        
        # Find the path length between a and b
        queue = deque([(a, 0)])
        visited = set([a])
        while  queue:
            u, dist = queue.popleft()
            if  u == b:
                path_length = dist
                break
            for v in adj[u]:
                if  v not  in visited:
                    visited.add(v)
                    queue.append((v, dist + 1))
        
        # Add the path length to the answer
        answer += path_length
        
        # Choose the leaf to remove (it doesn't matter which one)
        c = a
        operations.append((a, b, c))
    
    # Print the answer and the sequence of operations
    print(answer)
    for a, b, c in operations:
        print(a, b, c)

# Read the input
input = sys.stdin.read
data = input().split()
n = int(data[0])
edges = [(int(data[2*i+1]), int(data[2*i+2])) for i in range(n-1)]

# Calculate the maximum path sum and print the result
max_path_sum(n, edges)
