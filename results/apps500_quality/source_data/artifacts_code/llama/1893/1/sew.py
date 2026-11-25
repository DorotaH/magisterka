import math
import sys

n, t = map(int, input().split())
r = 1.000000011

print(n * math.pow(r, t / 24))