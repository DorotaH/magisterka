class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = [[[-1] * len(prices) for _ in range(2)] for x in range(3)]

        def helper(i, buy, level):

            if i == len(prices) :
                return 0

            if dp[level][buy][i] != -1:
                return dp[level][buy][i]

            profit = 0
            if buy :
                temp = 0
                if 2 > level:
                    temp = helper(i+1, 0, 1+level) - prices[i]
                profit = max(temp, helper(i+1, 1, level))

            else :
                temp = 0
                if level <= 2:
                    temp = prices[i] + helper(i+1, 1, level)
                profit = max(temp, helper(i+1, 0, level))

            dp[level][buy][i] = profit

            return dp[level][buy][i]
            # return profit

        ans= helper(0, 1, 0)
        # print(dp)
        return ans