
class Solution:
    def merge(self, array, left, middle, right, temp):
        i = left
        j = middle + 1
        k = left

        while i <= middle and j <= right:
            if array[i] <= array[j]:
                temp[k] = array[i]
                i += 1
            else:
                temp[k] = array[j]
                j += 1
            k += 1

        while i <= middle:
            temp[k] = array[i]
            i += 1
            k += 1

        while j <= right:
            temp[k] = array[j]
            j += 1
            k += 1

        for i in range(left, 1 + right):
            array[i] = temp[i]

    def mergeSort(self, array, left, right, temp):
        if left < right:
            middle = (left + right) // 2
            self.mergeSort(array, left, middle, temp)
            self.mergeSort(array, middle + 1, right, temp)
            self.merge(array, left, middle, right, temp)

    def findMin(self, nums: List[int]) -> int:
        temp = len(nums) * [None]
        self.mergeSort(nums, 0, len(nums) - 1, temp)
        return nums[0]  # Assuming the goal is to find the minimum value