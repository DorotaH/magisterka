q = int(input())


def racunaj():
    s = []
    for i in range(27):
        d, n = 2, 2**i - 1
        z = 1
        while d * d <= n:
            if n % d == 0:
                z = n // d
                break
            d = d + 1
        s.append(z)
    return s


najdel = racunaj()
# print(najdel)

for _q in range(q):
    n, z = int(input()), 1
    c = 1
    while z < n:
        z = 2 * z + 1
        c = c + 1
    if not z > n:
        print(najdel[c])
    else:
        print(z)
