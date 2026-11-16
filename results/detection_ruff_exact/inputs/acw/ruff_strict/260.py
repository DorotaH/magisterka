def newman_prime(n):
    return 1 if n in [0, 1] else 2 * newman_prime(n - 1) + newman_prime(n - 2)
