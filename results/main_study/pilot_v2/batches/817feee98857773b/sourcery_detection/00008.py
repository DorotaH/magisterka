class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = next(
            (i - 1 for i in range(len(nums) - 1, 0, -1) if nums[i - 1] < nums[i]),
            -1,
        )
        if pivot == -1:  # reverse the list
            for i in range(len(nums) // 2):
                temp = nums[i]
                nums[i] = nums[len(nums) - i - 1]
                nums[len(nums) - i - 1] = temp
            return

        smallestIndex = None
        for i in range(len(nums) - 1, pivot, -1):
            if nums[i] > nums[pivot] and (
                smallestIndex is None or nums[i] < nums[smallestIndex]
            ):
                smallestIndex = i

        # swap pivot and smallestIndex
        temp = nums[pivot]
        nums[pivot] = nums[smallestIndex]
        nums[smallestIndex] = temp

        for i in range((len(nums) - pivot - 1) // 2):
            temp = nums[i + pivot + 1]
            nums[i + pivot + 1] = nums[len(nums) - i - 1]
            nums[len(nums) - i - 1] = temp

    def getPermutation(self, n: int, k: int) -> str:
        start = list(range(1, n + 1))
        for _ in range(k - 1):
            self.nextPermutation(start)

        return "".join([str(x) for x in start])
