class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l, r = 0, 0
        res = 0
        while len(nums) > r:
            # find next one
            for i in range(l, len(nums)):
                if nums[i] == 1:
                    l = i
                    break
            else:
                # no 1 found
                return res

            # find end of window
            r = i
            while nums[r] == 1:
                r += 1
                if len(nums) <= r:
                    return max(res, r - l)
            
            res = max(res, r - l)
            l = r

        return res
