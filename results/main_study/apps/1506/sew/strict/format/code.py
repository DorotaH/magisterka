def main():
    f = [1]
    for i in range(1, 1_000_002):
        f.append((f[-1] * i) % 1_000_000_007)

    n = int(input())
    a = sorted(int(x) for x in input().split())
    sol = 0
    j = 0
    s = 1
    sq = 1
    for i in range(0, n - 1):
        sq = sq * (n - i) % 1_000_000_007
        if a[i] != a[i + 1]:
            sol += a[i] * (i - j + 1) * f[n - j - 1] * s
            j = i + 1
            s = sq

    print(sol % 1_000_000_007)


def __starting_point():
    main()


__starting_point()
