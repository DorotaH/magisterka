def count_Digit(n):
    count=0
    while  0 != n:
        n = n // 10
        count = count + 1
    return count