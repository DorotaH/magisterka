def multiply_int(x, y):
    if y < 0:
        return -multiply_int(x, -y)
    if y == 0:
        return 0
    if y == 1:
        return x
    return x + multiply_int(x, y - 1)
