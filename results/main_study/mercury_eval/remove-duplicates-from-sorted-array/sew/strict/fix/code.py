class Solution:
    def  removeDuplicates(self, nums: List[int]) -> int:
       array = self.remove_duplicates(nums)
       len_array = len(array)
       print(len_array,'nums = ' ,array)
       return
    def  remove_duplicates(self,array)->list:
        l, r = 0, 1
        while  l < r and  r<len(array):
            if not array[l] != array[r]:
                array.remove(array[l])
            else:
                r += 1
                l += 1
        return array
