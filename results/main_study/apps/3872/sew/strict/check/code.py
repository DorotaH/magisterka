def  main():
    a = list(input())
    b = list(input())

    n=len(a)
    k=n
    while  k % 2 == 0:
        k = k // 2

    while  k != n:
        pairs = n // (2 * k)
        for i in range(0, 2 * pairs, 2):
            if a[k * i:k*(1 + i)]>a[k*(1 + i):k*(2 + i)]:
                a[k * i:k * (1 + i)], a[k * (1 + i):k * (2 + i)] = a[k * (1 + i):k * (2 + i)], a[k * i:k * (1 + i)]
            if b[k * i:k*(1 + i)]>b[k*(1 + i):k*(2 + i)]:
                b[k * i:k * (1 + i)], b[k * (1 + i):k * (2 + i)] = b[k * (1 + i):k * (2 + i)], b[k * i:k * (1 + i)]
        k = k * 2

    if a == b:
        print('YES')
    else:
        print('NO')


main()