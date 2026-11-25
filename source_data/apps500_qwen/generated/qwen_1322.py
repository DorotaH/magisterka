MOD = 998244353

def count_good_arrays(n, k, a):
    # Initialize the DP table
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    
    # Iterate through each position in the array
    for i in range(1, n + 1):
        for j in range(k + 1):
            if a[i - 1] == -1:
                # If the current element is -1, we can replace it with any number from 1 to k
                dp[i][j] = (dp[i - 1][j] * k) % MOD
            else:
                # If the current element is not -1, it must match the corresponding element in the original array
                dp[i][j] = dp[i - 1][j - 1] if j > 0 else 0
    
    # The result is the number of good arrays ending at position n
    return dp[n][0]

# Read input
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
k = int(data[1])
a = list(map(int, data[2:]))

# Output the result
print(count_good_arrays(n, k, a))
