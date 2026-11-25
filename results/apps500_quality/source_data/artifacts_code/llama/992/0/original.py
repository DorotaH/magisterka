MOD = 998244353

def solve():
    n, s = map(int, input().split())
    a = list(map(int, input().split()))

    # Count the occurrences of each number in the array
    count = [0] * (s + 1)
    for x in a:
        count[x] += 1

    # Initialize dp table
    dp = [[0] * (s + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    # Fill the dp table using dynamic programming
    for i in range(1, n + 1):
        for j in range(s + 1):
            dp[i][j] = dp[i - 1][j]
            if j - a[i - 1] >= 0:
                dp[i][j] += dp[i - 1][j - a[i - 1]]
                dp[i][j] %= MOD

    # Calculate the sum of f(T) over all subsets T
    total = 0
    for i in range(s + 1):
        total += dp[n][i]
        total %= MOD

    return total

if __name__ == "__main__":
    print(solve())
