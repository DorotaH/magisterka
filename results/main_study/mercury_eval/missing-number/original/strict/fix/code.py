class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        tru = list(range(len(nums)))

        if nums[-1] != len(nums):
            return len(nums)

        while len(nums) > 1:
            i = len(nums)//2
            if nums[i//2] != tru[i//2]:
                nums = nums[:i//2+1]
                tru = tru[:i//2+1]
            else:
                nums = nums[i//2+1:]
                tru = tru[i//2+1:]

        return nums[0]-1
