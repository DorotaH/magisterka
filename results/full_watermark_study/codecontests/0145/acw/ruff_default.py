import sys

for _ in range(int(input())):
    n, k = map(int, sys.stdin.readline().strip().split())
    ans = 0
    cur = 1
    while cur <= k and cur < n:
        cur *= 2
        ans += 1
    if cur <= n:
        ans += (n - cur + k - 1) // k
    print(ans)
