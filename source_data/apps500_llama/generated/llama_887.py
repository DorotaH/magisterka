import math
import sys

N = int(input())
t = []
a = []
for _ in range(N):
    t_i, a_i = map(int, input().split())
    t.append(t_i)
    a.append(a_i)

def gcd(a, b):
    """Compute the greatest common divisor of a and b"""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b // gcd(a, b)

total_votes = 1
for i in range(N):
    total_votes = lcm(total_votes, t[i] * a[i])

ans = float('inf')
for i in range(N):
    ans = min(ans, t[i] + a[i] * (total_votes // gcd(t[i], a[i])))

print(ans)
