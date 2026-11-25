import sys


def read_ints():
    return list(map(int, sys.stdin.readline().strip().split()))

n = int(sys.stdin.readline().strip())
p = read_ints()
q = read_ints()

res = [0] * n
i, j = 0, 0
k = 0

while i < n:
    if p[i] < q[i]:
        res[k] = p[i]
        i += 1
    elif p[i] > q[i]:
        res[k] = q[i]
        j += 1
    else:
        res[k] = p[i]
        i += 1
        j += 1
        k += 1
    if i == n and j == n:
        break

if i < n:
    res[k] = p[i]
    k += 1
if j < n:
    res[k] = q[j]
    k += 1

print(' '.join(map(str, res)))
