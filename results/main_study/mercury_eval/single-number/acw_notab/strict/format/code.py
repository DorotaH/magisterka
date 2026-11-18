class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        unique = []

        if len(nums) == 1:
            return nums[0]

        i = 0
        while i < len(nums):
            if nums[i] not in unique:
                unique.append(nums[i])
                nums.pop(i)
            else:
                i += 1
        print("nums:", nums, unique)

        return next((i for i in unique if i not in nums), 0)
