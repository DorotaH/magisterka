from sys import stdin, stdout
from collections import defaultdict

MOD = 998244353


def main():
    reader = stdin.read
    data = reader().split()

    K = int(data[0])
    N = int(data[1])

    # dp[i][j] is the number of ways to get sum i with j dice
    dp = []
    for _ in range(N + 1):
        dp.append([0] * (K + 1))
    dp[0][0] = 1

    for i in range(1, 1 + N):
        for j in range(1, K + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
            dp[i][j] %= MOD

    # count[i] is the number of combinations of N sides such that the sum of no two different sides is i
    count = [0] * (2 * K + 1)

    for i in range(1, 1 + K):
        count[i + 1] = dp[N][i]
        count[i + 1] %= MOD

    for i in range(2 + K, 1 + 2 * K):
        count[i] = dp[N][K]
        count[i] %= MOD

    # Output the result
    for i in range(1, 2 * K):
        stdout.write(str(count[i + 1]) + "\n")


if __name__ == "__main__":
    main()
