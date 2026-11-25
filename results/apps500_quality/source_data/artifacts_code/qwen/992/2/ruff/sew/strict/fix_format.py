import sys

MOD = 998244353


def main():
    input = sys.stdin.read
    data = input().split()

    N = int(data[0])
    S, A = int(data[1]), list(map(int, data[2:]))

    # dp[i][j] is the number of ways to get sum j using the first i elements
    dp = [[0] * (S + 1) for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(1, N + 1):
        for j in range(0, S + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= A[i - 1]:
                dp[i][j] += dp[i - 1][j - A[i - 1]]
                dp[i][j] %= MOD

    # The answer is the sum of dp[N][j] for all j from 1 to S
    answer = sum(dp[N][j] for j in range(1, 1 + S)) % MOD

    print(answer)


if __name__ == "__main__":
    main()
