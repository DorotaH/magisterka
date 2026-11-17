def naiveSolve():

    return


def solve():

    return


from types import GeneratorType


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if not stack:
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
        else:
            return f(*args, **kwargs)

    return wrappedfunc


def main():

    t, allans = int(input()), []
    for _ in range(t):
        n = int(input())
        adj = [list() for _ in range(n + 1)]
        for __ in range(n - 1):
            u, v = readIntArr()
            adj[u].append(v)
            adj[v].append(u)

        pruned, budCnts = [False] * (n + 1), [0]
        childCnts = [0] * (n + 1)

        @bootstrap
        def dfs(node):
            for nex in adj[node]:
                if not (len(path) >= 2 and path[-2] == nex):  # not parent
                    childCnts[node] += 1
                    path.append(nex)
                    yield dfs(nex)
                    path.pop()
            if (
                len(path) >= 3 and pruned[node] == pruned[path[-2]] == False
            ):  # prune here
                budCnts[0] += 1
                pruned[path[-2]] = True
                childCnts[path[-3]] -= 1
            yield None

        path = [1]
        dfs(1)

        budCnts = budCnts[0]
        directLeaves = childCnts[1]
        budContribution = (
            n - 1 - directLeaves - budCnts * 2
        )  # for each bud, cover the parent and the parent of parent
        leavesWithoutBud = max(1, directLeaves)  # if no leaves, treat root as leave
        ans = budContribution + leavesWithoutBud
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
