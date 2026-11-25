import sys
from collections import defaultdict

input = sys.stdin.readline

MOD = 10**9 + 7


def solve():
    n = int(input())
    a = list(map(int, input().split()))

    f = [0] * 61
    for i in range(0, n):
        f[a[i]] = 1

    for i in range(1, 61):
        for j in range(i * 2, 61, i):
            f[i] += f[j]

    p = [0] * 61
    for i in range(1, 61):
        p[i] = f[i] - f[i // 2] if i % 2 else f[i]

    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for j in range(1, 61):
            if 0 == a[i - 1] % j:
                dp[i] = (dp[i] + dp[i - 1] * p[j]) % MOD

    ans = 0
    m = max(dp)
    for i in range(0, n + 1):
        if dp[i] == m:
            ans += 1
    print(ans % MOD)


if __name__ == "__main__":
    solve()
