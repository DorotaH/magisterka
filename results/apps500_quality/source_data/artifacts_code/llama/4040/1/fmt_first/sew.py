def f(n, m, d, c):
    c=[0]+c
    for  i in  range(1, m + 1):
        c[i]+=c[i-1]
    for  i in  range(1, m + 1):
        for  j in  range(c[i-1], c[i]):
            if j + d >= c[i]:
                print("NO")
                return None
    for  i in  range(1, n + 1):
        if i-c[m]<=0 and i+d>=c[m]:
            print("NO")
            return
    a = [0] * (n + 2)
    i = 1
    for  j in  range(1, m):
        if not c[j] <= d:
            a[c[j - 1] + 1 : c[j] + d + 1] = [j] * (c[j] + d + 1 - c[j - 1])
            i = c[j] + d + 1
        else:
            a[c[j] + 1 : c[j] + c[j + 1]] = [j + 1] * c[j + 1]
            i = c[j] + c[j + 1]
    a[1 + c[m - 1] : c[m]]=[m]*(c[m]-c[m-1])
    print("YES")
    print(*a[1 : 1 + n])


n, m, d=map(int, input().split())
c=list(map(int, input().split()))
f(n, m, d, c)