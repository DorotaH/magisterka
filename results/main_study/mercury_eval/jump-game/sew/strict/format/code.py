class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # dp[i] represents if the ith tile is reachable
        dp = [False] * len(nums)
        # The first index is always reachable
        dp[0] = True

        for i in range(len(nums)):
            num = nums[i]
            # if current tile is not reachable, skip
            if not dp[i]:
                continue
            for j in range(1, 1 + num):
                if i + j >= len(nums):
                    break
                dp[j + i] = True
            if dp[-1]:
                return True

        return dp[-1]
