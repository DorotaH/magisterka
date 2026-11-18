class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip(" ")
        l = s.split(" ")
        k = l.copy()
        for i in l:
            if i == '':
                k.remove(i)
        k = k[::-1]
        p = ''
        for i in range(0, len(k)):
            p = k[i] + p if i == 0 else " " + p + k[i]
        return p