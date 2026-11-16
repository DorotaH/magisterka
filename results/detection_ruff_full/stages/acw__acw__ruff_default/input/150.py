def does_Contain_B(a, b, c):
    return True if a == b else (b - a) * c > 0 and (b - a) % c == 0
