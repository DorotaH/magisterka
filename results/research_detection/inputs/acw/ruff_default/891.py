def same_Length(A, B):
    while 0 < A and B > 0:
        A = A / 10
        B = B / 10
    return A == 0 and B == 0
