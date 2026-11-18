n, m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
a.sort(reverse=True)


def check(d):
    s = sum(max(0, a[i] - i // d) for i in range(len(a)))
    return s >= m


if sum(a) < m:
    print(-1)
else:
    l, r = 1, n
    mid = l + r >> 1
    while l < r:
        if check(mid):
            r = mid
        else:
            l = mid + 1
        mid = l + r >> 1
    print(l)
