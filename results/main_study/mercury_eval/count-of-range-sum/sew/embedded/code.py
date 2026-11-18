import  array
class  Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        """
        Use pref_sum array.
        O(n**2) solutions: list/array + insort
        O(n log n) solutions: SortedList (very easy to use in python)
        PLEASE ADD: FENWICK TREE
        """
        def  my_bisect_left(nums, val):
            if len(nums) == 0:
                return 0
            l, r = 0, len(nums)
            while  r > l:
                mid=(l + r)//2
                if not nums[mid] < val:
                    r = mid
                else:
                    l = mid + 1
            return  l 

        n=len(nums)
        pref_sum=[0]*(1 + n)
        for  i in  range(0, n):
            pref_sum[1 + i]=nums[i]+pref_sum[i]
        ans, pref_sum_sorted = 0, array.array('l')
        for  s in  pref_sum:
            l, r = my_bisect_left(pref_sum_sorted, s - upper), my_bisect_left(pref_sum_sorted, s - lower + 1)
            ans+=r-l
            idx=my_bisect_left(pref_sum_sorted, s)
            pref_sum_sorted.insert(idx, s)
        return  ans