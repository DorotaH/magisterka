def solve(a, b, q, queries):
    g = b * a // math.gcd(a, b)
    prefix = [0] * g
    for i in range(g):
        if  (i % a) % b != (i % b) % a:
            prefix[i] = 1

    for i in range(1, g):
        prefix[i]+=prefix[i-1]

    for l, r in queries:
        ans=prefix[r % g-1]-prefix[(l % g-1)]
        if  l % g == 0:
            ans -= prefix[g - 1] - prefix[l % g - 1]
        print(ans, end=" ")

import math

for _ in range(int(input())):
    a, b, q = map(int, input().split())
    queries = list()
    for _ in range(q):
        l, r=map(int, input().split())
        queries.append((l, r))
    solve(a, b, q, queries)
    print()
