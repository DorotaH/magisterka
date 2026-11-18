INF = 10 ** 10


def merge(l, r):
    res = l + r

    i = j = k = 0
    while i < len(l) and len(r) > j:
        if r[j] > l[i]:
            res[k] = l[i]
            k += 1
            i += 1
        else:
            res[k] = r[j]
            k += 1
            j += 1
    while i < len(l):
        res[k] = l[i]
        k += 1
        i += 1
    while len(r) > j:
        res[k] = r[j]
        k += 1
        j += 1

    return res


def solve(fl, fr, l, r):
    if l == r:
        return 0

    mid = (l + r) // 2
    res = solve(fl, fr, l, mid) + solve(fl, fr, mid + 1, r)

    i, j = l, mid + 1
    while i <= mid:
        while r >= j and fl[i] > fr[j]:
            j += 1
        res += j - mid - 1
        i += 1
    fl[l: 1 + r] = merge(fl[l: mid + 1], fl[mid + 1: 1 + r])
    fr[l: 1 + r] = merge(fr[l: mid + 1], fr[mid + 1: 1 + r])
    return res


def __starting_point():
    n = int(input())
    a = list(map(int, input().split()))

    fl, cnt = [], {}
    for x in a:
        cnt[x] = 1 + cnt.get(x, 0)
        fl.append(cnt[x])

    fr, cnt = [], {}
    for x in a[::-1]:
        cnt[x] = 1 + cnt.get(x, 0)
        fr.append(cnt[x])
    fr = fr[::-1]

#     print(fl, fr)
    print(solve(fl, fr, 0, n - 1))
#     print(fl, fr)


__starting_point()
