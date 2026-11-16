def count_Squares(m, n):
    if m > n:
        temp = m
        m = n
        n = temp
    return n * (1 + n) * (3 * m - n + 1) // 6
