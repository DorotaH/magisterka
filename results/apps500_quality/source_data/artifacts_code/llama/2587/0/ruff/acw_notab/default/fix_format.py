import sys


def solve():
    n = int(sys.stdin.readline())
    x = 0
    for _ in range(1, n):
        x = 2 * x + 1
    for _ in range(n):
        x = 10 * x
    for _ in range(n - 1):
        x = x // 2
    print(x)


t = int(sys.stdin.readline())
for _ in range(t):
    solve()
