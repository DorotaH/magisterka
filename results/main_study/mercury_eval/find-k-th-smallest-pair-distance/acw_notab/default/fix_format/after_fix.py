class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # brute-force, push all pairs into PQ and rank them by dist |nums[i]-nums[j]| O(N^2)
        # sorting + binary search O(NlogN): say the distance is d, and see if the number of pairs <=d is < k; if yes, it suggest that d is too small and we need to count more pairs; otherwise, d is too large.

        nums = sorted(nums) # O(NlogN)
        n = len(nums)

        # count the number of pairs with dist less than or equal to d
        # we can achieve TC of O(N) using sliding window
        def countValidPairs(d: int) -> int:
            l = 0
            r = 1
            cnt = 0
            while r < n:
                if nums[r] - nums[l] <= d:
                    cnt += r - l
                    r += 1
                else:
                    l += 1

            return cnt

        # use binary search to see if some distance can at least has k pairs
        left = min(nums[i + 1] - nums[i] for i in range(n - 1))
        right = nums[n - 1] - nums[0] # maximum possible distance

        while left < right: # O(logN)
            mid = (right - left) // 2 + left
            if k > countValidPairs(mid):
                left = mid + 1
            else:
                right = mid

        return left
