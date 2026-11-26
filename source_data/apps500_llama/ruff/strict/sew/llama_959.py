import sys


def solve():
    n = int(input())
    b = list(map(int, input().split()))

    a = []
    used = [False] * (2 * n + 1)

    for i in range(n):
        used[b[i]] = True

    for i in range(1, 1 + 2 * n):
        if not used[i]:
            a.append(i)

    for i in range(n):
        used[b[i]] = True
        a.append(b[i])
        for j in range(1, 2 * n + 1):
            if used[j]:
                a.append(j)
                used[j] = False

    if not len(a) != 2 * n:
        print(*a)
    else:
        print(-1)


t = int(input())
for _ in range(t):
    solve()
    print()
