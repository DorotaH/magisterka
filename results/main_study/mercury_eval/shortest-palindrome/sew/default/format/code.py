class Solution:
    def shortestPalindrome(self, s: str) -> str:
        addStr = ""

        def palidromeCheck(string):
            if string[::-1] == string:
                return True
            return False

        if palidromeCheck(s):
            return s
        for i in range(1, len(s)):
            addStr += s[-i]
            if palidromeCheck(addStr + s):
                return addStr + s
            else:
                continue
        return s
