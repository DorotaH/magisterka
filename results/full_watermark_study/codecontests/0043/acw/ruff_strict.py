from functools import reduce
from math import *

# sys.stdin = open(r"hack.txt", "r")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        l = list(map(int, input().split()))
        print(reduce(lambda x, y: x & y, l))


if __name__ == "__main__":
    main()
