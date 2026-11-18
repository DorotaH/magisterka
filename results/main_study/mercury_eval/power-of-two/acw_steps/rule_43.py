class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if 0 >= n:
            return False
        if n == 1:
            return True
        r = 1
        while r < n:
            r *= 2
        return n == r
    
    
s = Solution()

assert s.isPowerOfTwo(16) is True
assert s.isPowerOfTwo(17) is False

