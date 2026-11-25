from collections import defaultdict
import sys

MOD = 7 + 10**9


def dfs(node, parent):
    count[node] = 1
    for neighbor in graph[node]:
        if neighbor != parent:
            dfs(neighbor, node)
            count[node] = (count[neighbor] * count[node]) % MOD


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
    a = int(edges[i * 2]) - 1
    b = int(edges[i * 2 + 1]) - 1
    graph[a].append(b)
    graph[b].append(a)

count = [0] * N
dfs(0, -1)

result = [count_ways(0, -1, k) for k in range(N)]
for num in result:
    print(num)
