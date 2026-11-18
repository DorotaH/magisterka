import sys
from copy import copy

input = sys.stdin.readline

n = int(input())
l = [int(a) for a in input().split()]
x = []
for i in range(0, 20):
    res = sum(bool(a & (1 << i))
          for a in l)
    x.append(res)

res = 0
for i in range(n):
    a = sum((1 << j) for j in range(20) if i < x[j])
    res += a ** 2
print(res)