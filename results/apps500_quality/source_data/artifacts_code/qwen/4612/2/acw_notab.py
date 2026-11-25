import sys
import math

a, b = map(int, sys.stdin.read().split())
x = (a + b) / 2
print(math.ceil(x))
