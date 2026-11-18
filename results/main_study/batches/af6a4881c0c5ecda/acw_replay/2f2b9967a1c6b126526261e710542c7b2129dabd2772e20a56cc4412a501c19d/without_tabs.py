class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        dp = [[0 for _ in range(1 + n2)]for _ in range(1 + n1)]
        for i in range(1 + n1):
            dp[i][0] = i
        for i in range(1 + n2):
            dp[0][i] = i

        for ind1 in range(1, 1 + n1):
            for ind2 in range(1, 1 + n2):
                if word1[ind1 - 1] == word2[ind2 - 1]:
                    dp[ind1][ind2] = dp[ind1 - 1][ind2 - 1]
                else:
                    insert = dp[ind1][ind2 - 1] + 1
                    delete = 1 + dp[ind1 - 1][ind2]
                    replace = dp[ind1 - 1][ind2 - 1] + 1
                    dp[ind1][ind2] = min(insert, min(delete, replace))
        return dp[n1][n2]
