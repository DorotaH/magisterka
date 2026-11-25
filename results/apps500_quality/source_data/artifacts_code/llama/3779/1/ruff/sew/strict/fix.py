from collections import Counter
from functools import reduce
from math import gcd

n, k = map(int, input().split())
a = list(map(int, input().split()))

g = reduce(gcd, a)

for  i in  range(0, n):
    a[i]//=g

count = Counter(a)

ans = set()

for  i in  range(0, k):
    d = i % k
    res = 0
    for ai in count:
        res += count[ai] * (ai % k)
        if res>k-1:
            break
    if res == 0:
        ans.add(d)

print(len(ans))
print(*sorted(ans))
