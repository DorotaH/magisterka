from math import floor

T = int(input())


def rl(t=int):
    return list(map(t, input().split()))


def feasible(a, m):
    # print("trying", a, m)
    og = a[:]
    for i in range(len(a) - 1, 1, -1):
        # h - 3 * d >= m
        # h - m >= 3 * d
        # (h - m) / 3 >= d
        if m > a[i]:
            return False

        d = floor((a[i] - m) // 3)
        if og[i] < 3 * d:
            d = og[i] // 3
        a[i - 1] += d
        a[i - 2] += 2 * d
        a[i] -= 3 * d
        # print("removed", d, a, m)
    return min(a[0], a[1]) >= m


for _ in range(1, T + 1):
    n = int(input())
    a = rl()

    i, j = min(a), max(a)
    while j - 1 > i:
        m = (i + j) // 2
        # print(i, m, j)
        if feasible(a[:], m):
            i = m
        else:
            j = m - 1

    print(j if feasible(a, j) else i)
