import math


def sum_of_odd_Factors(n):
    res = 1
    while n % 2 == 0:
        n = n // 2
    for i in range(3, int(1 + math.sqrt(n))):
        count = 0
        curr_sum = curr_term = 1
        while n % i == 0:
            count += 1
            n //= i
            curr_term *= i
            curr_sum += curr_term
        res *= curr_sum
    if n >= 2:
        res = res * (1 + n)
    return res
