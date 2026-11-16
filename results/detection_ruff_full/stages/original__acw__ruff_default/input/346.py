def zigzag(n, k):
    if n == 0 and k == 0:
        return 1
    return 0 if k == 0 else zigzag(n, k - 1) + zigzag(n - 1, n - k)
