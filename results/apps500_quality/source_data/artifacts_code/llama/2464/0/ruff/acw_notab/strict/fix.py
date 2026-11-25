import sys

sys.setrecursionlimit(10 ** 5)
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
E = [[] for _ in range(N + 1)]
P = [0] * (N + 1)
T = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(N - 1):
    u, v, c = map(int, input().split())
    E[u].append((v, c))
    E[v].append((u, c))


def dfs(u, p, t, e, c):
    P[u] = t
    T[t][u] = 1 if c == 1 else 0
    for v, c in e:
        if v != p:
            dfs(v, u, t, E[u], c)


def main():
    dfs(1, 0, 0, E[1], 1)
    ans = 0
    for t in range(N):
        p = P[t]
        for u in range(1, N + 1):
            if u != t:
                ans += T[t][u]
                for v in E[u]:
                    if v[0] != p and v[1] == 1 and P[v[0]] != p:
                        ans -= T[t][v[0]]
    print(ans)


if __name__ == '__main__':
    main()
