import sys


def can_draw_polygon(N, L):
    # Check if the longest side is strictly shorter than the sum of the other N-1 sides
    return sum(L) - max(L) > max(L)


N = int(input())
L = list(map(int, input().split()))

if can_draw_polygon(N, L):
    print('Yes')
else:
    print('No')
