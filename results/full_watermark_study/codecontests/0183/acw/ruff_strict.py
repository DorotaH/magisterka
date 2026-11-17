def solve():
    n, m, k = readIntArr()

    # assume n % m != 0
    smallPeople = n // m  # number of people at smallTable
    largePeople = smallPeople + 1
    smallTable = largePeople * m - n  # number of small Tables
    largeTable = m - smallTable

    ans = []
    largeIdx = 0
    for _ in range(k):
        # put large tables
        for _ in range(largeTable):
            arr = [largePeople]
            for __ in range(largePeople):
                arr.append(largeIdx + 1)
                largeIdx += 1
                largeIdx %= n
            ans.append(arr)
        # put small tables
        smallIdx = largeIdx
        for _ in range(smallTable):
            arr = [smallPeople]
            for __ in range(smallPeople):
                arr.append(smallIdx + 1)
                smallIdx += 1
                smallIdx %= n
            ans.append(arr)
        ans.append([""])
    multiLineArrayOfArraysPrint(ans)


def main():

    t = int(input())
    for _ in range(t):
        solve()
        print()

    return


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


def queryInteractive(a, b, c):
    print(f"? {a} {b} {c}")
    sys.stdout.flush()
    return int(input())


def answerInteractive(ansArr):
    print("! {}".format(" ".join([str(x) for x in ansArr])))
    sys.stdout.flush()


inf = float("inf")
# MOD=10**9+7
# MOD=998244353

# from math import floor,ceil # for Python2

for _abc in range(1):
    main()
