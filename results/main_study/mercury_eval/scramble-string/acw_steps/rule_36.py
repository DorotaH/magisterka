class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) <= 1 or len(s2) <= 1: return s1 == s2
        if len(s1) != len(s2): return false

        n = len(s1)

        dp = []
        for _ in range(n):
            matrixToAdd = [[False] * n for _ in range(n)]
            dp.append(matrixToAdd)


        for i in range(n):
            for j in range(n):
                dp[i][j][1-1] = s1[i] == s2[j]

        for matchLen in range(1, 1+n):
            for i in range(n-matchLen+1):
                for j in range(n-matchLen+1):
                    for xLen in range(1, min(matchLen, n - i)):
                        if dp[i][j][xLen-1] and dp[i+xLen][xLen+j][matchLen - xLen - 1]:
                            dp[i][j][matchLen-1] = True

                        if dp[i][matchLen+j-xLen][xLen-1] and dp[i+xLen][j][matchLen-xLen-1]:
                            dp[i][j][matchLen-1] = True

        return dp[0][0][n-1]