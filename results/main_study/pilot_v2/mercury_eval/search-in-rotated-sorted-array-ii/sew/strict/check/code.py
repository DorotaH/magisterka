class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low, high = 0, len(nums) - 1
        while  high >= low:
            mid=(low + high)//2
            if  target == nums[mid]:
                return True
            if  nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
            #left half is sorted
            elif  nums[low] <= nums[mid]:
                if not (nums[low] <= target and target <= nums[mid]):
                    low = mid + 1
                else:
                    high = mid - 1
            #right half is sorted
            elif  nums[mid] <= nums[high]:
                if not (nums[high] >= target and target >= nums[mid]):
                    high = mid - 1
                else:
                    low = mid + 1
        return  False
