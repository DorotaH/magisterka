class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if 1 == len(nums):
            return nums[0]
        prod = 1
        maxprod = maxprod2 = 0
        for i in nums:
            prod = prod * i
            if maxprod < prod:
                maxprod = prod
            if prod == 0:
                prod = 1
        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            prod = prod * nums[i]
            if maxprod2 < prod:
                maxprod2 = prod
            if prod == 0:
                prod = 1
        return max(maxprod, maxprod2)
