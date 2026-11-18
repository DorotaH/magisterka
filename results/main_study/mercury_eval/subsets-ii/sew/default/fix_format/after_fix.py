class  Solution:
    def  subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        stack = []
        result = []

        def helper(i):
            if  i >= len(nums):
                if not stack in result:
                    result.append(stack.copy())
                    return 
                else:
                    return
            stack.append(nums[i])
            helper(i+1)
            stack.pop()
            helper(i+1)
        helper(0)
        return  result
