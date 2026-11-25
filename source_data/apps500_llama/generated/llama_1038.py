import sys

t = int(input())
for _ in range(t):
    n = int(input())
    ans = 0
    h = 1
    while n >= h * (h + 1) // 2:
        ans += 1
        n -= h * (h + 1) // 2
        h += 1
    print(ans)
