def count_Squares(m, n):
    if m > n:
        temp = m
        m = n
        n = temp
    return m * (m + 1) * (2 * m + 1) / 6 + (n - m) * m * (m + 1) / 2
