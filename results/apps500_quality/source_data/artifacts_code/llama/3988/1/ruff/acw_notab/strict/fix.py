from collections import defaultdict
from sys import stdin


class Graph:
    def __init__(self, n):
        self.n = n
        self.g = defaultdict(list)
        self.in_degree = [0] * (1 + n)
        self.out_degree = [0] * (1 + n)

    def add_edge(self, u, v, directed):
        self.g[u].append((v, directed))
        self.out_degree[u] += 1
        if directed:
            self.in_degree[v] += 1
        else:
            self.out_degree[v] += 1
            self.in_degree[v] += 1
            self.in_degree[u] += 1

    def dfs(self, u, visited, plan):
        visited[u] = 1
        for v, directed in self.g[u]:
            if visited[v] == 0:
                self.dfs(v, visited, plan)
        plan[u] = 1

    def get_plan(self, maximize):
        visited = [0] * (1 + self.n)
        plan = [0] * (1 + self.m)
        self.dfs(self.s, visited, plan)
        for i in range(1, 1 + self.m):
            u, _, v = self.edges[i]
            if visited[v] == 0:
                plan[i] = 1 if maximize else -1
        return visited.count(1), plan


n, m, s = map(int, stdin.readline().split())
g = Graph(n)
for _ in range(m):
    t, u, v = map(int, stdin.readline().split())
    g.add_edge(u, v, t == 1)

max_plan, max_plan_str = g.get_plan(1)
min_plan, min_plan_str = g.get_plan(0)
print(max_plan)
print(''.join('+' if x == 1 else '-' for x in max_plan_str[:-1]))
print(min_plan)
print(''.join('+' if x == -1 else '-' for x in min_plan_str[:-1]))
