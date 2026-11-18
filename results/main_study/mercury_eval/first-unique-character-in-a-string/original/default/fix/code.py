class Solution:
    def firstUniqChar(self, s: str) -> int:
        element = False
        for i in range(len(s)):
            element = False
            for j in range(len(s)):
                if i==j:
                    continue
                if s[i]==s[j]:
                    element = True
                    break
            if not element:
                return i
                
        if element or len(s)==1:
            return -1
