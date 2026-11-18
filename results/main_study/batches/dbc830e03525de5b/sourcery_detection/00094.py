import sys

sys.setrecursionlimit(10000)

n = input()
k = int(input())
m = {}


def doit(n, k):
    if len(n) == 0:
        return k == 0
    d = int(n[0])
    if (n, k) not in m:
        ret = sum(
            (
                doit(n[1:], k - 1 if i > 0 else k)
                if i == d
                else doit('9' * (len(n) - 1), k - 1 if i > 0 else k)
            )
            for i in range(d + 1)
        )
        m[(n, k)] = ret
    return m[(n, k)]


print(doit(n, k))
