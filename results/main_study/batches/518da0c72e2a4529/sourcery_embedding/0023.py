class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        myMap1 = {}
        myMap2 = {}

        for num in nums1:
            if num not in myMap1:
                myMap1[num] = True
        retList = []
        for num in nums2:
            if num not in myMap2:
                myMap2[num] = True

        for key in myMap1.keys():
            if key in myMap2:
                retList.append(key)

        return retList

