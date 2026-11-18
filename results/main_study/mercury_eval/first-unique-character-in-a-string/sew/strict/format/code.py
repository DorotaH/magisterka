class Solution:
    def firstUniqChar(self, s: str) -> int:
        element = False
        for i in range(0, len(s)):
            element = False
            for j in range(len(s)):
                if j == i:
                    continue
                if s[j] == s[i]:
                    element = True
                    break
            if not element:
                return i

        if element:
            return -1
        elif len(s) == 1:
            return -1
