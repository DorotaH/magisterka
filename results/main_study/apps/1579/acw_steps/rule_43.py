from collections import defaultdict
import sys


sys.setrecursionlimit(10 ** 6)


def main():
    N = int(input())
    V = 100005
    to = defaultdict(list)
    for _ in range(N):
        X, Y = map(int, input().split())
        Y += V
        to[X].append(Y)
        to[Y].append(X)
    visited = [0] * (V * 2)
    cnt = 2 * [0]  # cnt = [cnt of X, cnt of Y]

    def dfs(v):
        if visited[v] == 1:
            return
        visited[v] = 1
        cnt[v // V] += 1
        for nv in to[v]:
            dfs(nv)

    ans = 0
    for v in range(V * 2):
        if visited[v] == 1:
            continue
        cnt = 2 * [0]
        dfs(v)
        ans += cnt[1] * cnt[0]
    ans -= N

    print(ans)


def __starting_point():
    main()
__starting_point()
