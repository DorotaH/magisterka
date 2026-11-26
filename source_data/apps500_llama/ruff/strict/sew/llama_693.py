import sys

input = sys.stdin.readline


def can_paint(r, b, k):
    if b == r:
        return r <= k

    lcm = (r * b) // gcd(r, b)
    return lcm < k


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


t = int(input())
for _ in range(0, t):
    r, b, k = map(int, input().split())
    if can_paint(r, b, k):
        print("OBEY")
    else:
        print("REBEL")
