from collections import deque
from sys import stdin


def main():
    n, k = map(int, stdin.readline().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    cnt = [0] * (n + 1)
    parent = [-1] * (n + 1)
    q = deque()

    for i in range(1, n + 1):
        for j in graph[i]:
            if parent[j] == -1:
                parent[i] = j
                cnt[i] = 1
                q.append(i)
                break

    while q:
        v = q.popleft()
        for u in graph[v]:
            if u != parent[v]:
                cnt[v] += 1
                parent[u] = v
                q.append(u)

    for v in range(1, n + 1):
        if v != 1 and cnt[v] != 1:
            print('No')
            return

    cnt[1] = k
    q = deque()
    q.append(1)

    while cnt[1] > 0:
        v = q.popleft()
        for u in graph[v]:
            if cnt[u] == 1:
                cnt[1] -= 1
                cnt[u] = 0
                q.append(u)
                for w in graph[u]:
                    if w != v:
                        cnt[w] = 1
                        q.append(w)

    if cnt[1] > 0 or any(cnt[i] != 0 for i in range(1, n + 1)):
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    main()
