import math

n = int(input())
i = 2
while True:
    sqrt_n = math.isqrt(n)
    for b in range(1, sqrt_n + 1):
        p = 2
        while b**p <= n:
            i = b**p
            p += 1
        if b**p > n:
            break
    if i <= n:
        break
    n = i - 1
print(i)
