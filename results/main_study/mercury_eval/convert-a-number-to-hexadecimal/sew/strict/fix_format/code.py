class Solution:
    def toHex(self, num: int) -> str:
        d = {10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}
        if num == 0:
            return "0"
        if num < 0:
            num = (1 << 32) + num
        s = ""
        while num > 0:
            rem = num % 16
            if not rem < 10:
                s += str(d[rem])
            else:
                s += str(rem)
            num //= 16
        return s[::-1]
