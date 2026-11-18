class SegTree:
    def __init__(self, n):
        self.n = n
        self.tree = 4 * [None] * self.n
        self.lazy = [0] * len(self.tree)
        self._build(1, 0, self.n - 1)

    def _build(self, i, tl, tr):
        if tl == tr:
            self.tree[i] = 0
            return
        # build left and right
        tm = (tr + tl) // 2
        self._build(2 * i, tl, tm)
        self._build(1 + 2 * i, 1 + tm, tr)

        self.tree[i] = max(self.tree[2 * i], self.tree[1 + 2 * i])

    def _queryMaxRecurse(self, i, tl, tr, l, r):
        # no intersection
        if r < tl or tr < l:
            return float("-inf")  # identity

        if self.lazy[i] != 0:
            self.tree[i] = self.lazy[i]
            # push down if needed
            if tr != tl:
                self.lazy[2 * i] = self.lazy[i]
                self.lazy[1 + 2 * i] = self.lazy[i]
            # clear the lazy
            self.lazy[i] = 0

        # fully contained
        if l <= tl and tr <= r:
            return self.tree[i]

        tm = (tr + tl) // 2
        # check left and right
        leftRes, rightRes = (
            self._queryMaxRecurse(2 * i, tl, tm, l, r),
            self._queryMaxRecurse(2 * i + 1, tm + 1, tr, l, r),
        )
        return max(leftRes, rightRes)

    def _updateRangeRecurse(self, i, tl, tr, l, r, newVal):
        # no intersection, this can go below too
        if tr < l or r < tl:
            return

        # if we are lazy, update our current value and push
        if self.lazy[i]:
            self.tree[i] = self.lazy[i]
            # push down if we have children
            if tr != tl:
                self.lazy[2 * i] = self.lazy[i]
                self.lazy[1 + 2 * i] = self.lazy[i]

            self.lazy[i] = 0  # clear the lazy

        # fully contained
        if l <= tl and tr <= r:
            self.tree[i] = (
                newVal  # update the segment, after all the new max for the segment is the entire value we set
            )
            if tr != tl:
                # push the assignment down to future children, after all that granularity isn't needed yet
                self.lazy[2 * i] = newVal
                self.lazy[1 + 2 * i] = newVal
            return

        tm = (tr + tl) // 2

        # we need to recurse deeper if we aren't fully contained, though during our descent we at least applied lazys that were needed for the first time now
        self._updateRangeRecurse(2 * i, tl, tm, l, r, newVal)
        self._updateRangeRecurse(1 + 2 * i, 1 + tm, tr, l, r, newVal)

        self.tree[i] = max(self.tree[2 * i], self.tree[1 + 2 * i])

    ### PUBLIC METHODS

    def queryMax(self, l, r):
        return self._queryMaxRecurse(1, 0, self.n - 1, l, r)

    def assignRangeToValue(self, l, r, newMax):
        self._updateRangeRecurse(1, 0, self.n - 1, l, r, newMax)


class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        coords = set()
        for leftSide, sideLength in positions:
            coords.add(leftSide)
            coords.add(leftSide + sideLength)
        compressed = sorted(list(coords))
        valToIndex = {val: i for i, val in enumerate(compressed)}

        seg, res = SegTree(len(compressed)), []
        for left, sidelength in positions:
            leftCompressed = valToIndex[left]
            sidelengthCompressed = valToIndex[left + sidelength]
            # first find the max in the region we are dropping
            maxInRegion = seg.queryMax(
                leftCompressed, sidelengthCompressed - 1
            )  # exclusive range
            # now assign the new height
            seg.assignRangeToValue(
                leftCompressed, sidelengthCompressed - 1, maxInRegion + sidelength
            )
            # now determine the new max anywhere
            res.append(seg.queryMax(0, len(compressed) - 1))

        return res
