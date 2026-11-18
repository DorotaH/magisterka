class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        stack = []
        result = []
        def helper(i):
            if i >= len(nums):
                if stack in result:
                    return
                result.append(stack.copy())
                return
            stack.append(nums[i])
            helper(i + 1)
            stack.pop()
            helper(i + 1)

        helper(0)
        return result