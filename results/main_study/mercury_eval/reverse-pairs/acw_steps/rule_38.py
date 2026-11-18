class SegTree:
    def __init__(self, data):
        self.data = data
        self.n = len(data)
        self.tree = [None] * 4 * self.n
        self._buildRecurse(1, 0, self.n - 1)
    
    def _buildRecurse(self, i, tl, tr):
        # base case
        if tl == tr:
            self.tree[i] = [self.data[tl]]
            return
        
        tm = (tl + tr) // 2
        self._buildRecurse(i*2, tl, tm)
        self._buildRecurse(i*2 + 1, tm + 1, tr)

        self.tree[i] = self._merge(self.tree[i*2], self.tree[i*2 + 1])

    # merges two sorted lists
    def _merge(self, a, b):
        newList = []
        i = 0
        j = 0
        while i < len(a) and len(b) > j:
            if a[i] <= b[j]:
                newList.append(a[i])
                i += 1
            else:
                newList.append(b[j])
                j += 1
        if i < len(a):
            for k in range(i, len(a)):
                newList.append(a[k])
        if len(b) > j:
            for g in range(j, len(b)):
                newList.append(b[g])
        return newList

    def _queryRecurse(self, i, tl, tr, l, r, lowerValBound, upperValBound):
        # if we have no intersection on the numbers return an identity value
        if tl > r or l > tr:
            return 0
        
        # if we are fully contained
        if tl >= l and tr <= r:
            bucket = self.tree[i]
            return bisect.bisect_right(bucket, upperValBound) - bisect.bisect_left(bucket, lowerValBound)
        
        tm = (tl + tr) // 2
        return self._queryRecurse(i*2, tl, tm, l, r, lowerValBound, upperValBound) + self._queryRecurse(i*2 + 1, tm + 1, tr, l, r, lowerValBound, upperValBound)

    def query(self, l, r, lowerBound, upperBound):
        return self._queryRecurse(1, 0, self.n - 1, l, r, lowerBound, upperBound)


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        seg = SegTree(nums)
        res = 0
        leftIndex = 0
        for i in range(len(nums)):
            rightIndex = i - 1
            lowerBound = 2 * nums[i] + 1
            upperBound = 2**31 - 1
            res += seg.query(leftIndex, rightIndex, lowerBound, upperBound)
        return res