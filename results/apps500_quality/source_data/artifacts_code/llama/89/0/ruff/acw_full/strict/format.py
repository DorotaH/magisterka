import math

n = int(input())
ans = 0
start = 0
for i in range(1, 1 + n):
    start += i * 2 + 1 if (i * 2 + 1 <= n) else n - i + 1
    ans += 1

print(ans)
