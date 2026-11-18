import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# node : 0<=i<=3*N-1, i:minus i+1: delete i+2: plus
# start : 3*N
# goal : 3*N+1

EDGE = [dict() for i in range(3 * N + 2)]
V = 3 * N + 2
start = 3 * N
goal = 3 * N + 1

for i in range(N):
    EDGE[start][i * 3] = -B[i] + (1 << 30)
    EDGE[i * 3][3 * i + 1] = A[i] + (1 << 30)
    EDGE[3 * i + 1][3 * i + 2] = B[i] + (1 << 30)
    EDGE[3 * i + 2][goal] = float("inf")

for i in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1

    EDGE[3 * x + 1][y * 3] = float("inf")
    EDGE[3 * y + 1][x * 3] = float("inf")

ANS = 0
while True:
    USED = [0] * V
    ROUTE, Q = [-1] * V, [(start, float("inf"))]

    while Q:  # DFS
        NOW, cost = Q.pop()
        if goal == NOW:
            break

        for to in EDGE[NOW]:
            if 0 == USED[to] and 0 != EDGE[NOW][to]:
                ROUTE[to] = NOW
                USED[to] = 1
                Q.append((to, min(cost, EDGE[NOW][to])))
    else:
        break

    ANS += cost
    i = goal
    while i != start:  # goalからたどり,Routeを使ってEDGEの更新
        j = ROUTE[i]
        EDGE[j][i] -= cost  # 使ったルートをいけなく更新
        if not j in EDGE[i]:
            EDGE[i][j] = cost
        else:
            EDGE[i][j] += (
                cost  # 逆向きに進めるようにする.これらを重みつきにすれ普通のフロー
            )

        i = j

print(-(ANS - (N << 30)))
