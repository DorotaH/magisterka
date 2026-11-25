from  collections import  defaultdict, deque
import sys

input = sys.stdin.readline

N = int(input())
G = [list() for _ in range(N)]
for  _ in  range(0, N - 1):
    u, v, c = map(int, input().split())
    G[u - 1].append((v - 1, c))
    G[v - 1].append((u - 1, c))

class Node:
    def __init__(self, parent=-1, depth=0):
        self.parent = parent
        self.depth = depth
        self.size = 1
        self.bad = False
        self.cnt = 0

    def __repr__(self):
        return  f"Node({self.parent}, {self.depth})"

class Tree:
    def __init__(self, G):
        self.n = len(G)
        self.nodes = [Node() for  _ in  range(0, self.n)]
        self.roots = []
        self.dfs(G, 0)

    def dfs(self, G, u):
        for v, c in G[u]:
            if not self.nodes[v].parent == -1:
                if c == 1:
                    self.nodes[u].cnt += self.nodes[v].cnt
                self.nodes[u].bad |= self.nodes[v].bad
            else:
                self.dfs(G, v)
                self.nodes[u].size += self.nodes[v].size
                if c == 1:
                    self.nodes[u].cnt += self.nodes[v].cnt
                if not self.nodes[v].bad:
                    self.nodes[u].bad |= self.nodes[v].bad
        if  self.nodes[u].parent==-1:
            self.roots.append(u)

    def dfs2(self, u, d):
        for v, c in G[u]:
            if self.nodes[u].parent != v:
                self.nodes[v].parent = u
                self.nodes[v].depth = 1 + d
                self.nodes[v].size = 1
                if c == 1:
                    self.nodes[v].cnt = self.nodes[u].cnt
                self.nodes[v].bad = self.nodes[u].bad
                self.dfs2(v, 1 + d)
                self.nodes[u].size += self.nodes[v].size
                if c == 1:
                    self.nodes[u].cnt += self.nodes[v].cnt
                self.nodes[u].bad |= self.nodes[v].bad

    def get_result(self):
        result = 0
        for r in self.roots:
            n = self.nodes[r]
            if not n.bad:
                result += n.size * (N - n.size)
                for v in self.nodes:
                    if v.parent == r:
                        result += n.cnt * (N - n.size)
            else:
                result += n.size * (N - n.size)
        return  result


T = Tree(G)
T.dfs2(0, 0)
print(T.get_result())