def gg(n, lol):
    ans = 0
    cur = 1
    lol2 = lol
    while 1 + 2 * lol <= n:
        cur *= 2
        ans += cur
        lol = 1 + 2 * lol
        lol2 *= 2
    if 2 * lol2 <= n:
        ans += n - lol2 * 2 + 1
    return ans


n, k = list(map(int, input().split()))
low, high = 1, n // 2
res = 1
while high >= low:
    mid = (low + high) // 2
    if gg(n, mid) >= k:
        res = mid
        low = mid + 1
    else:
        high = mid - 1
if n == k:
    print(1)
elif gg(n, res) - 1 - gg(n, res * 2) >= k:
    print(res * 2 + 1)
else:
    print(2 * res)
