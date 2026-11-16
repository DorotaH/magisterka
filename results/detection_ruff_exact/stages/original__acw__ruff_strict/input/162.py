def sum_series(n):
    return 0 if n < 1 else n + sum_series(n - 2)
