def harmonic_sum(n):
  return 1 if 2 > n else (harmonic_sum(n - 1)) + 1 / n
