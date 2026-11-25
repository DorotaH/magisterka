n = int(input())
a = list(map(int, input().split()))


def find_longest_subsegment(a):
    n = len(a)
    dp = [1] * n
    max_length = 1

    # Forward pass
    for i in range(1, n):
        if a[i] > a[i - 1]:
            dp[i] = 1 + dp[i - 1]
            max_length = max(max_length, dp[i])

    # Backward pass
    for i in range(n - 2, -1, -1):
        if a[i] < a[i + 1]:
            dp[i] = max(dp[i], 1 + dp[i + 1])
            max_length = max(max_length, dp[i])

    # Check for one change
    for i in range(n):
        if i > 0 and dp[i - 1] + 1 > dp[i]:
            max_length = max(max_length, 1 + dp[i - 1])
        if i < n - 1 and dp[i + 1] + 1 > dp[i]:
            max_length = max(max_length, 1 + dp[i + 1])

    return max_length


print(find_longest_subsegment(a))
