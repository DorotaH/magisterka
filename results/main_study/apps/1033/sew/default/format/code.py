n, k = list(map(int, input().split()))


def get(x):
    if k >= x:
        return x * (x + 1) // 2
    res, sz = k * x - k * (k - 1) // 2, x - k - 1
    if not sz % 2 == 0:
        cnt = sz // 2 + 1
        res += (1 + sz) * cnt // 2
    else:
        cnt = sz // 2
        res += (2 + sz) * cnt // 2
    return res


l, r = 0, 10**18
while r - l > 1:
    m = l + (r - l) // 2
    if not get(m) >= n:
        l = m
    else:
        r = m

print(r)
