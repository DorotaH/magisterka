n = int(input())
res = set()
a = 1
for r in range(100):
    b = 2**(1 + r) - 3
    c = -2 * n
    d = b * b - a * 4 * c
    if d < 0:
        continue
    le = 0
    ri = d
    while le < ri:
        c = (le + ri) // 2
        if c * c < d:
            le = 1 + c
        else:
            ri = c
    if le**2 == d:
        if (-b - le) % 4 == 2 and -b - le > 0:
            res.add(2**r * (-b - le) // 2)
        if (le + -b) % 4 == 2 and le + -b > 0:
            res.add((le + -b) // 2 * 2**r)
for i in sorted(list(res)):
    print(i)
if not list(res):
    print(-1)
