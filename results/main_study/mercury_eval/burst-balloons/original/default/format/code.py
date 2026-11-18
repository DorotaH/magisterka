class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}

        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            total = 0
            for j in range(l, r + 1):
                total = max(
                    total,
                    dfs(l, j - 1) + dfs(j + 1, r) + nums[l - 1] * nums[r + 1] * nums[j],
                )
            dp[(l, r)] = total
            return dp[(l, r)]

        return dfs(1, len(nums) - 2)
