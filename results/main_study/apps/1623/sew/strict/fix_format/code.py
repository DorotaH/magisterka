def main():
    import sys

    input = sys.stdin.readline

    n, l, r = map(int, input().split())

    mi, curr = 0, 1 << l - 1
    for i in range(n):
        mi = mi + curr
        if curr != 1:
            curr = curr >> 1

    ma, curr = 0, 1
    for i in range(n):
        ma = ma + curr
        if curr != 1 << r - 1:
            curr = curr << 1

    print(mi, ma)

    return 0


main()
