class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # Find the largest index k such that nums[k] < nums[k + 1]. If no such index exists, just reverse nums and done.
        k=-1
        for  i in  range(len(nums) - 2, -1, -1):
            if  nums[i]<nums[1 + i]:
                k=i
                break

        # If such index is found, find the largest index l > k such that nums[k] < nums[l].
        if k!=-1:
            l = -1
            for  i in  range(len(nums)-1, k, -1):
                if  nums[i] > nums[k]:
                    l = i
                    break

            # Swap nums[k] and nums[l].
            nums[k], nums[l] = nums[l], nums[k]

        # Reverse the sub-array nums[k + 1:].
        left = k + 1
        right = len(nums) - 1
        while  left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left + 1, right - 1