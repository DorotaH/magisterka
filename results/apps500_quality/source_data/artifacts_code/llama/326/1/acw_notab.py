from collections import deque

N = int(input())
strings = []
costs = []
for _ in range(N):
    s, c = input().split()
    strings.append(s)
    costs.append(int(c))


def is_palindrome(s):
    return s == s[::-1]


def min_cost():
    dp = [[float('inf')] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(1, i + 1):
            if is_palindrome(strings[i]):
                dp[j][i + 1] = min(dp[j][i], dp[j - 1][i - 1] + costs[i])
            else:
                dp[j][i + 1] = min(dp[j][i], dp[j][i - 1] + costs[i])
    return next((dp[j][N] for j in range(N + 1) if float('inf') > dp[j][N]), -1)


print(min_cost())
