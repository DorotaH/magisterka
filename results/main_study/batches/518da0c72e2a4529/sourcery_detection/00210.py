class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        [1, 2, 2, 3, 0, 1]

        """

        if len(nums) == 1 or nums[-1] > nums[0]:
            return nums[0]

        left = 0
        right = len(nums) - 1

        while left + 1 < right:
            if nums[right] > nums[left]:
                return nums[left]
            elif nums[right] < nums[left]:
                mid = (left + right) // 2
                if nums[mid] >= nums[left]:
                    left = mid
                else:
                    right = mid
            else:
                left += 1

        return min(nums[left], nums[right])
