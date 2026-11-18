class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        sub = ""

        def isRep(o, b):
            a = o
            if len(a) == len(b):
                return False
            while len(a) < len(b):
                a += o
            if a == b:
                return True
            return False

        for c in s:
            sub += c
            if isRep(sub, s):
                return True

        return False
