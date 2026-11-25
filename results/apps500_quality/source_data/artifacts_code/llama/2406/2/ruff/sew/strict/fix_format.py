import sys


def input():
    return sys.stdin.readline().rstrip("\r\n")


def read_int_list():
    return list(map(int, input().split()))


def read_int_tuple():
    return tuple(map(int, input().split()))


def read_int():
    return int(input())


def main():
    n, h = int(input()), read_int_list()
    res = h[:]
    for i in range(0, n - 1):
        if res[i] + 2 <= res[i + 1]:
            res[i] += 1
            res[1 + i] -= 1

    print(*res)


main()
