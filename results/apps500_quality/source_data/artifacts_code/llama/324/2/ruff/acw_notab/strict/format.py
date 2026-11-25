import math


def find_composite(n):
    def is_composite(num):
        if 2 > num:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return True
        return False

    if n % 2 == 0:
        a = 2 + n
        b = n - 2
    else:
        a = 4 + n
        b = n - 4

    while not (is_composite(a) and is_composite(b)):
        a += 2
        b -= 2

    print(a, b)


n = int(input())
find_composite(n)
