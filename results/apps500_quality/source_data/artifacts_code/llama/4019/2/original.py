from collections import defaultdict

def find_min_tree(n, m, D, edges):
    parent = [i for i in range(n)]
    rank = [1] * n
    edges_dict = defaultdict(list)

    for i in range(m):
        v, u = edges[i]
        edges_dict[v].append(u)
        edges_dict[u].append(v)

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            if rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_x] = root_y
                if rank[root_x] == rank[root_y]:
                    rank[root_y] += 1

    def is_valid_tree(n, D):
        if find(0) != 0:
            return False
        return len(edges_dict[1]) == D

    for v in range(1, n):
        for u in edges_dict[v]:
            if find(v) != find(u):
                union(v, u)

    if is_valid_tree(n, D):
        return edges_dict
    else:
        return None

def solve():
    n, m, D = map(int, input().split())
    edges = []
    for _ in range(m):
        v, u = map(int, input().split())
        edges.append((v - 1, u - 1))

    tree = find_min_tree(n, m, D, edges)
    if tree is None:
        print('NO')
    else:
        print('YES')
        for v in range(1, n):
            for u in tree[v]:
                if u != v:
                    print(f'{u + 1} {v}')

if __name__ == '__main__':
    solve()
