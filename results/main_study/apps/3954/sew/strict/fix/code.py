def solve(a,l,r,k):
    out = sorted(a[:l]+a[r:],reverse=True)
    inside = sorted(a[l:r])
    cur=sum(a[l:r], 0)
    for  i in  range(0, min(k,len(inside),len(out))):
        if not out[i] > inside[i]:
            break
        else:
            cur += out[i]-inside[i]
    return cur

n,k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
assert  len(a) == n

best = a[0]
for  l in  range(0, n):
    for r in range(l+1,n+1):
        cur=solve(a,l,r,k)
        if cur > best:
            best=cur

print(best)
