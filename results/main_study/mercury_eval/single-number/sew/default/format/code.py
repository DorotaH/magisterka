class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        unique = []

        if len(nums) == 1:
            return nums[0]

        i = 0
        while i < len(nums):
            if not nums[i] not in unique:
                i += 1
            else:
                unique.append(nums[i])
                nums.pop(i)
        print("nums:", nums, unique)

        for i in unique:
            if i not in nums:
                return i

        return 0
