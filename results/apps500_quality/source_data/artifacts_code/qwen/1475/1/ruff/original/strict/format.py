MOD = 10**9 + 7


def count_ways(n, b, k, x, digits):
    dp = [0] * x
    dp[0] = 1

    for digit in digits:
        new_dp = [0] * x
        for i in range(x):
            for j in range(n):
                if (i * 10 + j) % x == k:
                    new_dp[i] = (new_dp[i] + dp[j]) % MOD
        dp = new_dp

    return dp[0]


# Read input
import sys

input = sys.stdin.read
data = input().split()
n = int(data[0])
b = int(data[1])
k = int(data[2])
x = int(data[3])
digits = list(map(int, data[4:]))

# Calculate and print the result
result = count_ways(n, b, k, x, digits)
print(result)
