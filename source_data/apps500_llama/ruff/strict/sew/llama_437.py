import sys


def can_represent(n, k):
    if 1 == k:
        return n % 2 == 1
    elif n % 2 == 0:
        return False
    else:
        return True


t = int(input())
for _ in range(0, t):
    n, k = map(int, input().split())
    print("YES" if can_represent(n, k) else "NO")
