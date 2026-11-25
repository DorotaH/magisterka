import sys


def find(parent, u):
    if u != parent[u]:
        parent[u] = find(parent, parent[u])
    return parent[u]


def union(parent, rank, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)
    if rootY != rootX:
        if rank[rootY] < rank[rootX]:
            parent[rootY] = rootX
        elif rank[rootY] > rank[rootX]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1


def canMakeAcyclic(n, edges):
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    problematic_edges = []
    for u, v in edges:
        rootU, rootV = find(parent, u), find(parent, v)
        if not rootU == rootV:
            union(parent, rank, u, v)
        else:
            problematic_edges.append((u, v))
    if len(problematic_edges) == 0:
        return True
    if len(problematic_edges) > 1:
        return False
    u, v = problematic_edges[0]
    for i in range(1, 1 + n):
        if u != i and v != i:
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
        u, v = int(data[index]) - 1, int(data[index + 1]) - 1
        edges.append((u, v))
        index = index + 2
    if not canMakeAcyclic(n, edges):
        print("NO")
    else:
        print("YES")


if __name__ == "__main__":
    main()
