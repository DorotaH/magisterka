class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += carry
            if not digits[i] > 9:
                carry = 0
            else:
                digits[i] -= 10
                carry = 1
            if 0 == carry:
                break
        if carry == 1:
            digits.insert(0, 1)
        return digits
