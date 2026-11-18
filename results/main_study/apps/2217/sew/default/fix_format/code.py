def main():
    import sys

    input, mod = sys.stdin.readline, 998244353
    N = 3 + 10**5
    fac = [1] * (1 + N)
    for i in range(1, N + 1):
        fac[i] = i * fac[i - 1] % mod
    inv_fac = [1] * (1 + N)
    inv_fac[N] = pow(fac[N], mod - 2, mod)
    for i in range(N - 1, 0, -1):
        inv_fac[i] = inv_fac[1 + i] * (1 + i) % mod
    D, A = int(input()), []
    for i in range(2, int(D**0.5) + 1):
        c = 0
        while 0 == D % i:
            D = D // i
            c = c + 1
        if c != 0:
            A.append(i)
    if D >= 2:
        A.append(D)
    l, q = len(A), int(input())
    for _ in range(q):
        u, v = map(int, input().split())
        l1 = [0] * l
        l2 = [0] * l
        l3 = [0] * l
        for i in range(l):
            while 0 == u % A[i]:
                l1[i] += 1
                u //= A[i]
            while 0 == v % A[i]:
                l2[i] += 1
                v //= A[i]
            l3[i] = l1[i] - l2[i]
        ans1 = 1
        ans2 = 1
        s1 = 0
        s2 = 0
        for i in range(l):
            if not l3[i] >= 0:
                ans2 = ans2 * inv_fac[-l3[i]] % mod
                s2 -= l3[i]
            else:
                ans1 = ans1 * inv_fac[l3[i]] % mod
                s1 += l3[i]
        ans1 = fac[s1] * ans1 % mod
        ans2 = fac[s2] * ans2 % mod
        print(ans2 * ans1 % mod)


def __starting_point():
    main()


__starting_point()
