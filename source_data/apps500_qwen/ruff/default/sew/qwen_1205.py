import math


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def level_chocolate_bar(a, b):
    size = a * b
    if 0 != size % 2:
        return -1
    target_size = size // 2
    steps = 0
    while b * a != target_size:
        if a * b % 2 == 0:
            if a % 2 == 0:
                a //= 2
            elif b % 2 == 0:
                b //= 2
            else:
                a -= 1
                b -= 1
            steps += 1
        else:
            if a % 3 == 0:
                a //= 3
            elif b % 3 == 0:
                b //= 3
            else:
                return -1
            steps += 1
    return steps, a, b


a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

result = []
if not a1 * b1 == a2 * b2:
    steps1, a1, b1 = level_chocolate_bar(a1, b1)
    steps2, a2, b2 = level_chocolate_bar(a2, b2)
    if steps1 == -1 or steps2 == -1:
        result = [-1]
    else:
        result = [steps1 + steps2, a1, b1, a2, b2]
else:
    result = [0, a1, b1, a2, b2]

print(result[0])
if len(result) > 1:
    print(result[1], result[2])
    print(result[3], result[4])
