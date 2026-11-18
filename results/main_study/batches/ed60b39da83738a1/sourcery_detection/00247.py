class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        k = next(
            (i for i in range(len(nums) - 2, -1, -1) if nums[i] < nums[i + 1]), -1
        )
        # If such index is found, find the largest index l > k such that nums[k] < nums[l].
        if k != -1:
            l = next((i for i in range(len(nums) - 1, k, -1) if nums[i] > nums[k]), -1)
            # Swap nums[k] and nums[l].
            nums[k], nums[l] = nums[l], nums[k]

        # Reverse the sub-array nums[k + 1:].
        left, right = k + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left + 1, right - 1
