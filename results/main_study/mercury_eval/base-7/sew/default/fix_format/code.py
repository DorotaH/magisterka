class Solution:
    def convertToBase7(self, num: int) -> str:
        t = ""
        q, f = num, False
        if q == 0:
            return "0"
        if num < 0:
            f = True
            num *= -1
        while num > 0:
            k = str(num % 7)
            t = t + k
            num //= 7
        if f == True:
            return "-" + str(t[::-1])
        else:
            return str(t[::-1])
