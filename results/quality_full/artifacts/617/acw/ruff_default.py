def min_Jumps(a, b, d):
    temp = a
    a = min(a, b)
    b = max(temp, b)
    if b <= d:
        return (b + d - 1) / b
    if d == 0:
        return 0
    return 1 if (d == a) else 2
