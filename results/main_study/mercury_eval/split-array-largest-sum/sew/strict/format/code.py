class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        length = len(nums)

        prefix_sums = [0] * (1 + length)
        for i in range(1, length + 1):
            prefix_sums[i] = prefix_sums[i - 1] + nums[i - 1]

        dp = [[0] * (k + 1) for _ in range(length + 1)]

        for i in range(1, length + 1):
            dp[i][1] = prefix_sums[i]

        for sub_arrays_needed in range(2, k + 1):
            for i in range(1, length + 1):
                dp[i][sub_arrays_needed] = math.inf
                for j in range(sub_arrays_needed - 1, i):
                    local_sum = prefix_sums[i] - prefix_sums[j]
                    dp[i][sub_arrays_needed] = min(
                        dp[i][sub_arrays_needed],
                        max(local_sum, dp[j][sub_arrays_needed - 1]),
                    )

        return dp[length][k]
