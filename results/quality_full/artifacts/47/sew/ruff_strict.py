def compute_Last_Digit(A, B):
    variable = 1
    if B == A:
        return 1
    if (B - A) >= 5:
        return 0
    for i in range(A + 1, B + 1):
        variable = (variable * (i % 10)) % 10
    return variable % 10
