class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if nums == []:
            return []

        dct = {}
        for el in nums:
            if el not in dct:
                dct[el] = 1
            else:
                dct[el] += 1

        fin = [key for key in dct if dct[key] > (len(nums) // 3)]

        return fin
