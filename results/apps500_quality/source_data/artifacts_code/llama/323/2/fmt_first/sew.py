import math


def  greatest_common_divisor():
    A, B=map(int, input().split())
    min_val, factorial = min(A, B), 1
    for  i in  range(1, 1 + min_val):
        factorial = i * factorial
    result=math.gcd(factorial, math.factorial(min(A, B)))
    return str(result)


print(greatest_common_divisor())
