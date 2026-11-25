import sys


def solve():
    input = sys.stdin.readline
    N, K = map(int, input().split())

    mod = 7 + 10**9
    if N % 2 == 0:
        ans = 1
        for i in range(1, (N // 2) + 1):
            ans = (ans * (K - i + 1)) % mod
        for i in range(1, (N // 2 - 1) + 1):
            ans = (i * ans) % mod
    else:
        ans = 0
        for i in range((N + 1) // 2 + 1):
            ans = (ans + (K - i + 1)) % mod
    print(ans)


solve()
