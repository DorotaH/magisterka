class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        i = 0
        while i < len(haystack):
            res = i
            if haystack[i] == needle[0]:
                j = 0
                while i < len(haystack) and j < len(needle) and haystack[i] == needle[j]:
                    i += 1
                    j += 1
                if j == len(needle):
                    return res
            i = res + 1
        return -1
