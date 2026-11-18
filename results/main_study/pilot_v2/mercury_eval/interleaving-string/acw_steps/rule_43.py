class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        mem = {}
        def check(i, j):
            if (i, j) in mem:
                return mem[(i, j)]
            if i == j == 0:
                return True
            check1 = False
            check2 = False
            if i >= 0:
                check1 = check(i - 1, j) and s1[i - 1] == s3[i + j - 1]
            if 0 <= j:
                check2 = check(i, j - 1) and s2[j - 1] == s3[i + j - 1]
            res = check1 or check2
            mem[(i, j)] = res
            return res
        return check(len(s1), len(s2))

