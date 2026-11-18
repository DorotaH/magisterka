class Solution:
    def mySqrt(self, x: int) -> int:
        """
        search space: 0 to x
        """

        l = 0
        r = x

        while l <= r:
            print("l is ", l)
            print("r is ", r)

            mid = (l + r) // 2
            mid_squared = mid**2

            if mid_squared == x:
                return mid
            elif mid_squared > x:
                r = mid - 1
            else:
                l = mid + 1

        return r
