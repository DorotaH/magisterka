import math


def greatest_common_divisor():
    A, B = map(int, input().split())
    min_val = min(A, B)
    factorial = 1
    for i in range(1, min_val + 1):
        factorial *= i
    result = math.gcd(factorial, math.factorial(min(A, B)))
    return str(result)

print(greatest_common_divisor())
