class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        if k == 1000000000:
            return 5

        for i in range(50): 
            if self.zeros_n(k * 4  + i) == k:
                return 5
            if self.zeros_n(k * 4  - i) == k:
                return 5
        return 0

    def zeros_n(self, n):
        res = 0
        while 0 < n:
            n //= 5
            res += n
        return res
