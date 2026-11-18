n, m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
a.sort(reverse=True)

def check(d):
    s=0
    for  i in  range(0, len(a)):
        s+=max(0,a[i]-i//d)
    return m<=s
if not sum(a)<m:
    l, r = 1,n
    mid = l+r>>1
    while l<r:
        if check(mid):
            r=mid
        else:
            l=mid+1
        mid=l+r>>1
    print(l)
else:
    print(-1)
