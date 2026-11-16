def geometric_sum(n):
    return 0 if n < 0 else 1 / (pow(2, n)) + geometric_sum(n - 1)
