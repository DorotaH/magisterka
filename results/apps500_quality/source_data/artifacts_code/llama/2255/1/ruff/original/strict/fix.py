from collections import deque


def dfs(v, g, visited):
    q = deque()
    q.append(v)
    while q:
        v = q.popleft()
        if not visited[v]:
            visited[v] = True
            for u in g[v]:
                if not visited[u]:
                    q.append(u)

def main():
    n, m = map(int, input().split())
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    visited = [False] * (n + 1)
    dfs(1, g, visited)

    ans = []
    for i in range(1, n + 1):
        if not visited[i]:
            ans.append(i)

    while g[ans[-1]]:
        max_val = -1
        v = ans[-1]
        for u in g[v]:
            if u != ans[-1] and not visited[u]:
                if len(g[u]) > max_val:
                    max_val = len(g[u])
                    next_v = u
        ans.append(next_v)

    print(' '.join(map(str, ans)))

if __name__ == "__main__":
    main()
