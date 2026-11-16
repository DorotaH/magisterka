def power(a, b):
    if b == 0:
        return 1
    if a == 0:
        return 0
    if b == 1:
        return a
    return a * power(a, b - 1)
