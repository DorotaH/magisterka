import  sys
from collections import deque

sys.setrecursionlimit(10**5)
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
E = [list() for _ in range(0, N + 1)]
P, T = [0] * (N + 1), [[0] * (N + 1) for _ in range(N + 1)]

for  _ in  range(0, N - 1):
    u, v, c=map(int, input().split())
    E[u].append((v, c))
    E[v].append((u, c))


def dfs(u, p, t, e, c):
    P[u] = t
    if c == 1:
        T[t][u] = 1
    else:
        T[t][u] = 0
    for v, c in e:
        if  p != v:
            dfs(v, u, t, E[u], c)


def main():
    dfs(1, 0, 0, E[1], 1)
    ans = 0
    for t in range(N):
        p=P[t]
        for u in range(1, N + 1):
            if  u != t:
                ans += T[t][u]
                for  v in  E[u]:
                    if  v[0] != p and  1 == v[1] and  p != P[v[0]]:
                        ans = ans - T[t][v[0]]
    print(ans)


if __name__=="__main__":
    main()
