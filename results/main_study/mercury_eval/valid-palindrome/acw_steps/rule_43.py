class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ''.join(char.lower() for char in s if (char.isalnum()))
        # return False

        # return true is string is empty
        if (new == ''):
            return True

        # Loop through array
        j = len(new) - 1
        for i in range(len(new)):
            print('---------')
            print(len(new))
            print(i)
            print(j - i)

            # compare char, if not the same, return false
            if new[i] != new[j - i]:
                return False
            if ((len(new) % 2 != 0 and i == j - i) or (len(new) % 2 == 0 and i == j - i - 1)):
                return True
