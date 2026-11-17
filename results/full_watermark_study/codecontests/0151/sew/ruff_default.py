for _ in range(int(input())):
    n, l = int(input()), list(map(int, input().split()))
    l.sort()
    s, x = 0, l[0]
    mn = x
    for i in range(n):
        x = l[i] - s
        s += x
        mn = max(x, mn)

    print(mn)
