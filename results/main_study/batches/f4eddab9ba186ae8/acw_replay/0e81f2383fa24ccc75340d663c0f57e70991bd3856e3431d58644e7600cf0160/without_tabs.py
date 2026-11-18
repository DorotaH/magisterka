class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #1st method

        # n = len(nums)
        # result = []

        # def backtrack(first=0):
        #     # print("Before",first)
        #     if first == n:
        #         # print("after",first)
        #         result.append(nums[:])  # Copy the current permutation
        #         # print(result)
        #     for i in range(first, n):
        #         # Swap the elements at indices first and i
        #         nums[first], nums[i] = nums[i], nums[first]
        #         backtrack(first + 1)  # Recursive call for the rest of the elements
        #         nums[first], nums[i] = nums[i], nums[first]  # Backtrack (swap back)

        # backtrack()
        # return result

        #2nd Method
        # def backtrack(start):
        #     if start == len(nums):
        #         res.append(nums[:])
        #     for i in range(start, len(nums)):
        #         nums[start], nums[i] = nums[i], nums[start]  # Swap elements
        #         backtrack(start + 1)  # Recursive call
        #         nums[start], nums[i] = nums[i], nums[start]  # Backtrack (restore original order)

        # res = []
        # backtrack(0)
        # return res

        def backtrack(curr_nums):
            if len(curr_nums) == len(nums):
                res.append(curr_nums[:])
                return
            for num in nums:
                if num in curr_nums:
                    continue
                curr_nums.append(num)
                backtrack(curr_nums)
                curr_nums.pop()
        res = []
        backtrack([])
        return res




