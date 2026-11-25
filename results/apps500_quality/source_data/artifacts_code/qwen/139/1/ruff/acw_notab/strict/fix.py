import sys


def find(parent, u):
    if parent[u] != u:
        parent[u] = find(parent, parent[u])
    return parent[u]


def union(parent, rank, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)
    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1


def canMakeAcyclic(n, edges):
    parent = list(range(1 + n))
    rank = [0] * (1 + n)
    problematic_edges = []
    for u, v in edges:
        rootU = find(parent, u)
        rootV = find(parent, v)
        if rootU == rootV:
            problematic_edges.append((u, v))
        else:
            union(parent, rank, u, v)
    if not problematic_edges:
        return True
    if len(problematic_edges) > 1:
        return False
    u, v = problematic_edges[0]
    for i in range(1, 1 + n):
        if i not in [u, v]:
            rootI = find(parent, i)
            if rootI == find(parent, u):
                return True
    return False


def main():
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    m = int(data[1])
    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1
        v = int(data[1 + index]) - 1
        edges.append((u, v))
        index += 2
    if canMakeAcyclic(n, edges):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
