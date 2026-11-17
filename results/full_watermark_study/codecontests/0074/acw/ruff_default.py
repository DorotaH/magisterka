for _ in range(int(input())):
    n = int(input())
    c1 = 1
    c2 = 1
    i = 0
    a = 0
    b = 0
    while n:
        r = int(n % 10)
        if int(i % 2) == 0:
            a = (c1 * r) + a
            c1 *= 10
        else:
            b = (c2 * r) + b
            c2 *= 10
        n = int(n / 10)
        i += 1
    print(((a + 1) * (1 + b)) - 2)
