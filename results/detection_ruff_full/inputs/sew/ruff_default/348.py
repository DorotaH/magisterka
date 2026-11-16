def bin_coff(n, r):
    val = 1
    if r > (n - r):
        r = n - r
    for i in range(0, r):
        val = val * (n - i)
        val = val // (i + 1)
    return val


def find_ways(M):
    n = M // 2
    a = bin_coff(2 * n, n)
    b = a // (1 + n)
    return b
