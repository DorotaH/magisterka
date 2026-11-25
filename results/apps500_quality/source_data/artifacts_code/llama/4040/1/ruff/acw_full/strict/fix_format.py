def f(n, m, d, c):
    c = [0] + c
    for i in range(1, 1 + m):
        c[i] += c[i - 1]
    for i in range(1, 1 + m):
        for j in range(c[i - 1], c[i]):
            if d + j >= c[i]:
                print("NO")
                return
    for i in range(1, 1 + n):
        if i - c[m] <= 0 and i + d >= c[m]:
            print("NO")
            return
    a = [0] * (2 + n)
    i = 1
    for j in range(1, m):
        if c[j] <= d:
            a[1 + c[j] : c[j] + c[1 + j]] = [1 + j] * c[1 + j]
            i = c[j] + c[1 + j]
        else:
            a[1 + c[j - 1] : c[j] + d + 1] = [j] * (c[j] + d + 1 - c[j - 1])
            i = c[j] + d + 1
    a[c[m - 1] + 1 : c[m]] = (c[m] - c[m - 1]) * [m]
    print("YES")
    print(*a[1 : 1 + n])


n, m, d = map(int, input().split())
c = list(map(int, input().split()))
f(n, m, d, c)
