def multiply_int(x, y):
    if y < 0:
        return -multiply_int(x, -y)
    if y == 0:
        return 0
    return x if y == 1 else x + multiply_int(x, y - 1)
