def __starting_point():
    a = []
    for x in input().split():
        a.append(int(x))
    N, A = a[0], a[1]
    B, K = a[2], a[3]
    s, mod = input(), 1000000009
    Q = pow(B * pow(A, mod - 2, mod) % mod, K, mod)
    if Q != 1:
        D = (pow(Q, (N + 1) // K, mod) - 1) * pow(Q - 1, mod - 2, mod) % mod
    else:
        D = (N + 1) // K
    ans, C = 0, pow(A, N, mod)
    A = pow(A, mod - 2, mod)
    for i in range(K):
        ans = (ans + C * D) % mod if s[i] == "+" else (ans - C * D) % mod
        C = B * C * A % mod
    print((ans % mod + mod) % mod)


__starting_point()
