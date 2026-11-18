class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # use divide and conque to
        def helper(left, right, nums):
            if left == right:
                return nums[left]
            mid = left + (right - left) // 2
            leftM = helper(left, mid, nums)
            rightM = helper(mid + 1, right, nums)
            if leftM == rightM:
                return leftM
            leftcounter = 0
            rightcounter = 0
            for i in range(left, right + 1):
                if nums[i] == leftM:
                    leftcounter += 1
                elif nums[i] == rightM:
                    rightcounter += 1
            if leftcounter > rightcounter:
                return leftM
            return rightM

        return helper(0, len(nums) - 1, nums)
