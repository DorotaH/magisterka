class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = {}

        def doer(i, buy, trans, k):
            if i >= len(prices) or trans > k:
                return 0
            if (i, buy, trans) in dp:
                return dp[(i, buy, trans)]
            c = doer(i + 1, buy, trans, k)
            if buy:
                b = doer(i + 1, not buy, trans + 1, k) - prices[i]
                dp[(i, buy, trans)] = max(b, c)
            else:
                s = doer(i + 1, not buy, trans, k) + prices[i]
                dp[i, buy, trans] = max(s, c)
            return dp[(i, buy, trans)]

        p = doer(0, True, 0, k)
        return p
