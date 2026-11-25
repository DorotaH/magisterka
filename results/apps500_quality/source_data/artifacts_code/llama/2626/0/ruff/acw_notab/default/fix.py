import math
import sys


def main():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n = int(input())
        if n == 1:
            print(1)
        else:
            print(math.floor((n - 1) / 2) * math.ceil((n - 1) / 2))


if __name__ == "__main__":
    main()
