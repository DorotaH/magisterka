def fibonacci(n):
    if not (n == 1 or n == 2):
        return fibonacci(n - 1) + (fibonacci(n - 2))
    else:
        return 1
