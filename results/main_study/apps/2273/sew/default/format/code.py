import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = list(map(int, input().split()))
E = [list() for _ in range(0, N)]
for _ in range(M):
    a, b = list(map(int, input().split()))
    E[a - 1].append(b - 1)
    E[b - 1].append(a - 1)

inf = 1 << 20
A, B, C = list(), list(), list()
X = [0] * N
for a in E[0]:
    X[a] = 1
A = [i for i in range(N) if X[i] == 0]
b = min([i for i in range(N) if X[i] == 1] + [inf])
if b < inf:
    for a in E[b]:
        if 1 == X[a]:
            X[a] = 2
    B = [i for i in range(N) if 1 == X[i]]
c = min([i for i in range(0, N) if X[i] == 2] + [inf])
if c < inf:
    for a in E[c]:
        if 2 == X[a]:
            X[a] = 3
    C = [i for i in range(N) if 2 == X[i]]

if (
    max(X) == 2
    and len(A) * len(B) * len(C)
    and (len(A) + len(B) + len(C) == N)
    and (len(A) * len(B) + len(B) * len(C) + len(A) * len(C) == M)
):
    f = 0
    for i in range(N):
        for j in E[i]:
            if X[i] == X[j]:
                f = 1
                break
        if f:
            break
    if f:
        print(-1)
    else:
        print(*[x + 1 for x in X])
else:
    print(-1)
