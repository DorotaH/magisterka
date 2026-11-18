n, k, x=list(map(int, input().split()))
a=[None]+list(map(int, input().split()))

lo=0
hi = 10 ** 9 * 5000
q=[None]*(1 + n)


def  get(mid):
    f, r=0, 0
    q[0]=0, 0, 0
    for i in range(1, 1 + n):
        if q[r][2] == i - k - 1: r += 1
        cur=q[r][0]+a[i]-mid, 1 + q[r][1], i
        while  f >= r and  cur >= q[f]: f -= 1
        f += 1
        q[f]=cur
    if q[r][2] == n - k: r = r + 1
    return  q[r]

while hi > lo:
    mid = (lo + hi + 1) >> 1
    _, cnt, _ = get(mid)
    if cnt >= x:
        lo = mid
    else:
        hi = mid - 1

sm, _, _=get(lo)
ans=max(-1, sm+(x * lo))
print(ans)
