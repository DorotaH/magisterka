import sys
from collections import defaultdict

MOD = 10**9 + 7

def dfs(node, parent):
    count[node] = 1
    for neighbor in graph[node]:
        if neighbor != parent:
            dfs(neighbor, node)
            count[node] = (count[node] * count[neighbor]) % MOD

def count_ways(node, parent, k):
    if node == k:
        return 1
    result = 0
    for neighbor in graph[node]:
        if neighbor != parent:
            result = (result + count_ways(neighbor, node, k)) % MOD
    return result

input = sys.stdin.read
data = input().split()

N = int(data[0])
edges = data[1:]

graph = defaultdict(list)
for i in range(N - 1):
    a = int(edges[2 * i]) - 1
    b = int(edges[2 * i + 1]) - 1
    graph[a].append(b)
    graph[b].append(a)

count = [0] * N
dfs(0, -1)

result = []
for k in range(N):
    result.append(count_ways(0, -1, k))

for num in result:
    print(num)
