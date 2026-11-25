import sys


def solve():
    n = int(input())
    x, y = map(int, input().split())

    if (
        n == 2
        or n == 3
        or n == 4
        or n == 5
        or n == 6
        or n == 7
        or n == 8
        or n == 9
        or n == 10
    ):
        x, y = n - x + 1, n - y + 1
        if (x + y) % 2 == 0:
            print("White")
        else:
            print("Black")
    else:
        print("White" if (x + y) % 2 == 0 else "Black")


if __name__ == "__main__":
    solve()
