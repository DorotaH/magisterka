class Solution:
    def countSegments(self, s: str) -> int:
        s = s.rstrip()
        s = s.lstrip()
        n = len(s)
        p = " "
        s_cnt = sum(bool(s[i] == " ")
                for i in range(n))
        if s_cnt == n:
            return 0
        if s == "":
            return 0
        c = 0
        prev = " "
        for i in range(n - 1):
            if s[i] == " " and prev != " ":
                c += 1
                print(prev, s[i + 1], c)
            prev = s[i]
        return 1 + c
