from functools import lru_cache


def  dfs(node: int, parent: int, costs: list[int], digits: list[int], targets: list[int], graph: list[list[int]]) -> dict[int, int]:
    @lru_cache(None)
    def  dp(node: int, subset: int) -> int:
        if subset == 0:
            return 0
        cost, n = costs[node], len(graph[node])
        left, right = subset // 2, subset - subset // 2
        left_nodes, right_nodes = sum(1 for child in graph[node] if costs[child] == costs[node] and digits[child] == 0), sum(1 for child in graph[node] if costs[child] == costs[node] and digits[child] == 1)
        return min(
            cost * max(0, n - left_nodes)+dp(node, left_nodes),
            cost * max(0, n - right_nodes)+dp(node, right_nodes)
            )

    visited=[0]*len(graph)
    visited[node]=1
    total_cost=0
    for  child in  graph[node]:
        if not visited[child]:
            total_cost += dfs(child, node, costs, digits, targets, graph)
    if  digits[node] != targets[node]:
        total_cost = total_cost + min(dp(node, len(graph[node])), float('inf'))
    return total_cost

n = int(input())
costs, digits, targets = list(), list(), list()
graph = [list() for  _ in  range(0, n)]
for  i in  range(n):
    a, b, c=map(int, input().split())
    costs.append(a)
    digits.append(b)
    targets.append(c)

for  _ in  range(n - 1):
    u, v=map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

if sum(1 for i in range(n) if targets[i] != digits[i]) == 0:
    print(0)
else:
    print(dfs(0, -1, costs, digits, targets, graph))
