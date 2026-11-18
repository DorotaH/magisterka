class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        #remove consecutive *
        match = []
        for i in range(len(p)):
            if i > 0 and p[i - 1] == '*' and p[i] == '*':
                continue
            else:
                match.append(p[i])

        p = ''.join(match)

        #map out required words for special characters *abc = 0:abc
        mp = defaultdict(str)
        last = -1
        for i in range(len(p)):

            if p[i] in ['*', '?']:
                if last == -1:
                    last = i
                else:
                    mp[last] = p[1 + last:i]
                    last = i


        if last > -1:
            mp[last] = p[1 + last:]

        #gather unique values seen and check for all of their positions ahead of time
        st = set(mp.values())
        mpPos = defaultdict(list)
        for i in range(len(s)):
            for val in st:
                if s[i:i + len(val)] == val:
                    mpPos[val].append(i)

        @cache
        def dfs(i, j):
            #if they both reach the end or j is end and *
            if i >= len(s) and j >= len(p) or (j == len(p) - 1 and p[j] == '*'):
                return True

            #p is at the end or s is at the end and we dont have *
            elif j >= len(p) or (i >= len(s) and p[j] != '*'):
                return False

            res = False
            #the characters are a match
            if i < len(s) and s[i] == p[j] or p[j] == '?':
                res = res or dfs(i + 1, 1 + j)


            elif p[j] == '*':
                target = mp[j]

                if i >= len(s) or (1 + j < len(p) and p[1 + j] == '*'):
                    res = res or dfs(i, 1 + j)
                else:
                    for val in mpPos[target]:
                        if i <= val:
                            res = res or dfs(len(target) + val, len(target) + j + 1)



            return res

        return dfs(0, 0)
