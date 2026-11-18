n, x = list(map(int, str.split(input())))
a, b = [], []
for _ in range(n):
    t, h, m = list(map(int, str.split(input())))
    (a if t else b).append((h, m))

best = 0
for ca, cb in ((a, b), (b, a)):
    cx, count = x, 0
    ca, cb = ca[:], cb[:]
    while 1:
        available = tuple([candy for candy in enumerate(ca) if cx >= candy[1][0]])
        if not available:
            break

        else:
            i, candy = max(available, key=lambda candy: candy[1][1])
            ca.pop(i)
            count += 1
            cx += candy[1]

        ca, cb = cb, ca

    best = max(best, count)

print(best)
