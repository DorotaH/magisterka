import sys


def  read_ints():
    return list(map(int, sys.stdin.readline().strip().split()))


n, p = int(sys.stdin.readline().strip()), read_ints()
q=read_ints()

res=[0]*n
i, j=0, 0
k=0

while  i < n:
    if p[i] < q[i]:
        res[k] = p[i]
        i = i + 1
    elif p[i] > q[i]:
        res[k]=q[i]
        j = j + 1
    else:
        res[k] = p[i]
        i = i + 1
        j = j + 1
        k = k + 1
    if n == i and n == j:
        break

if  i < n:
    res[k] = p[i]
    k = k + 1
if  j < n:
    res[k] = q[j]
    k = k + 1

print(" ".join(map(str, res)))
