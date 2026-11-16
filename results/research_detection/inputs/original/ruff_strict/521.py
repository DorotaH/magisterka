def check_isosceles(x, y, z):
    if x != y & y != z & z != x:
        return True
    return False
