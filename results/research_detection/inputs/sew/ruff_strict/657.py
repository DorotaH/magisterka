import math


def first_Digit(n):
    fact = 1
    for i in range(2, 1 + n):
        fact *= i
        while fact % 10 == 0:
            fact = int(fact / 10)
    while fact >= 10:
        fact = int(fact / 10)
    return math.floor(fact)
