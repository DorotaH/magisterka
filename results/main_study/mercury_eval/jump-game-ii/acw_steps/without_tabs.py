class Solution:
    def jump(self, nums: List[int]) -> int:

        memo = { 0 : 0 }

        def dp(i):
            if i == len(nums):
                return memo[i - 1] if i - 1 in memo else -1

            for j in range(1, nums[i] + 1):
                jump = i + j

                memo[i + j] = min(memo[i + j], 1 + memo[i]) if jump in memo else 1 + memo[i]
            return dp(i + 1)

        x = dp(0)
        return x


    #[ 1, 1,  ]
