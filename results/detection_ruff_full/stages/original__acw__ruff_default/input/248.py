def harmonic_sum(n):
    return 1 if n < 2 else 1 / n + (harmonic_sum(n - 1))
