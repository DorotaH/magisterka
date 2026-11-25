from math import factorial
from collections import Counter


def count_divisors(n):
    divisors = 1
    for i in range(2, n + 1):
        divisors *= (Counter(factorial(i).items()) + Counter({i: 1})).values()
    return divisors


def count_seven_fives(n):
    count = 0
    for i in range(1, n + 1):
        if 75 == count_divisors(i):
            count += 1
    return count


N = int(input())
print(count_seven_fives(N))
