import array


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        """
        Use pref_sum array.
        O(n**2) solutions: list/array + insort
        O(n log n) solutions: SortedList (very easy to use in python)
        PLEASE ADD: FENWICK TREE
        """

        def my_bisect_left(nums, val):
            if len(nums) == 0:
                return 0
            l, r = 0, len(nums)
            while l < r:
                mid = (l + r) // 2
                if nums[mid] < val:
                    l = mid + 1
                else:
                    r = mid
            return l

        n = len(nums)
        pref_sum = [0] * (n + 1)
        for i in range(n):
            pref_sum[i + 1] = nums[i] + pref_sum[i]
        ans = 0
        pref_sum_sorted = array.array("l")
        for s in pref_sum:
            l = my_bisect_left(pref_sum_sorted, s - upper)
            r = my_bisect_left(pref_sum_sorted, s - lower + 1)
            ans += r - l
            idx = my_bisect_left(pref_sum_sorted, s)
            pref_sum_sorted.insert(idx, s)
        return ans
