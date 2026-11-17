t = int(input())
for i in range(t):
    k = []
    z = []
    a = list(map(int, input().split()[:7]))
    a.sort()
    k = a[-1] - (a[0] + a[1])
    z = [str(a[0]), str(a[1])]
    a.pop(0)
    a.pop(0)
    for i in a:
        if i == k:
            z.append(str(i))
            break
    print(" ".join(z))
