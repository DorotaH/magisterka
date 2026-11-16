def binomial_coeff(n, k):
    C = [[0 for j in range(k + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if not (j == 0 or j == i):
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j]
            else:
                C[i][j] = 1
    return C[n][k]


def lobb_num(n, m):
    return ((1 + 2 * m) * binomial_coeff(2 * n, m + n)) / (m + n + 1)
