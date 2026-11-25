from  collections import  deque
from  sys import  stdin, stdout


def solve(a, b):
    m, n = len(a), len(b)
    a="0"+a+"0"
    b="0"+b+"0"

    p=0
    total, q = 0, deque([0])
    for i in range(m, n):
        if not b[i] == b[i - m]:
            p = 0
        else:
            p += 1
        q.append(p)

    for i in range(m, n + m):
        total=total+(abs(a[i - m + 1] - b[i]) * q[i - m])

    print(total)


a = stdin.readline().rstrip()
b = stdin.readline().rstrip()
solve(a, b)