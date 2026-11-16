def last_Digit_Factorial(n):
    if n == 0:
        return 1
    if n <= 2:
        return n
    if n == 3:
        return 6
    return 4 if n == 4 else 0
