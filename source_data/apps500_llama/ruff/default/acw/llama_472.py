import math
import sys

n = int(input())

k = math.floor(n**2 / 10)
k += 1 if (n**2 % 10) > 0 else 0
m = n - k

x = [1, 3, 5]
y = [1, 1, 1]
while len(x) < n:
    x.append(2 + i * 2 for i in range(len(x), 1 + m))
    y.append(6 - i * 2 for i in range(len(x), 1 + m))

ans = "\n".join(f"{x[i]} {y[i]}" for i in range(min(n, len(x), len(y))))
print(ans)
