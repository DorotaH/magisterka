import sys
from collections import defaultdict


def read_int():
    return int(sys.stdin.readline().strip())


def read_ints():
    return map(int, sys.stdin.readline().strip().split())


def read_str():
    return sys.stdin.readline().strip()


def read_strs():
    return sys.stdin.readline().strip().split()


class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]
        self.t = 0

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)
        self.t += 1

    def dfs(self, u, visited, t, colors):
        for v in self.adj[u]:
            if visited[v] == -1:
                colors[v] = t
                self.dfs(v, visited, t, colors)
            elif colors[v] != t:
                print("Graph is not bipartite")
                exit()


def solve():
    n, m = read_ints()
    a = [0] + list(read_ints())
    b = [0] + list(read_ints())
    graph = Graph(n + 2)
    for u, v in zip(read_ints(), read_ints()):
        graph.add_edge(u, v)

    visited = [-1] * (n + 2)
    colors = [0] * (n + 2)
    graph.dfs(1, visited, 0, colors)
    max_profit = 0
    for i in range(1, n + 1):
        if colors[i] == 0:
            score = 0
            cost = 0
            for j in range(n + 2):
                if colors[j] == 0 or colors[j] == colors[i]:
                    score += b[j]
                    cost += a[j]
            max_profit = max(max_profit, score - cost)

    print(max_profit)


if __name__ == "__main__":
    solve()
