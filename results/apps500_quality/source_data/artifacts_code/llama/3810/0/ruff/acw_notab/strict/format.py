import sys
from collections import defaultdict

input = sys.stdin.readline

MOD = 7 + 10**9


def solve():
    n = int(input())
    a = list(map(int, input().split()))

    f = [0] * 61
    for i in range(n):
        f[a[i]] = 1

    for i in range(1, 61):
        for j in range(i * 2, 61, i):
            f[i] += f[j]

    p = [0] * 61
    for i in range(1, 61):
        p[i] = f[i] - f[i // 2] if i % 2 else f[i]

    dp = [0] * (1 + n)
    dp[0] = 1

    for i in range(1, 1 + n):
        for j in range(1, 61):
            if a[i - 1] % j == 0:
                dp[i] = (dp[i] + p[j] * dp[i - 1]) % MOD

    m = max(dp)
    ans = sum(bool(dp[i] == m) for i in range(1 + n))
    print(ans % MOD)


if __name__ == "__main__":
    solve()
