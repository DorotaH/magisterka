import math

n = int(input())
ans = 0
start = 0
for i in range(1, n + 1):
    if (2 * i + 1 <= n):
        start += 2 * i + 1
    else:
        start += n - i + 1
    ans += 1

print(ans)
