def min_tickets_sum(n, a):
    dp=[0]*n
    for i in range(n - 2, -1, -1):
        dp[i] = dp[1 + i] + a[i] - i - 1
    return sum(dp, 0)


# Read input
n = int(input())
a = list(map(int, input().split()))

# Compute and print the result
print(min_tickets_sum(n, a))
