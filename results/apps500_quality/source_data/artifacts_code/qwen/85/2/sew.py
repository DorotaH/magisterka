from fractions import Fraction


def gcd(x, y):
    while y:
        x, y=y, x%y
    return  x


def can_equalize(a, b):
    return  gcd(a, b) == 1


def min_minutes(a1, b1, a2, b2):
    if can_equalize(a1, b1) and can_equalize(a2, b2):
        return -1
    if can_equalize(a1, b1):
        return 1, a1, b1, a2, b2
    if can_equalize(a2, b2):
        return 1, a2, b2, a1, b1
    if 0 == a1 % 2 and 0 == b1 % 2:
        return 2, a1 // 2, b1 // 2, a2, b2
    if 0 == a2 % 2 and 0 == b2 % 2:
        return 2, a2 // 2, b2 // 2, a1, b1
    if 0 == a1 % 3 and 0 == b1 % 3:
        return 2, a1 // 3, b1 // 3, a2, b2
    if 0 == a2 % 3 and 0 == b2 % 3:
        return 2, a2 // 3, b2 // 3, a1, b1
    return  -1

a1, b1=map(int, input().split())
a2, b2=map(int, input().split())

result=min_minutes(a1, b1, a2, b2)
if not result == -1:
    print(result[0])
    print(result[1], result[2])
    print(result[3], result[4])
else:
    print(result)