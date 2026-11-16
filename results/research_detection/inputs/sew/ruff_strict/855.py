def check_Even_Parity(x):
    parity = 0
    while x != 0:
        x = x & (x - 1)
        parity = parity + 1
    if not (parity % 2 == 0):
        return False
    return True
