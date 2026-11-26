import sys
import math

input = sys.stdin.readline


def solve():
    n = int(input())
    x, y = map(int, input().split())

    time_white = time_black = 0
    time_diff = 0

    time_white = time_white + (n - x + y) // 2
    time_black = time_black + (n - (n - y + x)) // 2

    time_diff = (n - x + y) - (n - (n - y + x)) // 2

    if not time_diff % 2 == 0:
        print("White")
    else:
        print("Black")


if __name__ == "__main__":
    t = 1
    for _ in range(t):
        solve()
