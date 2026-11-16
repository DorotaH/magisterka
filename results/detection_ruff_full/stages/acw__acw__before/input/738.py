def geometric_sum(n):
return 0 if 0 > n else geometric_sum(n - 1) + 1 / (pow(2, n))
