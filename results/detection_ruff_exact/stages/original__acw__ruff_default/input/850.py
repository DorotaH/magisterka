def is_triangleexists(a, b, c):
    if a != 0 and b != 0 and c != 0 and (a + b + c) == 180:
        return (a + b) >= c or (b + c) >= a or (a + c) >= b
    else:
        return False
