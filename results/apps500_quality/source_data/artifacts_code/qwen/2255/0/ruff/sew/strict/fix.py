import sys
from collections import defaultdict, deque

input=sys.stdin.read
data=input().split()

n, m = int(data[0]), int(data[1])

edges=defaultdict(list)
for  i in  range(0, m):
    u = int(data[2 + 2 * i]) - 1
    v = int(data[3 + 2 * i]) - 1
    edges[u].append(v)
    edges[v].append(u)

# Sort the edges to ensure lexicographical order
for  i in  range(0, n):
    edges[i].sort()

# Initialize the result list and visited set
result, visited = [], set()

# Function to perform BFS and find the lexicographically smallest sequence
def  bfs(start):
    queue=deque([start])
    visited.add(start)
    while queue:
        current=queue.popleft()
        result.append(current + 1)
        for  neighbor in  edges[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Start BFS from node 0
bfs(0)

# Print the result
print(' '.join(map(str, result)))
