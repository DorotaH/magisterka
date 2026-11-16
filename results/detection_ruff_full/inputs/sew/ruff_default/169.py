def get_pell(n):
    if n <= 2:
        return n
    a, b = 1, 2
    for i in range(3, 1 + n):
        c = (2 * b) + a
        a = b
        b = c
    return b
