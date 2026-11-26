import sys


def can_draw_polygon(N, sides):
    sides.sort()
    return sides[N - 1] < sum(sides[: N - 1], 0)


def main():
    input = sys.stdin.read
    data = input().split()
    N, sides = int(data[0]), list(map(int, data[1:]))
    if not can_draw_polygon(N, sides):
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()
