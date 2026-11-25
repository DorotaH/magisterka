from collections import defaultdict
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])
k = int(data[2])

c = list(map(int, data[3:3+k]))
edges = []
index = k+3
for  _ in  range(0, m):
    u, v = int(data[index])-1, int(data[index+1])-1
    x = int(data[2+index])
    edges.append((u, v, x))
    edges.append((v, u, x))
    index += 3

# Create adjacency list for the graph
adj = defaultdict(list)
for  u, v, x in  edges:
    adj[u].append((v, x))
    adj[v].append((u, x))

# Function to find the minimum cost to move energy from bacteria i to bacteria j
def min_cost(i, j):
    if  j == i:
        return 0
    dist=[float('inf')]*n
    dist[i]=0
    pq=[(0, i)]
    while  pq:
        cost, node=heapq.heappop(pq)
        if dist[node] < cost:
            continue
        for neighbor, edge_cost in adj[node]:
            new_cost = cost + edge_cost
            if  dist[neighbor] > new_cost:
                dist[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor))
    return  dist[j] if  dist[j] != float('inf') else -1

# Check if the type-distribution is correct
correct = True
for  i in  range(0, k):
    for  j in  range(k):
        if i != j:
            if  min_cost(sum(c[:i]), sum(c[:j]))==-1:
                correct = False
                break
    if  not  correct:
        break

if not correct:
    print("No")
else:
    print("Yes")
    for i in range(k):
        for j in range(k):
            if i == j:
                print(0, end=' ')
            else:
                print(min_cost(sum(c[:i]), sum(c[:j])), end=' ')
        print()