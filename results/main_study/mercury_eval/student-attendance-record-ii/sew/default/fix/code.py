class Solution:
    def checkRecord(self, n: int) -> int:
        dp = []
        for ___ in range(n):
            dp.append([[0 for _ in range(2)] for __ in range(3)])
        # dp[i][L in a row][A counts]
        mod=int(1e9) + 7
        dp[0][0][1]=1  # A
        dp[0][1][0]=1  # L
        dp[0][0][0]=1  # P
        for  i in  range(1, n):
            # Place A
            for L in range(3):
                dp[i][0][1] += dp[i - 1][L][0]
            dp[i][0][1] %= mod
            # Place L
            for L in range(1, 3):
                for A in range(2):
                    dp[i][L][A]+=dp[i-1][L-1][A]
                    dp[i][L][A]%=mod
            # Place P
            for L in range(3):
                for A in range(2):
                    dp[i][0][A]+=dp[i-1][L][A]
                    dp[i][0][A]%=mod
        ans=0
        for  L in  range(3):
            for A in range(2):
                ans += dp[n - 1][L][A]
                ans %= mod
        return ans