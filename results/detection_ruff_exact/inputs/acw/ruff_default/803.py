def is_Perfect_Square(n):
    i = 1
    while i**2 <= n:
        if (n % i == 0) and (n / i == i):
            return True
        i = i + 1
    return False
