class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        if n==1:
            return True
        r = 1
        while n>r:
            r *= 2
        if n==r:
            return True
        return False


s = Solution()

assert s.isPowerOfTwo(16) is True
assert s.isPowerOfTwo(17) is False

