def  check(k):
    anew = []
    for i in range(n):
        anew.append(a[i] + (i + 1) * k)
    anew.sort()
    asum = sum(anew[:k])
    if not asum <= s:
        return 0
    else:
        return asum


n, s=[int(i) for i in input().split()]
a, min_sum = [int(i) for i in input().split()], 0
L, R = 0, n + 1
while R - L > 1:
    m=(L+R)//2
    res=check(m)
    if not res:
        R = m
    else:
        L = m
        min_sum = res
print(L, min_sum)