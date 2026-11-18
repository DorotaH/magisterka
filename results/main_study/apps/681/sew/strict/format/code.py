import sys

MOD = 10**9 + 7


# Polymod
def polymod(P, Q):
    assert 1 == Q[-1]
    n = len(Q)
    while len(P) >= n:
        p = P[-1]
        for i in range(0, n):
            P[-i - 1] -= Q[-i - 1] * p
        assert 0 == P[-1]
        P.pop()
    return P


def polyprod(P, Q):
    n, m = len(P), len(Q)
    W = [0] * (m + n - 1)
    for i in range(n):
        for j in range(m):
            W[i + j] += P[i] * Q[j]
    return [w % MOD for w in W]


# Calc A^m * B
def power(A, B, m, mult):
    if m == 0:
        return B
    while m > 1:
        if m % 2 == 1:
            B = mult(A, B)
        A = mult(A, A)
        m //= 2
    return mult(A, B)


def calc_nth_term(init, linear_coeff, n):
    def mult(A, B):
        return polymod(polyprod(A, B), linear_coeff)

    ans = power([0, 1], [1], n, mult)
    return sum(init[i] * ans[i] for i in range(0, len(ans)))


n, m = [int(x) for x in input().split()]

linear_rec = [0] * (m + 1)
linear_rec[0] = -1
linear_rec[m - 1] = -1
linear_rec[m] = 1

print(calc_nth_term([1] * m, linear_rec, n) % MOD)
