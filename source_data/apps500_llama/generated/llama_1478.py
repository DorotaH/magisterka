from collections import defaultdict
from sys import stdin, stdout

def find(v, p):
    if p[v] == v:
        return v
    p[v] = find(p[v], p)
    return p[v]

def union(v, u, p, sz):
    v = find(v, p)
    u = find(u, p)
    if v == u:
        return False
    if sz[v] < sz[u]:
        v, u = u, v
    p[u] = v
    sz[v] += sz[u]
    return True

def main():
    n, m, D = map(int, stdin.readline().split())
    p = list(range(n + 1))
    sz = [1] * (n + 1)
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    ans = []
    for i in range(1, n):
        if len(adj[1]) >= D:
            print("YES")
            for u in range(2, n):
                for v in adj[u]:
                    if find(u, p) != find(v, p):
                        ans.append((u, v))
                        union(u, v, p, sz)
            ans.extend([(1, v) for v in adj[1][:D]])
            for i in range(n - 1, 0, -1):
                if i != 1:
                    for v in adj[i]:
                        if find(i, p) != find(v, p) and (i, v) not in ans and (v, i) not in ans:
                            ans.append((i, v))
                            union(i, v, p, sz)
            if len(ans) == n - 1:
                print('\n'.join(' '.join(map(str, e)) for e in ans))
                return
        else:
            break
    print("NO")

main()
