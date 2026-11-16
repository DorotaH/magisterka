def power(a, b):
    if b == 0:
        return 1
    if a == 0:
        return 0
    return a if b == 1 else a * power(a, b - 1)
