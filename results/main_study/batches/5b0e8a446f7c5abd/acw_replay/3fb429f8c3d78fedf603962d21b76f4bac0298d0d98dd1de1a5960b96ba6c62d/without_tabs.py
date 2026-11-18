class Solution:
    def reverse(self, x: int) -> int:
        minNum  = -2147483648
        maxNum = 2147483647
        res = 0   
        while (x != 0):
            digit = int(math.fmod(x, 10))
            x = int(x / 10)
            if (res > maxNum // 10 or (maxNum // 10 == res and maxNum % 10 < digit)):
                return 0

            if (minNum // 10 > res or (minNum // 10 == res and minNum % 10 > digit)):
                print(minNum // 10, res)
                return 0
            
            res = res * 10 + digit
        
        return res
