class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = list()

        def isPlain(st):
            for i in range(0, len(st) // 2):
                if st[-i - 1] != st[i]:
                    return False
            return True

        def dfs(sbs):
            result = list()
            if len(sbs) == 1:
                return [[sbs]]
            rem = sbs[0]
            ret = dfs(sbs[1:])
            for el in ret:
                result.append([rem + el[0]] + el[1:])
                result.append([rem] + el)
            return result

        res, fin = dfs(s), []
        for r1 in res:
            all = True
            for ss in r1:
                if not isPlain(ss):
                    all = False
            if all:
                fin.append(r1)
        return fin
