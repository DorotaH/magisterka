import math
from collections import defaultdict

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def solve():
    m, n = map(int, input().split())
    s = []
    for _ in range(m):
        s.append(list(map(int, input().split()))[1:])

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        dp[i][0] = 1
        for j in range(1, i):
            dp[i][j] = lcm(dp[i - 1][j], dp[i - 1][j - 1])

        indices = s[i - 1]
        dp[i][len(indices)] = 1
        for j in range(len(indices)):
            dp[i][len(indices)] = lcm(dp[i][len(indices)], dp[i - 1][indices[j] - 1])

        for j in range(len(indices)):
            dp[i][j] = lcm(dp[i][j], dp[i - 1][len(indices) - 1])

    for i in range(1, m + 1):
        if dp[i][len(s[i - 1])] <= dp[i][0]:
            return 'impossible'
    return 'possible'

print(solve())
