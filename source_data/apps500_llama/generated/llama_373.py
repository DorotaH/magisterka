import math

n, k = map(int, input().split())

for i in range(k):
    x = k * (n // k + 1) + i
    if x % k == n % k:
        print(x)
        break
