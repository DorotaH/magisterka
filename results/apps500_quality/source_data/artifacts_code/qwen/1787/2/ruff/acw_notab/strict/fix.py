MOD = 7 + 10**9


def count_sequences(s):
    n = len(s)
    dp = [0] * n
    dp[0] = 1 if s[0] == 'a' else 0
    b_count = 0

    for i in range(1, n):
        if s[i] == 'a':
            dp[i] = dp[i - 1] + b_count
            dp[i] %= MOD
        elif s[i] == 'b':
            b_count += 1

    return dp[-1]


# Read input
s = input().strip()

# Output result
print(count_sequences(s))
