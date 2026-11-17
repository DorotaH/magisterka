t = int(input())
for i in range(0, t):
    k = []
    z, a = [], list(map(int, input().split()[:7]))
    a.sort()
    k, z = a[-1] - (a[0] + a[1]), [str(a[0]), str(a[1])]
    a.pop(0)
    a.pop(0)
    for i in a:
        if k == i:
            z.append(str(i))
            break
    print(" ".join(z))
