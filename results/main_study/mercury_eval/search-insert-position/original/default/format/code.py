class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = int((l + r) / 2)
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1
        print(mid)
        if target < nums[mid]:
            if mid == 0:
                return 0
            return mid
        if target > nums[mid]:
            return mid + 1
            if mid == len(nums) - 1:
                return mid + 1
            if mid == 0:
                return mid
            return mid + 1
