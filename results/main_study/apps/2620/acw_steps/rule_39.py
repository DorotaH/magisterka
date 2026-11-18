from math import *

n, q = list(map(int, input().split()))
after = min(15, n)
before = n - after


def calc(left, right):
    return right * (1 + right) // 2 - (left - 1) * left // 2


def perm(i):
    unused = [i + 1 for i in range(after)]
    arr = []
    for j in reversed(list(range(after))):
        cur = i // factorial(j)
        arr.append(unused[cur])
        del unused[cur]
        i -= factorial(j) * cur
    return arr


p = perm(0)
x = 0

for _ in range(q):
    line = list(map(int, input().split()))

    if len(line) == 3:
        # type 1
        l = line[1]
        r = line[2]
        res = 0
        if l <= before:
            res += r * (1 + r) // 2 if before >= r else before * (before + 1) // 2
            res -= l * (l - 1) // 2
            l = before + 1
        if before < r:
            res += sum(p[l-1-before:r-before]) + (r-l+1) * before

        print(res)
    else:
        # type 2
        x += line[1]
        p = perm(x)
