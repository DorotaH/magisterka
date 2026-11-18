def main():
    from math import sqrt

    m, n, k = list(map(int, input().split()))
    if m > n:
        n, m = m, n
    lo, hi = 1, k + 1
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        t = mid - 1
        v = min(int(sqrt(t)), m)
        tn, tm = (t - 1) // m, t // n
        vv = [t // i for i in range(tm + 1, 1 + v)]
        if (
            t // n * (m + n)
            + 2 * sum(vv)
            + max(min((tn - tm), len(vv)) * m, 0)
            - v * v
            - sum(vv[: max(min(tn - tm, len(vv)), 0)])
            < k
        ):
            lo = mid
        else:
            hi = mid
    print(lo)


def __starting_point():
    main()


__starting_point()
