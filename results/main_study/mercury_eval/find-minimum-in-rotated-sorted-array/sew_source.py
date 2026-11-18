
class Solution:
    def  merge(self, array, left, middle, right, temp):
        i, j = left, middle + 1
        k = left

        while  i <= middle and  j <= right:
            if array[i] <= array[j]:
                temp[k] = array[i]
                i += 1
            else:
                temp[k] = array[j]
                j += 1
            k = k + 1

        while  i <= middle:
            temp[k] = array[i]
            i = i + 1
            k = k + 1

        while  j <= right:
            temp[k] = array[j]
            j = j + 1
            k = k + 1

        for i in range(left, 1 + right):
            array[i]=temp[i]
    def  mergeSort(self, array, left, right, temp):
        if right > left:
            middle=(left+right)//2
            self.mergeSort(array, left, middle, temp)
            self.mergeSort(array, 1 + middle, right, temp)
            self.merge(array, left, middle, right, temp)
    def  findMin(self, nums: List[int]) -> int:
        temp = [None] * len(nums)
        self.mergeSort(nums, 0, len(nums) - 1, temp)
        return  nums[0]  # Assuming the goal is to find the minimum value
