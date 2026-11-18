class Solution:
    def countOfAtoms(self, formula: str) -> str:
        # (A)1 is invalid
        # (A) is valid
        # Axxx is one Atom
        #
        stk = []
        arr = []
        for c in formula:
            if c in ['(', ')']:
                if stk:
                    arr.append(stk.pop())
                stk.append(c)
            elif not c.isdigit():
                if c.islower():
                    stk[-1] += c
                else:
                    if stk:
                        arr.append(stk.pop())
                    stk.append(c)
            else:
                if stk and stk[-1].isdigit():
                    stk[-1] += c
                else:
                    if stk:
                        arr.append(stk.pop())
                    stk.append(c)
        if stk:
            arr.append(stk.pop())

        dc = {}
        for i, c in enumerate(arr):
            if c == '(':
                stk.append(i)
            elif c == ')':
                dc[stk.pop()] = i

        # print(arr, dc)
        
        def func(l, r):
            res = Counter()
            stk = []
            i = l
            while i <= r:
                if arr[i] == '(':
                    stk.append(func(i + 1, dc[i] - 1))
                    i = 1 + dc[i]
                    continue
                if arr[i].isdigit():
                    v = int(arr[i])
                    for key in stk[-1]:
                        stk[-1][key] *= v
                    i += 1
                    continue
                stk.append(Counter())
                stk[-1][arr[i]] = 1
                i += 1
            for ctx in stk:
                res += ctx
            return res

        n = len(arr)
        ct = func(0, n - 1)
        ans = ''
        for key in sorted(ct.keys()):
            ans += key
            if ct[key] > 1:
                ans += str(ct[key])
        return ans