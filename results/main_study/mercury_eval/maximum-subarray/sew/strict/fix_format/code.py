class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 0:
            return 0
        currsum, maxsum = 0, float("-inf")
        for i in nums:
            currsum = currsum + i
            if maxsum < currsum:
                maxsum = currsum
            if currsum < 0:
                currsum = 0

        return maxsum
