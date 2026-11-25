import sys
import heapq


class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1


def main():
    input_lines = sys.stdin.readlines()
    N, M = map(int, input_lines[0].split())
    edges = []
    for i in range(1, 1 + M):
        L, R, D = map(int, input_lines[i].split())
        edges.append((L - 1, R - 1, D))

    edges.sort(key=lambda x: x[0])

    disjoint_set = DisjointSet(N)
    for edge in edges:
        L, R, D = edge
        if disjoint_set.find(L) != disjoint_set.find(R):
            if R - L != D:
                print("No")
                return
            disjoint_set.union(L, R)

    print("Yes")


if __name__ == "__main__":
    main()
