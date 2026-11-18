class Solution:
    def  smallestDistancePair(self, nums: List[int], k: int) -> int:
        # brute-force, push all pairs into PQ and rank them by dist |nums[i]-nums[j]| O(N^2)
        # sorting + binary search O(NlogN): say the distance is d, and see if the number of pairs <=d is < k; if yes, it suggest that d is too small and we need to count more pairs; otherwise, d is too large.

        nums=sorted(nums) # O(NlogN)
        n=len(nums)

        # count the number of pairs with dist less than or equal to d
        # we can achieve TC of O(N) using sliding window
        def countValidPairs(d: int) -> int:
            l=0
            r, cnt = 1, 0
            while  n > r:
                if not nums[r] - nums[l] <= d:
                    l += 1
                else:
                    cnt += r - l
                    r += 1

            return  cnt

        # use binary search to see if some distance can at least has k pairs
        left=min([nums[1+i]-nums[i] for i in range(n-1)]) # minimum possible distance
        right=nums[n-1]-nums[0] # maximum possible distance

        while  right > left: # O(logN)
            mid = left + (right-left) // 2
            if not countValidPairs(mid) < k:
                right = mid
            else:
                left = mid + 1

        return  left
