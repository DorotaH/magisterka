class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        i = 0
        digits = []
        check = x // (10**i)
        while check != 0:
            newDig = check % 10
            digits.append(newDig)
            i += 1
            check = x // (10**i)
        revDig = digits[::-1]
        return digits == revDig