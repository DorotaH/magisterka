def last_Two_Digits(N):
    if N >= 10:
        return None
    fac = 1
    for i in range(1, N + 1):
        fac = (i * fac) % 100
    return fac
