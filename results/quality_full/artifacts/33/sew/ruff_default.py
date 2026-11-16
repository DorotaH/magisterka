def decimal_To_Binary(N):
    B_Number = 0
    cnt = 0
    while 0 != N:
        rem, c = N % 2, pow(10, cnt)
        B_Number = B_Number + rem * c
        N = N // 2
        cnt = cnt + 1
    return B_Number
