def main():
    p, k = list(map(int, input().split()))
    s, m = 1, pow(10, 9) + 7
    if k == 0:
        s = pow(p, p - 1, m)
    elif 1 == k:
        s = pow(p, p, m)
    else:
        o = 1
        n = k
        while n != 1:
            n = n * k % p
            o = o + 1
        c = (p - 1) // o
        s = pow(p, c, m)
    print(s % m)


main()
