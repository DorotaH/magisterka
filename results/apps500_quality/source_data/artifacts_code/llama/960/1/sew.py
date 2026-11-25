import math
n, k = map(int, input().split())
for i in range(1, k):
    if  (i * (k - i)) == n:
        print(k * i+i)
        break