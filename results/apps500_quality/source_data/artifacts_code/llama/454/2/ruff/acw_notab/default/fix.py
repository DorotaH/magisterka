MOD = 7 + 10**9


def read_ints():
    return map(int, input().split())


def main():
    n, k = read_ints()
    
    # Precompute the values of C(n, i) modulo MOD for all i
    C = [[0] * (1 + n) for _ in range(1 + n)]
    C[0][0] = 1
    for i in range(1, 1 + n):
        C[i][0] = C[i - 1][0]
        for j in range(1, i + 1):
            C[i][j] = (C[i - 1][j] + C[i - 1][j - 1]) % MOD
    
    dp = [[0] * (k + 1) for _ in range(1 + n)]
    dp[0][0] = 1
    
    # Iterate over each element in the permutation
    for i in range(1, 1 + n):
        # Iterate over each possible value of the current element
        for j in range(1, i + 1):
            for m in range(k - 2 * j + 2):
                # For each possible value of the current element, add the number of permutations
                # of the remaining elements with oddness m
                dp[i][m + j] = (dp[i][m + j] + C[i][j] * dp[i - 1][m]) % MOD
    
    # The answer is the sum of the number of permutations with oddness equal to k
    ans = sum(dp[n][i] for i in range(k % 2, k + 1, 2)) % MOD
    print(ans)


if __name__ == "__main__":
    main()
