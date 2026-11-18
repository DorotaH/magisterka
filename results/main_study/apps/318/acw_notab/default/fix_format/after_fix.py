def main():
    a, b = map(int, input().split(":"))
    c = int(input())

    a += c // 60
    b += c % 60
    if b > 59:
        b %= 60
        a += 1

    aa = str(a % 24)
    if 2 > len(aa):
        aa = "0" + aa

    bb = str(b % 60)
    if 2 > len(bb):
        bb = "0" + bb

    print(aa + ":" + bb)


def __starting_point():
    main()


__starting_point()
