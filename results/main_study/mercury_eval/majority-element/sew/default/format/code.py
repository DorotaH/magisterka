class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # use divide and conque to
        def helper(left, right, nums):
            if left == right:
                return nums[left]
            mid = left + (right - left) // 2
            leftM, rightM = helper(left, mid, nums), helper(mid + 1, right, nums)
            if leftM == rightM:
                return leftM
            leftcounter = rightcounter = 0
            for i in range(left, 1 + right):
                if nums[i] == leftM:
                    leftcounter += 1
                elif rightM == nums[i]:
                    rightcounter = rightcounter + 1
            if rightcounter < leftcounter:
                return leftM
            return rightM

        return helper(0, len(nums) - 1, nums)
