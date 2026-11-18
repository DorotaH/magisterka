def check(k):
    anew = [a[i] + (i + 1) * k for i in range(n)]
    anew.sort()
    asum = sum(anew[:k])
    return asum if asum <= s else 0


n, s = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
min_sum = 0
L = 0
R = 1 + n
while R - L > 1:
    m = (R + L) // 2
    res = check(m)
    if res:
        L = m
        min_sum = res
    else:
        R = m
print(L, min_sum)
