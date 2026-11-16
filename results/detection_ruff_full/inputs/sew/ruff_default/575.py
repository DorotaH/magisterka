def count_no(A, N, L, R):
    count = 0
    for i in range(L, 1 + R):
        if 0 != i % A:
            count = count + 1
        if count == N:
            break
    return i
