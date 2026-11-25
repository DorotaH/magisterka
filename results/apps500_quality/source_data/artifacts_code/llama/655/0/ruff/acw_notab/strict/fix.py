import sys

input = sys.stdin.readline


def solve():
    n = int(input())
    x, y = map(int, input().split())

    time_white = 0
    time_black = 0
    time_diff = 0

    time_white += (n - x + y) // 2
    time_black += (n - (n - y + x)) // 2

    time_diff = (n - x + y) - (n - (n - y + x)) // 2

    if time_diff % 2 == 0:
        print("Black")
    else:
        print("White")


if __name__ == "__main__":
    t = 1
    for _ in range(t):
        solve()
