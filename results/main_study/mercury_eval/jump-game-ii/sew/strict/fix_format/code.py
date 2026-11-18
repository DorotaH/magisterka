class Solution:
    def jump(self, nums: List[int]) -> int:

        memo = {0: 0}

        def dp(i):
            if i == len(nums):
                return memo[i - 1] if i - 1 in memo else -1

            for j in range(1, nums[i] + 1):
                jump = j + i

                if jump not in memo:
                    memo[i + j] = 1 + memo[i]
                else:
                    memo[i + j] = min(memo[i + j], 1 + memo[i])

            return dp(1 + i)

        x = dp(0)
        return x

    # [ 1, 1,  ]
