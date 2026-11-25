import math
import sys

a, b = map(int, sys.stdin.read().split())
x = (a + b) / 2
print(math.ceil(x))
