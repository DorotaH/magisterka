def naiveSolve():

    return


def solve():

    return


from types import GeneratorType


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        to = f(*args, **kwargs)
        while True:
            if type(to) is GeneratorType:
                stack.append(to)
                to = next(to)
            else:
                stack.pop()
                if not stack:
                    break
                to = stack[-1].send(to)
        return to

    return wrappedfunc


def main():

    t = int(input())
    allans = []
    for _ in range(t):
        n = int(input())
        req = [None for __ in range(n)]
        for i in range(n):
            temp = readIntArr()
            temp.pop(0)
            for j in range(len(temp)):
                temp[j] -= 1
            req[i] = temp

        # check for cycles in a path (like topological sort)
        hasCycle = [False]
        visited = [False] * n
        path = [False] * n

        @bootstrap
        def dfs(book):
            for nex in req[book]:
                if hasCycle[0]:
                    yield None
                if path[nex]:
                    hasCycle[0] = True
                    yield None
                if visited[nex] == False:
                    visited[nex] = True
                    path[nex] = True
                    yield dfs(nex)
                    path[nex] = False
            yield None

        for i in range(n):  # check if a book visits itself
            if not visited[i]:
                path[i] = True
                visited[i] = True
                dfs(i)
                path[i] = False

        if hasCycle[0]:
            allans.append(-1)
            continue

        memo = [-1] * n

        @bootstrap
        def dp(book):
            if memo[book] == -1:
                ans = 1
                for prev in req[book]:
                    if book > prev:
                        ans = max(ans, (yield dp(prev)))
                    else:
                        ans = max(ans, 1 + (yield dp(prev)))
                memo[book] = ans
            yield memo[book]

        ans = 0
        for book in range(n):
            ans = max(ans, dp(book))
        allans.append(ans)

    multiLineArrayPrint(allans)


import sys

input = (
    sys.stdin.buffer.readline
)  # FOR READING PURE INTEGER INPUTS (space separation ok)
# input=lambda: sys.stdin.readline().rstrip("\r\n") #FOR READING STRING/TEXT INPUTS.


def oneLineArrayPrint(arr):
    print(" ".join([str(x) for x in arr]))


def multiLineArrayPrint(arr):
    print("\n".join([str(x) for x in arr]))


def multiLineArrayOfArraysPrint(arr):
    print("\n".join([" ".join([str(x) for x in y]) for y in arr]))


def readIntArr():
    return [int(x) for x in input().split()]


# def readFloatArr():
#     return [float(x) for x in input().split()]


def makeArr(defaultValFactory, dimensionArr):  # eg. makeArr(lambda:0,[n,m])
    dv = defaultValFactory
    da = dimensionArr
    if len(da) == 1:
        return [dv() for _ in range(da[0])]
    else:
        return [makeArr(dv, da[1:]) for _ in range(da[0])]


def queryInteractive(x):
    print(f"{x}")
    sys.stdout.flush()
    return int(input())


def answerInteractive(ans):
    print(f"! {ans}")
    sys.stdout.flush()


inf = float("inf")
# MOD=10**9+7
# MOD=998244353

# from math import floor,ceil # for Python2

for _abc in range(1):
    main()
