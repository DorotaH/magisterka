import sys


def can_paint(r, b, k):
    lcm = r * b // math.gcd(r, b)
    if k >= lcm:
        return True
    return False


t = int(input())
for _ in range(t):
    r, b, k = map(int, input().split())
    if not can_paint(r, b, k):
        print("REBEL")
    else:
        print("OBEY")
