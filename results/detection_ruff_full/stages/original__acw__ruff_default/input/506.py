def permutation_coefficient(n, k):
    P = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            P[i][j] = 1 if j == 0 else P[i - 1][j] + (j * P[i - 1][j - 1])
            if j < k:
                P[i][j + 1] = 0
    return P[n][k]
