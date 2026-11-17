import sys

for t in range(0, int(input())):
    n, k = map(int, sys.stdin.readline().strip().split())
    ans, cur = 0, 1
    while k >= cur and n > cur:
        cur = cur * 2
        ans = ans + 1
    if cur <= n:
        ans += (n - cur + k - 1) // k
    print(ans)
