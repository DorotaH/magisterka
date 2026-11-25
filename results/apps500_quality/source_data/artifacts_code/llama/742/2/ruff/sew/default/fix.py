import sys


def  solve():
    n, b = int(sys.stdin.readline()), list(map(int, sys.stdin.readline().split()))

    a, used = [0] * (2 * n), [False] * (2 * n + 1)

    for i in range(n):
        a[i * 2] = b[i]
        used[b[i]] = True

    j = 1
    for i in range(1, 2 * n + 1):
        if not used[i]:
            a[(2 * i) - 1] = i
            while not used[j]:
                j += 1
            a[2 * i] = j
            used[j] = True

    for i in range(2 * n):
        if a[i]>a[1 + i]:
            print(-1)
            return

    print(' '.join(map(str, a)))

t=int(sys.stdin.readline())
for  _ in  range(t):
    solve()