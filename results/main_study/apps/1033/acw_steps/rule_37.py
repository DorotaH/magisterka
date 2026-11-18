n, k = list(map(int, input().split()))


def get(x):
    if x <= k:
        return x * (1 + x) // 2
    res = k * x - (k - 1) * k // 2
    sz = x - k - 1
    if sz % 2 == 0:
        cnt = sz // 2
        res += (2 + sz) * cnt // 2
    else:
        cnt = sz // 2 + 1
        res += (sz + 1) * cnt // 2
    return res


l = 0
r = 10 ** 18
while r - l > 1:
    m = l + (r - l) // 2
    if get(m) >= n:
        r = m
    else:
        l = m

print(r)
