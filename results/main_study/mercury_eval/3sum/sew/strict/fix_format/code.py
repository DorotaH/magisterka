class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def twoSum(i, target):
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < target:
                    l = l + 1
                elif nums[l] + nums[r] > target:
                    r = r - 1
                else:
                    temp = [-target, nums[l], nums[r]]
                    temp.sort()
                    if temp not in res:
                        res.append(temp)
                    l += 1
                    while l < len(nums) and nums[l] == nums[l - 1]:
                        l = l + 1
                    r -= 1
                    while r >= 0 and nums[r] == nums[r + 1]:
                        r = r - 1

        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break
            twoSum(i, -nums[i])

        return res
