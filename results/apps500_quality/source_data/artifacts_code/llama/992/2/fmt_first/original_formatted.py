from sys import stdin, stdout

MOD = 998244353


def read_ints():
    return map(int, stdin.readline().split())


def main():
    N, S = read_ints()
    A = list(read_ints())
    A = [0] + A  # Adjusting A to be 1-indexed

    # Create a dynamic programming table to store the number of ways to sum up to each possible value
    dp = [0] * (S + 1)
    dp[0] = 1

    for i in range(1, N + 1):
        for j in range(S, A[i], -1):
            dp[j] = (dp[j] + dp[j - A[i]]) % MOD

    # Calculate the sum of f(T) over all 2^N-1 subsets T of {1, 2, ..., N}
    ans = 0
    for i in range(1, 2**N):
        subset_sum = 0
        for j in range(1, N + 1):
            if (i >> (N - j)) & 1:
                subset_sum += A[j]
        ans = (ans + dp[subset_sum]) % MOD

    stdout.write(str(ans))


if __name__ == "__main__":
    main()
