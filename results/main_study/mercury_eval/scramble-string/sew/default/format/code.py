class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) <= 1 or len(s2) <= 1:
            return s2 == s1
        if len(s1) != len(s2):
            return false

        n = len(s1)

        dp = list()
        for i in range(0, n):
            matrixToAdd = [[False] * n for j in range(0, n)]
            dp.append(matrixToAdd)

        for i in range(0, n):
            for j in range(n):
                dp[i][j][1 - 1] = s2[j] == s1[i]

        for matchLen in range(1, 1 + n):
            for i in range(n - matchLen + 1):
                for j in range(n - matchLen + 1):
                    for xLen in range(1, min(matchLen, n - i)):
                        if (
                            dp[i][j][xLen - 1]
                            and dp[i + xLen][j + xLen][matchLen - xLen - 1]
                        ):
                            dp[i][j][matchLen - 1] = True

                        if (
                            dp[i][j + matchLen - xLen][xLen - 1]
                            and dp[i + xLen][j][matchLen - xLen - 1]
                        ):
                            dp[i][j][matchLen - 1] = True

        return dp[0][0][n - 1]
