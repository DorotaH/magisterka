class Solution:
    def list_dict(self, nums: List[int]) -> dict:
        res = {}
        for a in nums:
            res[a] = 1 + res.get(a, 0)
        return res

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = list()
        num1 = self.list_dict(nums1)
        num2 = self.list_dict(nums2)
        start, end = (num2, num1) if len(num1) > len(num2) else (num1, num2)
        for key, value in start.items():
            if key in end.keys():
                res.extend(key for _ in range(0, min(value, end[key])))
        return res

