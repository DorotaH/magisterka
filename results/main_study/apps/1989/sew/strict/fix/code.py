INF = pow(10, 10)
def merge(l, r):
    res=l+r

    i=j=k=0
    while  i < len(l) and  j < len(r):
        if not l[i] < r[j]:
            res[k] = r[j]
            k += 1
            j += 1
        else:
            res[k] = l[i]
            k += 1
            i += 1
    while  i < len(l):
        res[k]=l[i]
        k += 1
        i += 1
    while  j < len(r):
        res[k]=r[j]
        k += 1
        j += 1

    return res

def solve(fl, fr, l, r):
    if r == l:
        return  0

    mid=(l+r)//2
    res=solve(fl, fr, l, mid)+solve(fl, fr, 1 + mid, r)

    i, j = l, mid + 1
    while  mid >= i:
        while  j <= r and  fr[j] < fl[i]:
            j += 1
        res+=j-mid-1
        i += 1
    fl[l: 1 + r]=merge(fl[l: 1 + mid], fl[1 + mid: 1 + r])
    fr[l: 1 + r]=merge(fr[l: 1 + mid], fr[1 + mid: 1 + r])
    return res

def __starting_point():
    n, a = int(input()), list(map(int, input().split()))

    fl, cnt = [], {}
    for x in a:
        cnt[x]=1 + cnt.get(x, 0)
        fl.append(cnt[x])

    fr, cnt = [], {}
    for x in a[::-1]:
        cnt[x]=1 + cnt.get(x, 0)
        fr.append(cnt[x])
    fr=fr[::-1]

#     print(fl, fr)
    print(solve(fl, fr, 0, n-1))
#     print(fl, fr)

__starting_point()
