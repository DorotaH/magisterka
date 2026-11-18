class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def twoSum(i, target):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[r] + nums[l] < target:
                    l += 1
                elif nums[r] + nums[l] > target:
                    r -= 1
                else:
                    temp = [-target, nums[l], nums[r]]
                    temp.sort()
                    if temp not in res:
                        res.append(temp)
                    l += 1
                    while l < len(nums) and nums[l] == nums[l - 1]:
                        l += 1
                    r -= 1
                    while 0 <= r and nums[r] == nums[1 + r]:
                        r -= 1

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break
            twoSum(i, -nums[i])

        return res
