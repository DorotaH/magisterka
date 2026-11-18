class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out = []
        index = 0
        for n in nums:
            want, dp = target - n, list(nums)
            dp.remove(n)
            m = set(dp)
            if want not in m:
                index += 1
                continue
            out.append(index)
            index = index + 1

        return out
