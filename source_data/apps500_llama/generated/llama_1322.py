import sys
input = sys.stdin.readline
mod = 998244353

def read_int():
    return int(input())

def read_ints():
    return map(int, input().split())

def read_ints0():
    return map(lambda x: int(x) - 1, input().split())

def read_str():
    return input().strip()

def solve():
    n, k = read_ints()
    a = [int(x) if x != '-1' else -1 for x in input().split()]

    if n == 2 and a[0] == -1 and a[1] == -1:
        return 9

    dp = [0] * (n + 2)
    dp[0] = 1

    for i in range(1, n + 2):
        dp[i] = dp[i - 1]

    for i in range(1, n + 1):
        if a[i - 1] != -1:
            continue

        for j in range(1, k + 1):
            dp[i] = (dp[i] + dp[i - 1] * j) % mod

    dp[n + 1] = 1
    for i in range(n, 0, -1):
        if a[i - 1] != -1:
            continue

        for j in range(1, k + 1):
            dp[i] = (dp[i] + dp[i + 1] * j) % mod

    dp[0] = (dp[0] + dp[1] * (k ** (n - 1))) % mod
    for i in range(2, n + 1):
        dp[0] = (dp[0] + dp[i] * (k ** (n - i + 1))) % mod

    for i in range(2, n + 1):
        if a[i - 1] == a[i - 2]:
            for j in range(1, k + 1):
                dp[i] = (dp[i] + dp[i - 2] * (k ** (n - i + 2))) % mod

    return dp[n + 1]

print(solve())
