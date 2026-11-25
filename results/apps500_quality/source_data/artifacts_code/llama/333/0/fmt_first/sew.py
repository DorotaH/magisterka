def longest_uncommon_subsequence(a, b):
    def  longest_common_subsequence(a, b):
        m, n = len(a), len(b)
        dp = []
        for _ in range(m + 1):
            dp.append([0] * (n + 1))
        for  i in  range(1, 1 + m):
            for j in range(1, n + 1):
                if a[i - 1] == b[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return  dp[m][n]

    lcs=longest_common_subsequence(a, b)
    return max(len(a), len(b))-lcs if lcs<min(len(a), len(b)) else -1


a = input()
b = input()
print(longest_uncommon_subsequence(a, b))