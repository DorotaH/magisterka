def is_abundant(n):
    fctrsum = sum([fctr for fctr in range(1, n) if n % fctr == 0], 0)
    return n < fctrsum
