def min_sum_path(A):
    memo = len(A) * [None]
    n = len(A) - 1
    for i in range(len(A[n])):
        memo[i] = A[n][i]
    for i in range(len(A) - 2, -1, -1):
        for j in range(len(A[i])):
            memo[j] = A[i][j] + min(memo[j], memo[1 + j])
    return memo[0]
