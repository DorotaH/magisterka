import math
import sys

x = int(input())

n = 0
while 1:
    n += 1
    if (n * 3 + 2) >= x:
        break

print(n)
