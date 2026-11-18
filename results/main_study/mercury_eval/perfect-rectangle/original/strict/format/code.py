class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        freq = {}
        minx1 = float("inf")
        miny1 = float("inf")
        maxx2 = float("-inf")
        maxy2 = float("-inf")
        res = 0
        for x1, y1, x2, y2 in rectangles:
            p1 = (x1, y1)
            p2 = (x2, y2)
            p3 = (x1, y2)
            p4 = (x2, y1)
            freq[p1] = freq.get(p1, 0) + 1
            freq[p2] = freq.get(p2, 0) + 1
            freq[p3] = freq.get(p3, 0) + 1
            freq[p4] = freq.get(p4, 0) + 1
            area = (x2 - x1) * (y2 - y1)
            res += area
            if x1 <= minx1 and y1 <= miny1:
                minx1 = x1
                miny1 = y1
            if x2 >= maxx2 and y2 >= maxy2:
                maxx2 = x2
                maxy2 = y2

        # get points freq = 1
        points = []
        for k, v in freq.items():
            if v % 2 == 1:
                points.append(k)

        if len(points) != 4:
            return False
        # else:
        #     for p in points:
        #         if freq[p] != 1:
        #             return False

        largetRec = (maxx2 - minx1) * (maxy2 - miny1)
        if largetRec != res:
            return False

        for p in points:
            if (
                p != (minx1, miny1)
                and p != (maxx2, maxy2)
                and p != (minx1, maxy2)
                and p != (maxx2, miny1)
            ):
                return False
        return True
