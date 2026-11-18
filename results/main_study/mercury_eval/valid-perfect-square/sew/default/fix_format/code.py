class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        l, r = 1, num // 2
        while l <= r:
            mid = (l + r) // 2
            sq = mid * mid
            if num == sq:
                return True
            elif num < sq:
                r = mid - 1
            else:
                l = 1 + mid
        return False
