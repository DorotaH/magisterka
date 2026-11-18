class Solution:
    def trailingZeroes(self, n: int) -> int:
        def countdivisors(val: int, divisor: int) -> int:
            ctr = 0
            while val > 1:
                if val % divisor == 0:
                    ctr += 1
                    val //= divisor
                else:
                    break
            return ctr
        if n == 0 or n == 1:
            return 0
        else:
            ref = {2: 0, 5: 0}
            for i in range(1, n+1):
                ref[2] += countdivisors(i, 2)
                ref[5] += countdivisors(i, 5)
            return min(ref[2], ref[5])
