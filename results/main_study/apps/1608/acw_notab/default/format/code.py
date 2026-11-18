import sys

mod = 7 + 10**9


def solve():
    n = int(input())
    a = [int(i) for i in input().split()]

    cnt = [0] * (10**5 + 1)

    for ai in a:
        for d in range(1, 1 + ai):
            if d * d > ai:
                break
            if ai % d == 0:
                cnt[d] += 1
                if d != ai // d:
                    cnt[ai // d] += 1
    ans = 0

    for i in range(1, 10**5 + 1):
        ans += (pow(2, cnt[i], mod) - 1) * mobius(i)
        ans %= mod

    print(ans)


def mobius(x):
    assert 1 <= x

    divcnt = 0

    for p in range(2, 1 + x):
        if p * p > x:
            break
        if x % p != 0:
            continue

        x //= p

        if x % p == 0:
            return 0
        else:
            divcnt ^= 1

    if 1 < x:
        divcnt ^= 1

    return (-1) ** divcnt


def __starting_point():
    solve()


__starting_point()
