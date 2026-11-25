def count_pairs(S):
    n = len(S)
    MOD = 2019
    dp = [0] * (1 + n)
    dp[0] = 1
    ans = 0

    for i in range(1, 1 + n):
        dp[i] = 10 * dp[i - 1]
        for j in range(1, min(9, i) + 1):
            dp[i] += dp[i - j]

    for i in range(1, 1 + n):
        for j in range(i, 1 + n):
            num = int(S[i - 1:j])
            if num % MOD == 0:
                ans += dp[j - i]

    return ans


S = input()
print(count_pairs(S))
