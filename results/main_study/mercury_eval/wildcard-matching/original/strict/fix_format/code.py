class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        # remove consecutive *
        match = []
        for i in range(len(p)):
            if i > 0 and p[i - 1] == "*" and p[i] == "*":
                continue
            else:
                match.append(p[i])

        p = "".join(match)

        # map out required words for special characters *abc = 0:abc
        mp = defaultdict(str)
        last = -1
        for i in range(len(p)):
            if p[i] == "*" or p[i] == "?":
                if last == -1:
                    last = i
                else:
                    mp[last] = p[last + 1 : i]
                    last = i

        if last > -1:
            mp[last] = p[last + 1 : len(p)]

        # gather unique values seen and check for all of their positions ahead of time
        st = set(mp.values())
        mpPos = defaultdict(list)
        for i in range(len(s)):
            for val in st:
                if s[i : i + len(val)] == val:
                    mpPos[val].append(i)

        @cache
        def dfs(i, j):
            # if they both reach the end or j is end and *
            if i >= len(s) and j >= len(p) or (j == len(p) - 1 and p[j] == "*"):
                return True

            # p is at the end or s is at the end and we dont have *
            elif j >= len(p) or (i >= len(s) and p[j] != "*"):
                return False

            res = False
            # the characters are a match
            if i < len(s) and s[i] == p[j] or p[j] == "?":
                res = res or dfs(i + 1, j + 1)

            elif p[j] == "*":
                target = mp[j]

                if i >= len(s) or (j + 1 < len(p) and p[j + 1] == "*"):
                    res = res or dfs(i, j + 1)
                else:
                    for val in mpPos[target]:
                        if val >= i:
                            res = res or dfs(val + len(target), j + len(target) + 1)

            return res

        return dfs(0, 0)
