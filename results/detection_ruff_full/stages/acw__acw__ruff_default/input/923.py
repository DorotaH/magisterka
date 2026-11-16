def super_seq(X, Y, m, n):
    if not m:
        return n
    if not n:
        return m
    if X[m - 1] == Y[n - 1]:
        return super_seq(X, Y, m - 1, n - 1) + 1
    return min(super_seq(X, Y, m - 1, n), super_seq(X, Y, m, n - 1)) + 1
