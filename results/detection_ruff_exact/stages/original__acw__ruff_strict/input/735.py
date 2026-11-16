def set_middle_bits(n):
    n |= n >> 1
    n |= n >> 2
    n |= n >> 4
    n |= n >> 8
    n |= n >> 16
    return (n >> 1) ^ 1


def toggle_middle_bits(n):
    return 1 if n == 1 else n ^ set_middle_bits(n)
