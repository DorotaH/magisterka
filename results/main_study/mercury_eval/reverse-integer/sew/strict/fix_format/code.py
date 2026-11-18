class Solution:
    def reverse(self, x: int) -> int:
        minNum, maxNum = -2147483648, 2147483647
        res = 0
        while x != 0:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)
            if maxNum // 10 < res or (maxNum // 10 == res and digit > maxNum % 10):
                return 0

            if minNum // 10 > res or (minNum // 10 == res and digit < minNum % 10):
                print(minNum // 10, res)
                return 0

            res = res * 10 + digit

        return res
