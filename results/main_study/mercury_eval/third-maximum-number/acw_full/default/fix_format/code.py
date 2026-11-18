class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        if len(nums) < 3:
            return max(nums)

        i = 0
        maxi = float("-inf")
        initial = max(nums)
        while i < 3:
            if not nums:
                return initial
            ele = max(nums)
            nums.remove(ele)
            if ele == maxi:
                pass
            else:
                maxi = ele
                i += 1
        return maxi
