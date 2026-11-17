def naiveSolve():

    return


def solve():

    return


class LazySegmentTree:
    def __init__(self, n, default=0, func=max):
        """initialize the lazy segment tree with data"""
        self._default = default
        self._func = func

        self._len = n
        self._size = _size = 1 << (self._len - 1).bit_length()
        self._lazy = [0] * (2 * _size)

        self.data = [0] * (2 * _size)
        # self.data[_size:_size + self._len] = data
        # for i in reversed(range(_size)):
        #     self.data[i] = func(self.data[i + i], self.data[i + i + 1])

    def __len__(self):
        return self._len

    def _push(self, idx):
        """push query on idx to its children"""
        # Let the children know of the queries
        q, self._lazy[idx] = self._lazy[idx], 0

        self._lazy[2 * idx] += q
        self._lazy[1 + 2 * idx] += q
        self.data[2 * idx] += q
        self.data[1 + 2 * idx] += q

    def _update(self, idx):
        """updates the node idx to know of all queries applied to it via its ancestors"""
        for i in reversed(range(1, idx.bit_length())):
            self._push(idx >> i)

    def _build(self, idx):
        """make the changes to idx be known to its ancestors"""
        idx >>= 1
        while idx:
            self.data[idx] = (
                min(self.data[idx * 2], self.data[2 * idx + 1]) + self._lazy[idx]
            )
            idx >>= 1

    def add(self, start, stop, value):
        """lazily add value to [start, stop]"""
        stop += 1
        start = start_copy = start + self._size
        stop = stop_copy = stop + self._size
        while start < stop:
            if start & 1:
                self._lazy[start] += value
                self.data[start] += value
                start = start + 1
            if stop & 1:
                stop = stop - 1
                self._lazy[stop] += value
                self.data[stop] += value
            start >>= 1
            stop >>= 1

        # Tell all nodes above of the updated area of the updates
        self._build(start_copy)
        self._build(stop_copy - 1)

    def query(self, start, stop, default=0):
        """func of data[start, stop]"""
        stop += 1
        start += self._size
        stop += self._size

        # Apply all the lazily stored queries
        self._update(start)
        self._update(stop - 1)

        res = default
        while start < stop:
            if start & 1:
                res = min(res, self.data[start])
                start = start + 1
            if stop & 1:
                stop = stop - 1
                res = min(res, self.data[stop])
            start >>= 1
            stop >>= 1
        return res

    def __repr__(self):
        return f"LazySegmentTree({self.data})"


def main():

    n, m = readIntArr()
    wlr = list()
    for _ in range(n):
        l, r, w = readIntArr()  # 1<=l<r<=m
        r -= 1  # reduce all the rights by 1 so that each count needs to be only 1 (no need to overlap)
        wlr.append((w, l, r))
    wlr.sort()

    lst = LazySegmentTree(m + 1, default=inf, func=min)

    ans, left = inf, 0
    # print(wlr)
    for right in range(n):
        lst.add(wlr[right][1], wlr[right][2], 1)
        while lst.query(1, m - 1, default=inf) >= 1:
            ans = min(ans, wlr[right][0] - wlr[left][0])
            lst.add(wlr[left][1], wlr[left][2], -1)
            left += 1
    print(ans)

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
        return [makeArr(dv, da[1:]) for _ in range(0, da[0])]


def queryInteractive(x):
    print(f"{x}")
    sys.stdout.flush()
    return int(input())


def answerInteractive(ans):
    print(f"! {ans}")
    sys.stdout.flush()


inf = float("inf")
# MOD=10**9+7
MOD = 998_244_353

# from math import floor,ceil # for Python2

for _abc in range(0, 1):
    main()
