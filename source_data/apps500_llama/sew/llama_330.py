a, b = input().strip(), input().strip()

def  longest_uncommon_subsequence(a, b):
    def lcs_length(a, b):
        m, n = len(a), len(b)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(0, m + 1):
            for  j in  range(n + 1):
                if  0 == i or  0 == j:
                    dp[i][j] = 0
                elif  b[j - 1] == a[i - 1]:
                    dp[i][j]=1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[m][n]

    lcs_ab, lcs_ba = lcs_length(a, b), lcs_length(b, a)

    if not (lcs_ab == lcs_ba and lcs_ab == max(len(a), len(b))):
        return max(len(a), len(b))
    else:
        return -1

print(longest_uncommon_subsequence(a, b))
