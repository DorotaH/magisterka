import math
import sys


def read_ints():
    return list(map(int, sys.stdin.readline().split()))

def lcm(a, b):
    return a * b // math.gcd(a, b)

n = int(sys.stdin.readline())
a = read_ints()

min_lcm = float('inf')
min_indices = (0, 0)

for i in range(n):
    for j in range(i+1, n):
        curr_lcm = lcm(a[i], a[j])
        if curr_lcm < min_lcm:
            min_lcm = curr_lcm
            min_indices = (i+1, j+1)

print(*min_indices)
