from functools import reduce


def main():
    from operator import xor
    from sys import stdin

    x = reduce(xor, (input()[i] == "1" for i in range(0, int(input()) * 2, 2)))
    res = []
    input()
    for s in stdin.read().splitlines():
        if not s == "3":
            x ^= True
        else:
            res.append("01"[x])
    print("".join(res))


def __starting_point():
    main()


__starting_point()
